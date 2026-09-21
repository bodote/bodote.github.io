---
title: "Der Issue Grundlage Skill: /issue-grundlage"
date: 2026-09-16
published: false
visible: false
categories:
  - Blog
tags:
  - Agentic
toc: true
classes: wide
---

# Meine Hypothesen
* Coding Agent sind inzwischen "schlau" genugt, um die komplette Produktion des Codes incl. Code-Review, Deployment etc. zu übernehmen
* das geht aber nicht "einfach so"
* Der Schlüssel ist die Orchestrierung, Guard Rails in Form von z.B.  Architekturvorgaben, prüfbaren Qualitätskritereien, die so engmaschig und zuverlässig sind, dass die Entwickler 100% vertrauen darin haben.
* Diese Architekturvorgaben, prüfbaren Qualitätskritereien sind als **Skills** realisiert, die aber NICHT von anderen Übernommen werden sondern werden von dem selben Entwicklerteam selbst entwickelt und immer weiter verfeinert.
* zu "Fremden" Skills kann vieleicht noch ein einzelner Entwickler 100% vertrauen haben, aber was, wenn sich doch Fehler einschleichen? Wer fixed diesen nachhaltig , sodass die auch in Zukunft nicht mehr auftreten ?
* "Fertige Skillsets" wie z.B. GSD oder BMAD sind beeindruckend, funktionieren für mich für kleinere Projekte, bei denen nicht viel auf dem Spiel steht. Aber für große Projekt habe ich keine 100% vertrauen 
* Daher: Skill müssen (jedenfalls derzeit noch) selbst entwickelt werden.
* Skills werden inkrementell verbessert


# Beispiel 1: der "Issue-Grundlage" Skill

Vorraussetzung: Monorepo für BE **UND** FE, eine Trennung von beiden macht m.E. für Codings Agents keinen Sinn

## Ausgangssituation:

ich kopiere den Issue Text aus Gitlab in den Prompt. Funktioniert für reine Backend Task okish, aber nicht nicht für Frontend

### Das Problem 

1. warum selber Kopieren? kann doch der coding agent auch!

2. Problem :  Anforderungen für FE liegen größtenteils im Figma. Aber : wir haben (noch) kein fertiges Design System, sondern nur die Entscheidung "spartan-ng" zu verwenden. "Spartan-ng" ist ein "shadcn"-Componentenset für Angular.

### Einschub: Shadcn:

shadcn/ui is a set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks and AI models. Open Source. Open Code.

This is not a component library. It is how you build your component library.

## Lösung 

### Iteration 1

* Skill für gitlab , basierend auf der `glab`-CLI
* Figma-Dev-mode + Figma MCP -Server + Figma "Besipiel-Prompt kopieren"  Prompt mit Link in meinen Prompt kopieren
 
#### Jedoch:

* Skill für gitlab läuft
* Aber : Figma-Bespielprompt bring noch nicht die Detais für FE wie gewünscht: FE hat viele Fehler die alle nachgebessert werden müsse, nicht manuell aber mit je einem Prompt pro Problem, was viel Arbeit macht

### Iteration 2
* Figma Skill der den Agent anweist auf **KEINEN FALL** ein Design auf grund eines Figma-PNG-Screenshots zu machen, sondern der den Agent zwingt die Figma - Design-Properties zu lesen und diese zu verwenden
* Figma - Design-Properties  sind im Figma jedoch verteilt: 
    * verschiedenen Aspekte des Designs stehen auf  verschiedenen "Ebenen" 
    * in verschiedenen "Objecten", 
    * Zukünftige aber für dieses aktuelle Issue noch nicht relevante Details sind auch schon drin, müssen (noch) ignoriert werden
    * Coding agent schaft es nicht sich aus einem einzigen Firma Link die relevanten Punkte rauszupicken
* daher: alle relevanten Figma links (Typischerweise 10-20) manuell zusammensuchen und ins Issue reinkopieren, genau an die Stellen im Issue, wo die zugehörigen Akzeptanzkriterien stehen. 

#### Jedoch
* viel manuelle recherche in Figma, Entwickler muss die passenden Stellen suchen, die Links erzeugen und manuell ins Issue kopieren-> viel Arbeit
* Ergebniss besser, aber nicht überzeugend, Coding Agent übersieht nach wie vor viele wichtige Design-Details

### Iteration 3
* neuer Skill "Issue Grundlage"
* Figma Entwürfe so anlegen, dass der Coding Agent sich selbstständig zurecht findet

#### Konzept "Issue Grundlage": 
* Issue inhalt zunächst ins Projekt unter tmp/issue<nr>.md kopieren lassen.
* präzise Anweisungen, wie der Agent Figma-mcp und die Links zum Figma nutzen muss:
    * siehe "Pflichtschritt F — Figma-Komponenten-Varianten" im "issue-grundlage" - Skill des Projekts
* tmp/issue<nr>.md stark erweitern lassen um alle interessanten und auch impliziten Details, insb. bezüglich Design, aber auch alle fachlichen Definitionslücken rigoros aufdecken und per User - Rückfrage schließen. 
* Ergebniss ist ein neues MD-File, das 3-4 mal so lang ist wie das ursprüngliche Issue im Gitlab 

#### Jedoch
* Funktioniert schon besser, aber immer noch Lücken und Missverständnisse

### Iteration 4
* mehrer Agenten (Claude und Codex) mit dem selben Skill auf das selbe Issue und die selben Figma links ansetzen.
* 2 konkurrierende Ergebnisse produzieren
* Finaler Vergleich, Deduplication, aufdecken von Widersprüchen durch einen Coding Agent (hier: Claude weil größere Tokenbudget)
* Ergebniss: Liste von "offene Punkte" die der Entwicker mit PO und UX-Designerin klären muss.



# Der Skill
(Stand vom 21.Sept.2026) 
### Description Header:
```
---
name: issue-grundlage
description: >-
  Erstellt vor der Planung aus einem GitLab-Work-Item und seinem Figma-Design ein
  Grundlagendokument mit Akzeptanzkriterien, Design-Specs und Klaerungsliste. Trigger:
  "Issue aufarbeiten", "Grundlagendokument erstellen", "Issue plus Figma". Benoetigt
  die Work-Item-Nummer; eine Figma-URL ist optional.
argument-hint: "<gitlab-work-item-nummer> [figma-url], z. B. 92"
---
```

