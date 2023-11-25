---
title: "Probleme mit Server Side Events"
date: 2023-11-24
published: true
visible: true
categories:
  - Blog
tags:
  - spring-boot
  - server-side-events
toc: false
classes: wide
---
# Verzögerung bei der Erkennung von SSE-Verbindungsabbrüchen und Lösungen

Server Side Events (SSE) für die Kommunikation von Server zu Browser können verwendet werden, um die Clients über serverseitige Aktualisierungen der Daten zu informieren, die der Client-Browser dem Benutzer anzeigt. Dann kann z.B. eine Frontend-Single-Page-Anwendung entscheiden, neue Daten vom Server neu zu laden.

Bei der Implementierung dieser Lösung mit Spring Boot und Angular für ein Projekt haben wir beobachtet, dass, wenn das SSE-Verbindungstimeout auf der Serverseite auf Unendlich gesetzt ist, der Server selbst bei Senden von Keepalive-Ereignissen an den Client alle 10 - 30 Sekunden zur Vermeidung unterbrochener Verbindungen, einen Verbindungsabbruch erst nach etwa 10 Minuten erkennt. Dies resultiert aus einem `RTO` von bis zu 60 Sekunden und `tcp_retries2` von 15, wie unten erklärt.
Außerdem haben wir beobachtet, dass es in einigen Umgebungen notwendig zu sein scheint, dass der Server alle 10 Sekunden Keepalive-Ereignisse an den Client sendet, um zu verhindern, dass die Netzwerkinfrastruktur (Firewalls usw.) die Verbindung vorzeitig abbricht.

In diesem Blogbeitrag untersuchen wir die Gründe für diese Beobachtung und mögliche Lösungen wie WebSockets und die Begrenzung der Dauer der SSE-Verbindung auf der Serverseite, während wir auch erörtern, warum eine solche Verzögerung von 10 Minuten bei der Erkennung von Verbindungsabbrüchen problematisch ist:

- **Problem der verzögerten Erkennung**: Eine 10-minütige Verzögerung bei der Erkennung von Verbindungsabbrüchen ist problematisch, weil sie zu **ineffizienter Ressourcennutzung** führen kann, da der Server weiterhin Ressourcen für eine Verbindung bereitstellt, die effektiv tot ist. Diese Ineffizienz kann die Serverleistung beeinträchtigen und seine Kapazität, aktive Benutzer zu bedienen, einschränken.

## TCP und SSE-Begrenzungen
Die Verzögerung bei der Erkennung von Verbindungsabbrüchen mit SSE wird erheblich von den Eigenschaften des zugrundeliegenden TCP-Protokolls und der Natur von SSE selbst beeinflusst:

- **Einseitige Kommunikation von SSE**: SSE ist von Natur aus einseitig und erlaubt nur den Datenfluss vom Server zum Client. Dieses Design fehlt einem Mechanismus für den Client, periodische Bestätigungen oder Keep-Alive-Signale an den Server zurückzusenden, was es für den Server schwierig macht, umgehend zu erkennen, ob der Client getrennt wurde oder ob die Verbindung unterbrochen wurde.

- **Abhängigkeit von TCPs Timeout-Mechanismen**: SSE funktioniert über TCP, das Timeout-Mechanismen verwendet, um verlorene Pakete und Verbindungsprobleme zu erkennen. Diese Mechanismen beinhalten die Berechnung von `Retransmission Timeouts` (`RTO`) und den Einsatz von exponentiellen Backoff-Strategien für Paketwiederholungen. Jedoch ist TCP darauf ausgelegt, eine Verbindung konservativ als unterbrochen zu deklarieren, um vorübergehende Netzwerkprobleme elegant zu handhaben. Dies führt oft dazu, dass die Standard-TCP-Timeouts auf mehrere Minuten eingestellt sind, was zu Verzögerungen bei der Erkennung von Verbindungsabbrüchen in SSE führt.