# Issue-Grundlage — Work Item + Figma zu einem Grundlagendokument

Diese Skill erzeugt **die Grundlage fuer den Implementierungsplan** — nicht den Plan selbst.
Ergebnis ist ein Dokument, in dem jedes Akzeptanzkriterium des Work Items neben den konkreten
Figma-Design-Details steht, und eine Liste der Punkte, die der Nutzer klaeren muss.

Zwei unabhaengige Analysten arbeiten dasselbe Work Item aus:

| Analyst | Modell / Effort | Ergebnisdatei |
| --- | --- | --- |
| Claude-Subagent | Opus 5 / High | `tmp/item<N>-opus5.md` |
| codex-CLI | gpt-5.6-sol / high | `tmp/item<N>-gpt5.6-sol.md` |
| **Zusammenfuehrung** | Opus 5 / High | `docs/item<N>-final.md` |

Dazu der geteilte Issue-Snapshot `tmp/issue-grundlage/issue<N>.md`.

**Nur das finale Dokument liegt in `docs/` und wird eingecheckt.** Die beiden
Analysten-Zwischenergebnisse und der Snapshot liegen unter `tmp/` (git-ignoriert) — sie sind
Arbeitsmaterial fuer die Zusammenfuehrung, kein Projektartefakt. Niemals ein `item<N>-opus5.md`
oder `item<N>-gpt5.6-sol.md` nach `docs/` schreiben und nichts davon zu Git hinzufuegen.

> **Kein Code, kein Plan.** Diese Skill liest **keinen** Quellcode und schreibt **keinen**
> Implementierungsplan. Sie beantwortet nur: *Was ist gefordert, wie sieht es im Figma genau aus,
> und was ist noch offen?* Der Plan entsteht erst danach — aus `docs/item<N>-final.md`, nachdem der
> Nutzer die offenen Punkte geklaert hat.

## Erforderliche Eingabe

1. **Pflicht:** die **Work-Item-Nummer** `<N>` (z. B. `92` aus
   `https://git.office.brand-ad.de/guardops/issues/-/work_items/92`).
   **Fehlt sie, stoppen und fragen.** Nicht aus dem Branch-Namen raten — ein Branch kann zu einem
   Task gehoeren, waehrend die Anforderung am uebergeordneten Work Item haengt.
2. **Optional:** eine **Figma-URL**. Nur noetig, wenn im Work Item keine steht (siehe Phase 1).

## Nicht verhandelbare Regeln

- **Kein Quellcode.** Weder Analysten noch Merger lesen `backend/src/**`, `frontend/src/**`, Tests,
  Build- oder Konfigurationsdateien; kein `git diff`, kein `git log`. Ob und wie etwas bereits
  implementiert ist, ist hier ausdruecklich **nicht** die Frage.
- **Screenshots sind keine Designquelle.** Bilder, die am Issue haengen, dienen hoechstens der
  Orientierung. Verbindliche Design-Werte kommen **ausschliesslich** aus dem Figma-MCP. Ein
  Screenshot ersetzt niemals den Figma-Link.
- **Nichts erfinden.** Jede Aussage im Dokument ist entweder mit einer Issue-Stelle oder mit einer
  **Figma-Node-ID** belegt. Alles andere gehoert in die Klaerungsliste (Abschnitt 10) — nicht in die
  Spezifikation. Kein „vermutlich", kein „analog zu", kein stilles Auffuellen von Luecken.
- **Anti-Pattern-Regel (Figma-Luecken):** Eine „Luecke im Figma" darf **erst** behauptet werden,
  wenn der Komponenten-Set-Lookup (Pflichtschritt F, Schritte 1–4) durchgefuehrt wurde und nichts
  ergeben hat. Eine notierte Vermutung ohne durchgefuehrten Lookup ist ein Fehler, kein Finding.
- **Nur die drei Ergebnisdateien schreiben** (plus der Snapshot in Phase 0). Keine Aenderung an
  bestehenden Dokumenten, kein `git add`, kein Commit.
- Modell und Effort der Analysten sind fest verdrahtet und **unabhaengig vom Modell, mit dem diese
  Skill aufgerufen wurde**.

---

## Pflichtschritt F — Figma-Komponenten-Varianten

**Dieser Abschnitt ist der Kern der Skill. Beide Analysten arbeiten ihn vollstaendig ab.**