- **Erste und nachfolgende RTOs**: Das anfängliche RTO von TCP liegt typischerweise bei etwa 1 Sekunde, passt sich aber auf der Basis von laufenden Round-Trip-Time (RTT)-Messungen bis zu **60 Sek** an. Das RTO erhöht sich exponentiell bei aufeinanderfolgenden Wiederholungstimeouts (exponentieller Backoff), was zu erheblichen Verzögerungen bei der Erkennung einer unterbrochenen Verbindung führen kann, insbesondere unter schwankenden Netzwerkbedingungen.

- **Systemebene TCP-Einstellungen**: Linux TCP-Einstellungen `tcp_retries1`` und `tcp_retries2` tragen zur Zeit bei, die benötigt wird, um unterbrochene Verbindungen zu erkennen. `tcp_retries2` ist typischerweise **15** auf einem üblichen Linux-Betriebssystem.

- **Fehlendes sofortiges Feedback in TCP**: TCP bietet keine unmittelbare Rückmeldung an die Anwendungsschicht über den Zustand der Verbindung. Das Protokoll muss mehrere Timeout-Zyklen und Wiederholungen durchlaufen, bevor es schlussfolgert, dass die Verbindung nicht mehr aktiv ist. Dieser Prozess ist zeitaufwendig, und während dieser Zeit bleibt die Anwendungsschicht (in diesem Fall SSE) über den Verbindungsabbruch im Unklaren.

- **Auswirkungen auf die SSE-Leistung**: Aufgrund dieser TCP-Eigenschaften könnte ein SSE-Server weiterhin versuchen, Ereignisse an einen Client zu senden, der nicht mehr verbunden ist, was zu verschwendeten Serverressourcen und möglichen Problemen bei der Anwendungsleistung führt, insbesondere in Szenarien, die Echtzeit-Datenaustausch oder hohe Benutzerkonkurrenz erfordern.

Die Kombination aus dem einseitigen Kommunikationsmodell von SSE und dem konservativen Ansatz von TCP bei der Verbindungsverwaltung führt zu inhärenten Verzögerungen bei der Erkennung von Trennungen in SSE-basierten Anwendungen.

## Lösungen

1. **WebSocket-Lösung**: Die Verwendung von WebSockets kann dieses Problem lösen, indem sie bidirektionale Kommunikation ermöglicht, was eine Echtzeiterkennung von Verbindungsproblemen und eine effizientere Ressourcenverwaltung erlaubt.

2. **Begrenzung der Dauer der SSE-Verbindung**: Das Konfigurieren von SSE-Verbindungen als kurzlebig (z. B. 30 Sekunden) zwingt die Clients, sich regelmäßig neu zu verbinden, was eine schnellere Erkennung von Verbindungsabbrüchen bei erhöhtem Overhead ermöglicht.

3. **Client-zu-Server-Keepalives**: Um ein responsiveres Verbindungsmanagement zu erreichen, sind benutzerdefinierte Lösungen wie bidirektionale Keep-Alives oder erweitertes Monitoring erforderlich, werden jedoch in SSE oder Spring Boot nicht inhärent unterstützt.

**Anmerkung:** Bei Verwendung von Spring Boot 3.x ist der Standardwert für das Timeout für SSE sowieso 30 Sekunden. Es kann auch auf Unendlich gesetzt werden, was nur funktioniert, solange der Server alle 10 Sekunden oder so Keepalive-Ereignisse sendet.

Zusammenfassend stellt die erhebliche Verzögerung bei der Erkennung von unterbrochenen SSE-Verbindungen eine Herausforderung in Bezug auf Ressourceneffizienz und Serverleistung dar. Obwohl SSE Vorteile hat, führt seine Abhängigkeit von TCP und das Fehlen bidirektionaler Kommunikation zu erheblichen Verzögerungen bei der Erkennung getrennter Clients. Die Annahme von Alternativen wie **WebSockets** oder **Strategien zur Begrenzung der Verbindungsdauer** kann eine sofortigere Erkennung und bessere Ressourcenverwaltung bieten, obwohl sie mit ihren eigenen Kompromissen und Implementierungsanforderungen einhergehen.