`get_metadata` / `get_design_context` auf einer Komponenten-**INSTANZ** zeigen **nur den aktuell
eingestellten Variant-State**. Andere States (Emptystate, Skeleton, Hover, Disabled, Error, …) sind
darin **unsichtbar** — sie existieren nur am **Component-Set** (in der Figma-UI: „Komponenten-
verhalten untersuchen"). Ohne diesen Schritt sieht eine Analyse vollstaendig aus, obwohl States
fehlen: **jede Instanz ist grundsaetzlich verdaechtig.**

Darum MUSS bei jeder Figma-Analyse:

1. **Einmal pro Datei** ein vollstaendiges Komponenten-Inventar erheben. Wenn der Harness
   `list_file_components_for_code_connect(fileKey)` anbietet, dieses Tool aufrufen; es liefert alle
   **published Component-Sets** inkl. Variant-Properties, Optionen und Node-IDs. Da der lokale
   Codex-Server `figma-desktop` dieses Tool nicht anbietet, verwendet Codex stattdessen
   `get_metadata` auf der **„Components"-Page** der aktiven Datei. Dieser Weg erfasst auch lokale,
   unveroeffentlichte Sets. Den verwendeten Weg in Abschnitt 11 nennen. Ist weder das Listen-Tool
   noch die Components-Page erreichbar, die Analyse als unvollstaendig markieren; der Schritt darf
   nie stillschweigend entfallen.
2. **Jede** in den analysierten Frames vorkommende **Instanz** (erkennbar an `data-name` /
   Layer-Name) gegen dieses Inventar **matchen**.
3. Fuer **jede** Komponente **ALLE** Variant-Properties **disponieren** — Ergebnis als Pflicht-
   Tabelle (Abschnitt 4.2 der Berichtsstruktur):

   `Komponente | Node-ID Set | Variant-Properties (alle Optionen) | Disposition`

   Disposition ist entweder **„referenziert: Node-ID …"** oder **„nicht relevant, weil …"**.
   **Eine verwendete Komponente ohne Zeile bedeutet: die Analyse ist unvollstaendig.**
4. **Relevante Varianten aufloesen:** `get_metadata` auf die Set-Node → Node-ID des
   `State=…`-Symbols → `get_screenshot` bzw. `get_design_context` pro Variante → **Node-ID ins
   Ergebnisdokument**.

### Figma-Zugang je Harness — zwei verschiedene Mechanismen

**Claude Code: MCP-Tools.** `mcp__plugin_figma_figma__<name>` fuer die Cloud-Anbindung,
`mcp__figma-desktop__<name>` fuer den lokal laufenden Dev-Mode-Server. MCP-Tools sind *deferred*:
vor dem ersten Aufruf per `ToolSearch` laden. Bei Unklarheit an den Tool-Namen im Tool-Listing des
laufenden Harness orientieren, nicht raten.

**Codex: lokaler MCP-Server.** Codex verwendet den in der Codex-Konfiguration eingetragenen
Dev-Mode-Server `figma-desktop` ueber `mcp__figma_desktop__<name>`. Die Tools koennen deferred sein
und im anfaenglichen Tool-Listing fehlen; vor einer Nichtverfuegbarkeitsmeldung im Runtime-
Tool-Katalog gezielt nach dem Praefix `mcp__figma_desktop__` suchen. Zuerst
`.codex/skills/figma-desktop/SKILL.md` vollstaendig lesen. Vor jedem `get_design_context` ausserdem
den verpflichtenden Skill `figma:figma-design-to-code` laden, dabei aber den lokalen Namespace
beibehalten.

Der lokale Server arbeitet mit dem in Figma Desktop aktiven Dokument. Seine Tools akzeptieren
`nodeId` und je nach Tool `clientFrameworks` / `clientLanguages`, aber **kein `fileKey`**. Nicht auf
`mcp__codex_apps__figma_*`, Web-Browsing oder die Figma-REST-API ausweichen. Ist das falsche Figma-
Dokument aktiv, den Nutzer bitten, die verlinkte Datei in Figma Desktop zu aktivieren, und danach
erneut aufrufen.

`fileKey` ist der Pfadbestandteil der URL und bleibt als Quellenbeleg im Ergebnisdokument:
`https://www.figma.com/design/<fileKey>/<Name>?node-id=<a>-<b>` → in Tool-Aufrufen wird `node-id`
als `<a>:<b>` geschrieben. Claude-/Cloud-Tools erhalten `fileKey`, wenn ihr Schema ihn verlangt;
Codex sendet beim lokalen `figma-desktop` nur `nodeId` und die vom konkreten Tool unterstuetzten
weiteren Parameter.

---

## Analysekatalog (beide Analysten, identisch)

Beide arbeiten **genau diesen** Katalog ab — nur so sind die zwei Ergebnisse vergleichbar.

### A1 — Anforderungen und Akzeptanzkriterien vollstaendig erfassen

Quelle ist **ausschliesslich** der Snapshot `tmp/issue-grundlage/issue<N>.md`: Beschreibung, **alle
Tasks** und **alle Kommentare**.

**AK-IDs sind verbindlich und stabil zu bilden** (die Zusammenfuehrung haengt daran):

- Die Nummerierung des Issues uebernehmen. Aus dem Abschnitt „**2. Berechnung**" wird `AK2`, sein
  erster Aufzaehlungspunkt `AK2.1`, der zweite `AK2.2` — in **Dokumentreihenfolge**, ohne
  Umsortierung, ohne Zusammenfassen zweier Punkte zu einem.
- Anforderungen, die **nur** in einem Kommentar stehen, als `AKK1`, `AKK2`, … fuehren, jeweils mit
  Autor und Datum des Kommentars.
- Anforderungen aus einem **Task** als `T<task-iid>.1`, `T<task-iid>.2`, … fuehren.
- Jede AK-Zeile bekommt den **Wortlaut** aus dem Issue (gekuerzt nur, wo eindeutig), nicht eine
  Paraphrase.

### A2 — Tasks

Jeder Task des Work Items bekommt eine Zeile: `iid | Titel | Typ | Bereich (BE/FE) | eigene
Anforderungen? | Bezug zu AK`. Tasks ohne eigene Beschreibung ausdruecklich als „nur Titel, keine
zusaetzliche Anforderung" markieren — nicht weglassen, damit sichtbar bleibt, dass sie geprueft
wurden.

### A3 — Figma-Inventar

- **Alle** Figma-Links aus Beschreibung, Tasks und Kommentaren aufloesen; je Link `get_metadata`
  auf die Node, dann `get_design_context` fuer die relevanten Frames.
- Kindbaum jedes Frames durchgehen: Frame-Namen, Reihenfolge, sichtbare Texte (deutsch!),
  Zahlenformate, Icons, Zustaende.
- **Design-Specs mitnehmen:** Typografie, Farben/Token-Namen (`get_variable_defs`), Abstaende,
  Geometrie, Radien, Breakpoints — als Werte **mit** Token-Namen, nicht nur „grau".
- Nodes, die als Design-Annotation/Spec-Sheet erkennbar sind (Style-Annotations, Spec-Frames), als
  solche kennzeichnen: sie sind Referenz fuer Werte, aber kein umzusetzender Screen.
- **Pflichtschritt F vollstaendig ausfuehren.**

### A4 — Zuordnung AK ↔ Figma (Kern des Dokuments)

Jede AK-Zeile aus A1 bekommt genau eine Zeile in der Zuordnungstabelle mit:
`AK-ID | Kurztext | Figma-Node-ID(s) | konkrete Design-Details (Texte, Werte, Zustaende) | Status`.

Status ist einer von:

| Status | Bedeutung |
| --- | --- |
| `belegt` | Figma zeigt das Kriterium eindeutig; Node-ID genannt. |
| `teilweise belegt` | Figma zeigt einen Teil; der fehlende Teil ist in Abschnitt 10 als offener Punkt gefuehrt. |
| `kein Figma-Bezug` | Rein fachliches/Backend-Kriterium ohne UI-Anteil — mit Begruendung. |
| `im Figma nicht gefunden` | **Nur zulaessig nach vollstaendigem Pflichtschritt F**, mit Angabe, was gesucht wurde. |
| `widerspruechlich` | Issue und Figma sagen Unterschiedliches → Abschnitt 9. |

### A5 — Detailspezifikation je AK

Fuer jedes AK mit UI-Anteil so ausformulieren, dass ein Entwickler es **ohne Rueckfrage** umsetzen
koennte: exakte deutsche Beschriftungen und Texte, Zahlen-/Datumsformate, Sortierung und
Standardwerte, Grenzwerte und Validierung, Fehler-, Lade- und **Leerzustaende**, Interaktionen und
Zustandsuebergaenge, Barrierefreiheit (Label, Fokus, Rollen). Jeder Wert mit Herkunft: Issue-Stelle
oder Figma-Node-ID. Was sich nicht belegen laesst, wandert nach Abschnitt 10 — **nicht** raten.

### A6 — Ueberdeckung und Unterdeckung

- **Im Figma vorhanden, im Issue nicht gefordert** → Abschnitt 7 (Scope-Kandidat; der Nutzer
  entscheidet, ob das in den Scope gehoert).
- **Im Issue gefordert, im Figma nicht auffindbar** → Abschnitt 8, mit dem Nachweis, dass
  Pflichtschritt F durchgefuehrt wurde.

### A7 — Widersprueche

Drei Arten, jeweils mit Belegen auf **beiden** Seiten:

1. **Issue gegen Figma** — z. B. Text, Reihenfolge, Anzahl oder Schwellwert weicht ab.
2. **Issue gegen Issue** — Beschreibung gegen Kommentar, oder Kommentar gegen Kommentar. Grundregel:
   der **juengere** Kommentar hat Vorrang — das ist eine **Annahme** und muss als offener Punkt
   gefuehrt werden, wenn daran eine Umsetzungsentscheidung haengt.
3. **Figma gegen Figma** — zwei Frames oder eine Variante gegen ihr Spec-Sheet widersprechen sich;
   auch Widersprueche zum dokumentierten spartan-ng-Standard hier melden (mit Node-ID), statt sie
   ungeprueft zu uebernehmen.

### A8 — Vollstaendigkeits- und Widerspruchsfreiheitspruefung

Am Ende ausdruecklich pruefen und im Dokument bestaetigen:

- Jedes AK aus A1 hat eine Zeile in A4. (Anzahl abgleichen und **beide Zahlen nennen**.)
- Jede verwendete Komponente hat eine Zeile in der Varianten-Tabelle (Pflichtschritt F.3).
- Jeder Figma-Link aus dem Issue ist aufgeloest oder mit Begruendung verworfen.
- Kein Status `im Figma nicht gefunden` ohne durchgefuehrten Pflichtschritt F.

### A9 — Klaerungsliste

Alle offenen Punkte als `U1`, `U2`, … Jeder Eintrag: **Frage** (eine Zeile, entscheidbar), **Bezug**
(AK-ID / Node-ID / Issue-Stelle), **warum es blockiert** (was ohne Antwort falsch werden kann),
**Optionen** und — wo moeglich — eine **Empfehlung mit Begruendung**. Keine rhetorischen Fragen und
keine Punkte, die sich aus Issue oder Figma bereits beantworten lassen.

---

## Verbindliche Berichtsstruktur (beide Analysten, exakt)

Die Zusammenfuehrung in Phase 4 haengt an dieser Gliederung — nicht abweichen.

```markdown
# Grundlagendokument Work Item <N> — „<Titel>" — Analyst: <Modell/Effort>

## 0. Kopf
- Work Item: <URL> — „<Titel>", Typ, Labels, State
- Tasks: <iids> (<Anzahl>)
- Kommentare beruecksichtigt: <Anzahl> (nicht-System)
- Quellen-Snapshot: tmp/issue-grundlage/issue<N>.md
- Figma-Datei: <fileKey> — „<Dateiname>"
- Analysierte Figma-Nodes: <node-id> (<Kurzname>), …
- Datum: <YYYY-MM-DD>

## 1. User Story und Ziel
## 2. Anforderungen und Akzeptanzkriterien (A1)
| AK-ID | Wortlaut (Issue) | Quelle (Beschreibung/Kommentar/Task) | Bereich (BE/FE/beide) |

## 3. Tasks (A2)
| iid | Titel | Typ | Bereich | eigene Anforderungen | Bezug zu AK |

## 4. Figma-Inventar (A3)
### 4.1 Analysierte Frames
| Node-ID | Frame-Name | Zweck | Screen / Spec-Sheet |
### 4.2 Komponenten-Varianten-Disposition (PFLICHT — Pflichtschritt F.3)
| Komponente | Node-ID Set | Variant-Properties (alle Optionen) | Disposition |
### 4.3 Design-Specs (Typografie, Farben/Token, Abstaende, Geometrie)

## 5. Zuordnung AK ↔ Figma (A4)
| AK-ID | Kurztext | Figma-Node-ID(s) | Design-Details | Status |

## 6. Detailspezifikation je AK (A5)
### AK<x> — <Titel>
- **Anforderung (Issue):** …
- **Figma-Beleg:** <node-id> — …
- **Konkrete Vorgaben:** Texte, Formate, Zustaende, Grenzwerte, Interaktion, A11y
- **Offen:** <U-IDs oder „keine">

## 7. Im Figma vorhanden, im Issue nicht gefordert (A6)
## 8. Im Issue gefordert, im Figma nicht auffindbar (A6 — nur nach Pflichtschritt F)
## 9. Widersprueche (A7)
| # | Art | Seite A (Beleg) | Seite B (Beleg) | Auswirkung |

## 10. Offene Punkte — Klaerung durch den Nutzer (A9)
### U1 — <Frage>
- **Bezug:** …
- **Warum blockierend:** …
- **Optionen:** …
- **Empfehlung:** …

## 11. Vollstaendigkeitspruefung, nicht geprueft und Annahmen (A8)
- AK gesamt: <n> — Zeilen in Abschnitt 5: <n>
- Komponenten mit Instanz im Frame: <n> — Zeilen in 4.2: <n>
- Figma-Links im Issue: <n> — aufgeloest: <n>
- Nicht geprueft / nicht verfuegbar: …
- Annahmen: …
```

---

## Ablauf

### Phase 0 — Vorbereitung und Snapshot

1. **`<N>`** aus dem Argument uebernehmen; fehlt es, stoppen und fragen.
2. Verzeichnisse anlegen und **alte Ergebnisdateien dieses `<N>`** bereinigen (die drei Dateien aus
   der Tabelle oben), damit nichts aus einem frueheren Lauf kollidiert. Dem Nutzer kurz nennen, was
   bereinigt wurde. Dateien anderer Nummern bleiben unangetastet.

   ```bash
   mkdir -p tmp/issue-grundlage docs
   ```

3. **Work Item, Tasks und Kommentare holen.** Alle `glab`-Aufrufe mit
   `GLAB_HOST=git.office.brand-ad.de` und — auf macOS — `dangerouslyDisableSandbox: true`; die
   Aufrufe brauchen Netz und laufen teils >60 s, darum grosszuegiges `timeout` setzen.

   ```bash
   export GLAB_HOST=git.office.brand-ad.de
   glab api "projects/guardops%2Fissues/issues/<N>"                       > tmp/issue-grundlage/issue<N>.json
   glab api "projects/guardops%2Fissues/issues/<N>/notes?per_page=100"    > tmp/issue-grundlage/issue<N>-notes.json
   ```

   **Tasks (Child-Work-Items) gibt es in der REST-API nicht** — sie haengen als Hierarchie-Widget am
   Work Item und werden per GraphQL geholt:

   ```bash
   glab api graphql -f query='query { namespace(fullPath: "guardops/issues") {
     workItems(iid: "<N>") { nodes { iid title workItemType { name } widgets {
       ... on WorkItemWidgetHierarchy {
         parent { iid title }
         children { nodes { iid title workItemType { name } } } } } } } }' \
     > tmp/issue-grundlage/issue<N>-tasks.json
   ```

   Die Child-`iid`s sind normale Issue-`iid`s — Beschreibung und Kommentare je Task damit ueber
   dieselben REST-Endpunkte holen:

   ```bash
   for T in <task-iids>; do
     glab api "projects/guardops%2Fissues/issues/$T"                    > tmp/issue-grundlage/task$T.json
     glab api "projects/guardops%2Fissues/issues/$T/notes?per_page=100" > tmp/issue-grundlage/task$T-notes.json
   done
   ```

   Hat das Work Item ein `parent`, dessen Beschreibung ebenfalls lesen und im Snapshot als
   **Kontext** kennzeichnen (nicht als eigene AK-Quelle).

4. **Snapshot `tmp/issue-grundlage/issue<N>.md` schreiben.** Beide Analysten lesen **denselben**
   Snapshot, damit sie garantiert gegen identische Anforderungen arbeiten (und codex nicht auf
   eigene Netzwerkzugriffe angewiesen ist). Inhalt:

   - Titel, `iid`, Typ, `state`, Labels, `web_url`,
   - die **vollstaendige, ungekuerzte** Beschreibung,
   - je Task: `iid`, Titel, Typ und die **vollstaendige** Beschreibung (oder „keine Beschreibung"),
   - **alle nicht-System-Kommentare** (`.system == false`) des Work Items und der Tasks in
     chronologischer Reihenfolge, mit Autor und Datum — Kommentare enthalten regelmaessig spaetere
     Entscheidungen, die den Beschreibungstext ueberschreiben,
   - eine Liste **aller** Figma-Links aus Beschreibung, Tasks und Kommentaren:

     ```bash
     grep -ohE 'https://www\.figma\.com/design/[^ )"]*' tmp/issue-grundlage/issue<N>.md | sort -u
     ```

   Nichts zusammenfassen, nichts weglassen — der Snapshot ist die Sollquelle.

### Phase 1 — Figma-Link sicherstellen (ggf. Rueckfrage)

Aus dem Snapshot die Figma-Links ziehen und `fileKey` + `node-id`s isolieren. Jedes Issue **sollte**
mindestens einen echten Figma-Link haben. Die **vollstaendigen URLs** ebenfalls aufbewahren — der
codex-Prompt in Phase 3 braucht sie, um die aktive Desktop-Datei und die Node-IDs eindeutig zu
pruefen.

- **Link gefunden:** weiter mit Phase 2. Mehrere Links: **alle** an beide Analysten uebergeben.
- **Kein Link, aber die Skill wurde mit Figma-URL-Argument aufgerufen:** diese verwenden.
- **Kein Link und kein Argument:** **stoppen und den Nutzer nach der Figma-URL fragen.** Dabei
  ausdruecklich sagen, dass am Issue haengende **Screenshots keine gueltige Designquelle** sind und
  eine `figma.com/design/...?node-id=…`-URL gebraucht wird. Nicht mit einem geratenen Link
  weiterarbeiten und nicht ohne Figma starten.

Danach kurz ausgeben: `<N>`, Titel, Anzahl Tasks, Anzahl Kommentare, `fileKey` und die gefundenen
Node-IDs. Ab hier laufen die Phasen 2–5 **am Stueck durch**; ausser den Abbruchfaellen in Phase 0/1
gibt es keine Rueckfrage mehr.

### Phase 2 — Analyst 1: Claude-Subagent (Opus 5 / High)

Einen Subagenten mit `subagent_type: "issue-grundlage-opus5"` starten (Definition:
`.claude/agents/issue-grundlage-opus5.md`, Modell/Effort dort fest verdrahtet). **Kein** inline
`model`-Argument — das kann nur grobe Aliase und keinen Effort.

> Die Definition hat absichtlich **keine** `tools:`-Allowlist. Eine Allowlist filtert die
> MCP-Server heraus — der Subagent kaeme dann nicht an die Figma-Tools und wuerde Pflichtschritt F
> ueber einen Ersatzweg erledigen. Nicht „aufraeumen".

Der Prompt uebergibt: `<N>` und die Work-Item-URL, den Snapshot-Pfad, `fileKey` und **alle**
Figma-Node-IDs mit ihrer Herkunft, den Zielpfad `tmp/item<N>-opus5.md` und den Hinweis, dass
Analysekatalog, **Pflichtschritt F** und Berichtsstruktur vollstaendig in
`.agents/skills/issue-grundlage/SKILL.md` stehen und exakt zu befolgen sind.

#### Wenn der Subagent kein MCP hat: Ursache pruefen, nicht ausweichen

Meldet der Subagent, die Figma-MCP-Tools seien nicht aufrufbar, ist die **haeufigste Ursache eine
`tools:`-Allowlist in seiner Agent-Definition** — die filtert alle MCP-Server heraus, und
`ToolSearch` findet dann *ueberhaupt keine* deferred Tools. Belegt am 2026-08-11: mit Allowlist
schlug jeder Figma-Aufruf fehl, nach dem Entfernen der Zeile luden dieselben Tools im selben
Agent-Typ sofort — **ohne** Neustart von Claude Code. Zwei Fallen dabei:

- Die Meldung „`ListMcpResourcesTool` is disabled for this session, in subagents as well as here"
  betrifft **nur dieses eine Tool**. Sie ist **kein** Beleg, dass MCP session-weit aus ist — ein
  Gegentest mit einem `general-purpose`-Subagenten (der keine Allowlist hat) entscheidet das in
  wenigen Sekunden und ist vor jeder anderen Erklaerung faellig.
- Eine Aenderung an der Agent-Definition greift erst fuer **danach** gestartete Subagenten. Einen
  Lauf, der Sekunden nach der Aenderung startet, kann noch die alte Definition treffen.

Weicht der Subagent stattdessen auf Sekundaerquellen (aeltere `tmp/`-Artefakte) oder die
Figma-REST-API aus, entsteht eine Analyse, die belegt **aussieht**, aber Pflichtschritt F nicht
ausgefuehrt hat. Die REST-API ist auch kein voller Ersatz: `/variables/local` gibt HTTP 403, die
Token-Klarnamen fehlen dann komplett.

#### Rueckfallweg: Pflichtschritt F.1 macht der Orchestrator

Laesst sich MCP im Subagenten nicht herstellen, erhebt **der Orchestrator** die Figma-Rohdaten
selbst — er hat MCP — und legt sie als Verifikationsdatei ab:

```
tmp/issue-grundlage/figma<N>-mcp-verify.md
```

Mindestinhalt, jeweils mit dem verwendeten Tool-Namen als Herkunft:

1. `list_file_components_for_code_connect(fileKey)` oder, beim lokalen Codex-Server, `get_metadata`
   auf der Components-Page — **vollstaendig**: jede gefundene Komponente mit Node-ID, Typ,
   **allen** Variant-Properties samt Optionen und Default. Das ist das Inventar fuer
   Pflichtschritt F.2/F.3; den verwendeten Erhebungsweg nennen.
2. `get_variable_defs(<Hauptnode>)` und je relevanter Variante — Token-Klarnamen **mit** Werten.
   Ohne diesen Aufruf fehlen dem Dokument die Token-Namen (`/variables/local` der REST-API ist
   403-gesperrt, liefert also keinen Ersatz).
3. Kurze, belastbare Schlussfolgerungen aus dem Inventar (welche Variante welches AK belegt, welche
   Komponente trotz Set nirgends instanziiert ist, welche Komponente auf einer Archiv-Page liegt).

Der Weg ist ausdruecklich der **Rueckfall**, nicht der Normalfall: der Analyst soll Figma selbst
lesen, weil er dabei Fragen stellen kann, die im Voraus niemand kennt. Wird die Datei gebraucht,
gehoert der Grund in Abschnitt 11 des Analysedokuments.

Diese Datei wird beiden Analysten im Prompt genannt. Der Claude-Subagent behandelt sie als
**Primaerbeleg** (eigener Marker, z. B. `[MCP]`) und darf Pflichtschritt F damit als erfuellt
ansehen; codex ruft die MCP-Tools zusaetzlich selbst auf (eigener Prozess, eigene MCP-Verbindung)
und nutzt die Datei als Gegenprobe. Fehlt die Datei, ist der Subagent angewiesen, das zu **melden**
statt auf Sekundaerquellen auszuweichen.

### Phase 3 — Analyst 2: codex-CLI (gpt-5.6-sol / high)

Kann parallel zu Phase 2 starten. Fuer **Binary-Discovery**, **Update** und die **Startregeln**
gilt unveraendert `.claude/skills/super-review/references/codex-cli.md` — dort nachlesen und nicht
neu erfinden. Kurzfassung: `codex` liegt nicht zwingend im PATH (macOS:
`/opt/homebrew/bin/codex`; Windows: Pfad aus `~/.codex/config.toml`), vor dem Lauf aktualisieren,
ein fehlgeschlagenes Update ist **kein** Abbruch. `<codex>` steht unten fuer den gefundenen vollen
Pfad.

```bash
RUST_LOG=info <codex> exec \
  --json \
  -m gpt-5.6-sol \
  -c model_reasoning_effort="high" \
  --sandbox workspace-write \
  --skip-git-repo-check \
  "Erstelle ein Grundlagendokument fuer das GitLab-Work-Item \
https://git.office.brand-ad.de/guardops/issues/-/work_items/<N>. Lies die Datei \
.agents/skills/issue-grundlage/SKILL.md im aktuellen Repository und befolge ihren Abschnitt \
'Pflichtschritt F', den 'Analysekatalog' (A1-A9) und die 'Verbindliche Berichtsstruktur' \
VOLLSTAENDIG. Lies ausserdem .codex/skills/figma-desktop/SKILL.md vollstaendig und verwende \
ausschliesslich den lokalen MCP-Namespace mcp__figma_desktop__ fuer Figma. Die Anforderungen \
liest du ausschliesslich aus dem Snapshot \
tmp/issue-grundlage/issue<N>.md (Beschreibung, Tasks UND Kommentare) - lade nichts aus GitLab nach. \
Das Figma-Design analysierst du mit dem lokalen figma-desktop MCP. Seine Tools koennen deferred \
sein: Suche vor einer Nichtverfuegbarkeitsmeldung im Runtime-Tool-Katalog nach \
mcp__figma_desktop__. Verwende die aktive Desktop-Datei und diese Nodes: <FIGMA-URLS> \
(Quellen-fileKey <FILEKEY>, Node-IDs <NODE-IDS>). Sende an figma-desktop kein fileKey, sondern \
nodeId und die vom konkreten Tool unterstuetzten Parameter. Nutze weder den gehosteten \
mcp__codex_apps__figma_-Namespace noch Web-Browsing oder die Figma-REST-API. Pflichtschritt F ist \
nicht optional: eine Komponenten-Instanz zeigt nur ihren eingestellten Variant-State, darum \
get_metadata auf die 'Components'-Page aufrufen, jede Instanz dagegen matchen und JEDE Komponente \
in der Tabelle 4.2 disponieren; figma-desktop bietet \
list_file_components_for_code_connect nicht an. Vermerke den Erhebungsweg in Abschnitt 11. Eine 'Luecke im \
Figma' darfst du erst behaupten, nachdem dieser Lookup nichts ergeben hat. WICHTIG: Lies KEINEN \
Quellcode - weder backend/src noch frontend/src noch Tests, Build- oder Konfigurationsdateien; \
kein git diff, kein git log. Schreibe keinen Implementierungsplan. Aendere KEINE Datei ausser \
deiner Ergebnisdatei tmp/item<N>-gpt5.6-sol.md und nimm nichts in Git auf. Schreibe NICHT nach \
docs/ - das Verzeichnis ist allein dem finalen Dokument vorbehalten, das ein anderer Agent \
erstellt." \
  < /dev/null > tmp/issue-grundlage/codex<N>.log 2>&1
```

Mit `timeout: 900000`, `run_in_background: true` und — auf macOS/Windows —
`dangerouslyDisableSandbox: true` starten, sonst findet die Bash-Sandbox die codex-Binary nicht.

**`< /dev/null` ist Pflicht, nicht Kosmetik.** `codex exec` liest beim Start zusaetzlichen Input von
stdin („Reading additional input from stdin..."). Wird es aus einem Tool-Aufruf gestartet und ist
stdin ein offener Pipe oder Terminal-Handle, wartet es **unbegrenzt**: keine einzige Ausgabezeile,
CPU-Zeit bleibt bei ~0,06 s, und der Lauf endet erst im Timeout. Das ist ein echter Haenger und
sieht einem Modell-Stall zum Verwechseln aehnlich.

**Ausgabe in eine Datei umleiten, niemals nach `| tail -n`.** Eine Pipe in `tail` puffert die
gesamte Ausgabe bis EOF — die Logdatei bleibt waehrend des ganzen Laufs leer, der Fortschritt ist
also nicht beobachtbar. Fortschritt statt dessen mit `tail` bzw. `grep -c "mcp:"` **auf der
Logdatei** pruefen.

So unterscheidet man Arbeit von Haenger: Ein laufender codex erzeugt stetig neue Zeilen in der
Logdatei (bei Figma-Arbeit `mcp: figma-desktop/... started`). Mehrere Minuten ohne neue Zeile sind
bei nachdenklichen Phasen normal und **kein** Stall — eine **von Anfang an leere** Logdatei bei
~0 s CPU dagegen schon.

**Platzhalter im Prompt:** `<FIGMA-URLS>` sind die vollstaendigen `figma.com/design/...?node-id=…`
-URLs aus Phase 1 (alle, komma-getrennt); sie belegen die Quelldatei und erlauben den Abgleich mit
dem in Figma Desktop aktiven Dokument. `<FILEKEY>` bleibt als Quellenbeleg fuer das Ergebnis,
`<NODE-IDS>` liefert die Werte fuer die lokalen Tool-Aufrufe. Pflichtschritt F verwendet in Codex
die Components-Page der aktiven Datei und benoetigt dafuer keinen `fileKey`-Toolparameter.

**Die lokale Tool-Vorgabe nicht zu einer allgemeinen „installed Figma integration" abschwaechen.**
Der Codex-Lauf muss `.codex/skills/figma-desktop/SKILL.md` lesen, den exakten Namespace
`mcp__figma_desktop__*` entdecken und verwenden. Ein Ergebnis aus dem gehosteten Figma-Plug-in,
Web-Browsing oder der REST-API erfuellt Pflichtschritt F nicht.

Ist codex nach vollstaendiger Discovery nicht verfuegbar oder bricht ab: nicht abbrechen, sondern
`tmp/item<N>-gpt5.6-sol.md` mit „codex-Analyse nicht verfuegbar" plus Fehlerursache fuellen, den
Nutzer informieren und in Phase 5 mit der einen vorhandenen Analyse weiterarbeiten — das Enddokument
muss dann im Kopf ausweisen, dass es **nicht** doppelt belegt ist.

### Phase 4 — Barriere

Erst weiter, wenn **beide** Dateien existieren, nicht leer sind und die Abschnitte 0–11 der
Berichtsstruktur enthalten. Zusaetzlich pruefen, ob Abschnitt 4.2 (Varianten-Disposition) in beiden
Dateien vorhanden und gefuellt ist — fehlt sie, ist die betroffene Analyse laut Pflichtschritt F
unvollstaendig; das im Kopf des Enddokuments vermerken, weil es die Konsens-Zaehlung verzerrt.

### Phase 5 — Zusammenfuehren (Subagent)

Einen Subagenten mit `subagent_type: "issue-grundlage-merger"` starten (Opus 5 / High,
`.claude/agents/issue-grundlage-merger.md`). Er liest **nur** die zwei Analyse-Dokumente — er prueft
weder Issue noch Figma nach und fuehrt keine dritte Analyse durch.

> **Der Merger liefert Teil-Dateien, der Orchestrator fuegt sie zusammen.** Das Enddokument wird
> 60–200 KB gross und passt **nicht** in einen `Write`: der Lauf reisst die Ausgabegrenze und haengt
> dann in endlosen Textrunden. Belegt am 2026-08-11 zweimal — der erste Lauf brach nach Abschnitt
> 4.3.8 ab und produzierte 30 Minuten Turns ohne einen einzigen Tool-Aufruf.
>
> `Edit` ist **kein** Ausweg: es ist in Subagenten dieser Umgebung gesperrt („Edit is disabled for
> this session, in subagents as well as here"), obwohl es in der Tool-Liste steht — es in die
> `tools:`-Zeile aufzunehmen aendert daran nichts. Der Merger schreibt daher mehrere Dateien unter
> `tmp/` (`…teil1.md` = 0–4, `…teil2a.md` = 5–6, `…teil2b.md` = 7–9, `…teil2c.md` = 10–12) und nennt
> sie in seiner Abschlussmeldung. Der Orchestrator haengt sie in dieser Reihenfolge zusammen:
>
> ```bash
> cat tmp/item<N>-final.teil1.md tmp/item<N>-final.teil2a.md tmp/item<N>-final.teil2b.md tmp/item<N>-final.teil2c.md > docs/item<N>-final.md
> ```
>
> Bricht ein Lauf trotzdem mittendrin ab: **nicht von vorn starten.** Vorhandene Teile sichern und
> einen Fortsetzungslauf beauftragen, der sie liest und nur die fehlenden Abschnitte als neue
> Teil-Datei schreibt. Ein Neustart wuerde die Klaerungsliste **neu durchnummerieren**, womit alle
> `U`-Verweise im schon geschriebenen Teil falsch werden — die Nummerierung aus Abschnitt 0b ist die
> Vorgabe.

Auftrag:

1. **Gemeinsamkeiten zusammenfuehren:** Aussagen, die beide Dokumente inhaltlich gleich treffen,
   werden **ein** Eintrag, ueber die **AK-ID** verknuepft (bei abweichender Formulierung ueber den
   Wortlaut aus dem Issue). Jeder Eintrag ist mit `[beide]` markiert.
2. **Einseitige Punkte uebernehmen, nicht wegkuerzen:** was nur ein Dokument enthaelt, kommt mit
   `[nur Opus 5]` bzw. `[nur gpt-5.6-sol]` ins Enddokument. Das gilt fuer AK, Figma-Nodes,
   Varianten-Zeilen, Detailvorgaben, Scope-Kandidaten und offene Punkte gleichermassen.
3. **Widersprueche zwischen den Dokumenten** in einen eigenen Abschnitt, mit beiden Aussagen im
   Wortlaut, den jeweiligen Belegen (Node-ID / Issue-Stelle) und der Auswirkung. Jeder solche
   Widerspruch wird **zusaetzlich** als Klaerungspunkt `U…` gefuehrt — **der Nutzer muss ihn
   entscheiden**; der Merger entscheidet nicht selbst und mittelt nicht.
4. **Klaerungsliste vereinen und durchnummerieren** (`U1`, `U2`, …), Duplikate zusammenfuehren, die
   Herkunft je Punkt nennen. Diese Liste ist das Arbeitsergebnis fuer den Nutzer und steht
   **zusaetzlich** ganz oben im Dokument als Kurzliste.
5. **Vollstaendigkeit:** jede AK-Zeile, jede Node-ID und jeder offene Punkt aus beiden Dokumenten
   muss im Enddokument wiederzufinden sein.

Enddokument `docs/item<N>-final.md` mit dieser Gliederung:

```markdown
# Grundlagendokument (final) Work Item <N> — „<Titel>"
> Status: ENTWURF — erst nach Klaerung aller Punkte in Abschnitt 10 Grundlage fuer den Implementierungsplan.

## 0. Kopf   (Quellen, Analysten + ob doppelt belegt, fileKey, Nodes, Datum, Zahlen)
## 0b. Klaerungsliste — Kurzform   (U1…Un als Checkliste, je eine Zeile)
## 1. User Story und Ziel
## 2. Anforderungen und Akzeptanzkriterien          (je Zeile Herkunftsmarker)
## 3. Tasks
## 4. Figma-Inventar (4.1 Frames · 4.2 Varianten-Disposition · 4.3 Design-Specs)
## 5. Zuordnung AK ↔ Figma                          (Status je AK; bei Uneinigkeit beide Status)
## 6. Detailspezifikation je AK
## 7. Im Figma vorhanden, im Issue nicht gefordert
## 8. Im Issue gefordert, im Figma nicht auffindbar
## 9. Widersprueche
### 9.1 Issue ↔ Figma / Issue ↔ Issue / Figma ↔ Figma   (aus beiden Analysen)
### 9.2 Analyse ↔ Analyse — Opus 5 gegen gpt-5.6-sol    (vom Nutzer zu entscheiden)
## 10. Offene Punkte — Klaerung durch den Nutzer     (U1…Un, ausformuliert)
## 11. Vollstaendigkeitspruefung und Annahmen
## 12. Uebersichtstabelle
| AK-ID | Kurztext | Node-ID | Status | Opus 5 | gpt-5.6-sol | offen (U) |
```

Bei uneinheitlichem Status **beide Werte nennen** (z. B. `belegt (Opus5) / teilweise belegt
(gpt5.6-sol)`) und **nicht** mitteln.

### Phase 6 — Bericht an den Nutzer

Kurz zusammenfassen, ohne das Enddokument abzuschreiben: Anzahl AK, davon `belegt` /
`teilweise belegt` / `im Figma nicht gefunden`, Anzahl Widersprueche (getrennt nach inhaltlich und
Analyse-gegen-Analyse), **die Klaerungsliste `U1…Un` als kompakte Aufzaehlung** — das ist der Punkt,
an dem der Nutzer arbeitet — und die Dateipfade: `docs/item<N>-final.md` als Ergebnis, die beiden
`tmp/item<N>-*.md` als Belege zum Nachschlagen.

Dann **stoppen**. Kein Implementierungsplan, keine Codeaenderung, kein Commit. Erst wenn der Nutzer
die offenen Punkte beantwortet hat, werden die Antworten in `docs/item<N>-final.md` eingearbeitet
(Status `ENTWURF` im Kopf entfernen) — und erst danach entsteht daraus der Plan.

## Zusammenspiel der Phasen

```
Phase 0  <N> → Work Item + Tasks (GraphQL-Hierarchie) + alle Kommentare
         → Snapshot tmp/issue-grundlage/issue<N>.md; alte Ergebnisdateien bereinigen
Phase 1  Figma-Link aus Snapshot; fehlt er → NACHFRAGEN (Screenshots gelten nicht)
Phase 2  Opus 5 / High        ─┐  gleicher Snapshot, gleicher Katalog,
Phase 3  codex gpt-5.6-sol/high ┘  Pflichtschritt F verpflichtend
Phase 4  Barriere: beide Dateien da, Abschnitte 0–11 inkl. 4.2 vorhanden
Phase 5  Merger-Subagent: tmp/item<N>-opus5.md + tmp/item<N>-gpt5.6-sol.md
         → docs/item<N>-final.md  (einziges Artefakt in docs/)
         (Gemeinsamkeiten · einseitige Punkte · Widersprueche → Klaerungsliste)
Phase 6  Kurzbericht + Klaerungsliste an den Nutzer — ENDE

Kein Quellcode. Kein Plan. In docs/ landet nur item<N>-final.md; die beiden
Analysen und der Snapshot bleiben unter tmp/ und werden nicht eingecheckt.
```
