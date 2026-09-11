# AGENTS.md

## Was dieses Projekt ist

Persönlicher Software-Blog (`bodote.github.io`), gebaut mit **Jekyll 3.10** über das
`github-pages` Gem und dem **Minimal Mistakes** Remote-Theme. Deployment erfolgt
automatisch durch GitHub Pages beim Push auf `master` — es gibt **keine** eigene
CI-Pipeline (`.github/` existiert nicht). Ein Push auf `master` ist damit direkt
eine Veröffentlichung.

Inhaltssprache: **Deutsch** (einzelne Posts sind englisch). Themenschwerpunkt: TDD,
Test-First, Testautomatisierung, Softwarearchitektur, Angular/React, Spring Boot.

## Toolchain

- **Ruby 3.3.12** über `rbenv`, im Projekt gepinnt via `.ruby-version`.
  Das macOS-System-Ruby (2.6.10 unter `/usr/bin/ruby`) wird **nicht** benutzt.
- `rbenv` ist per Homebrew installiert und in `~/.zshrc` initialisiert
  (`eval "$(rbenv init - zsh)"`). In einer frischen Shell greift `.ruby-version`
  automatisch — `ruby -v` muss 3.3.12 zeigen.
- **Bundler 2.5.7**; `bundle` wählt diese Version wegen `BUNDLED WITH` im
  Lockfile selbst aus, auch wenn eine neuere Bundler-Version installiert ist.
  Kein `bundle _2.5.7_`-Präfix nötig.
- Gems liegen lokal in `vendor/bundle` (`bundle config set --local path vendor/bundle`,
  hinterlegt in `.bundle/config`) — beides gitignored.
- Nicht auf Ruby 3.4 wechseln: dort sind `csv` und `base64` nicht mehr Teil der
  Stdlib, womit Jekyll 3.10 bzw. Abhängigkeiten von `github-pages` brechen.

## Lokal bauen und servieren

```bash
bundle install            # einmalig
bundle exec jekyll build  # Verifikation, dass Liquid/Front Matter fehlerfrei sind
bundle exec jekyll serve  # oder: ./localserver.sh
./serve.sh                # bindet 0.0.0.0, --watch --unpublished (zeigt Drafts)
```

Der Build ist unter Ruby 3.3.12 verifiziert (17 Post-Seiten, exit 0). Die Meldung
`To use retry middleware with Faraday v2.0+, install faraday-retry gem` ist
harmlos und kommt aus `jekyll-github-metadata`.

- Änderungen an `_config.yml` werden **nicht** automatisch neu geladen — Server neu starten.
- `./serve.sh` ist der richtige Weg, um Posts mit `published: false` vorab zu prüfen.
- `jekyll build` ist die einzige verfügbare Verifikation; es gibt keine Tests und
  keinen Linter.
- `update.sh` ist nur eine Notiz-Datei mit auskommentierten `bundle update` /
  `bundle install`-Kommandos, kein ausführbares Update-Skript.

## Verzeichnisstruktur

| Pfad | Zweck |
|---|---|
| `_posts/` | Blogposts, `YYYY-MM-DD-Titel.md` |
| `_pages/` | Statische Seiten + Archiv-Layouts (über `include:` in `_config.yml` eingebunden) |
| `_data/navigation.yml` | Hauptnavigation |
| `_includes/` | Eigene Snippets (nur `mastodon_feed.html`) |
| `assets/images/`, `assets/powerpoints/` | Bilder, Vortragsfolien (PDF/PPTX) |
| `assets/css/main.scss` | Einziger Style-Einstiegspunkt, importiert Theme-Partials |
| `index.html` | Startseite, nur Front Matter (`layout: home`) |
| `doc/README.md` | Übrig gebliebenes Starter-Template-README |
| `.ruby-version` | Pinnt Ruby 3.3.12 für rbenv |
| `_site/`, `vendor/`, `.bundle` | Build-Output / lokale Gems / gitignored |

Das Theme liegt **nicht** im Repo (`remote_theme: mmistakes/minimal-mistakes`).
Layouts oder Theme-Partials nicht suchen — zum Überschreiben muss eine Datei mit
gleichem Namen in `_layouts/` bzw. `_includes/` neu angelegt werden.

## Neuen Post anlegen

Datei `_posts/YYYY-MM-DD-Kurz-Titel.md` mit diesem Front Matter (so sieht es in
allen bestehenden Posts aus):

```yaml
---
title: "Titel in Anführungszeichen"
date: 2025-07-10
published: true
visible: true
categories:
  - blog          # bestehende Werte: blog / Blog / Vorträge
tags:
  - TDD
toc: true         # Inhaltsverzeichnis
classes: wide     # breites Layout, in fast allen Posts gesetzt
---
```

- `published: false` hält einen Post aus dem Build heraus (aktuell bei zwei Posts).
- `visible:` ist ein eigenes, vom Theme nicht ausgewertetes Feld — beim Kopieren
  mitführen, aber keine Wirkung erwarten.
- Permalinks folgen `/:categories/:title/`; eine Änderung von Titel oder Kategorie
  eines veröffentlichten Posts **bricht die bestehende URL**.
- Kategorie-/Tag-Archive (`/categories/`, `/tags/`) existieren als Seiten, sind aber
  in `_data/navigation.yml` bewusst auskommentiert.
- Asset-Links absolut vom Site-Root schreiben: `/assets/images/foo.png`.

## Konventionen

- Deutsche Texte; VS Code nutzt cSpell mit `"cSpell.language": "en,de"`.
- Commit-Nachrichten in der History sind durchweg `.` — keine Konvention vorhanden;
  aussagekräftige Messages sind eine Verbesserung, keine Abweichung.
- Dependency-Updates laufen über Renovate (`renovate.json`, `config:base`).

## Dependencies updaten

Der Kern der Toolchain ist **nicht frei wählbar**: das `github-pages`-Gem pinnt
Jekyll, Liquid, Kramdown, Rouge und `jekyll-sass-converter` auf exakte Versionen,
weil GitHub Pages serverseitig mit genau diesem Set baut.

- `bundle update` ist der richtige Befehl — es löst innerhalb dieser Pins auf und
  aktualisiert nur die freien transitiven Gems.
- `bundle outdated` listet u.a. `jekyll 3.10.0 -> 4.4.1`, `liquid 4.0.4 -> 5.13.0`,
  `rouge 3.30.0 -> 5.1.0`. Diese **nicht** erzwingen: lokal würde dann etwas anderes
  gebaut als auf GitHub Pages, und der Fehler fällt erst nach dem Push auf.
- Ein echter Sprung dieser Gems geht nur über eine neuere `github-pages`-Version
  (aktuell 232 = neueste) — oder durch Umstellung auf eine eigene GitHub-Action,
  die die Site selbst baut und `_site/` deployt.
- Nach jedem Update: `bundle exec jekyll build` muss durchlaufen, und `_site/` soll
  ~33 HTML-Seiten inkl. 17 Posts, `feed.xml`, `sitemap.xml` und ein ~95 KB großes
  `assets/css/main.css` enthalten.

Stand 2026-09-11 durchgeführt (`bundle update`): u.a. activesupport 7.1.3.4 -> 8.1.3.1,
nokogiri 1.16.7 -> 1.19.4, faraday 2.10.1 -> 2.14.3, minitest 5.24.1 -> 6.0.6,
rexml 3.3.4 -> 3.4.4. Build und `jekyll serve` verifiziert.

- `odt_convert.sh` konvertiert einen fest verdrahteten Post per pandoc nach ODT
  (`custom-reference.odt` als Referenz-Dokument) — Ad-hoc-Skript, Pfad vor Nutzung anpassen.

## Vorsicht

- Nicht `_site/` bearbeiten — wird bei jedem Build überschrieben.
- Große Binärdateien (PDFs bis ~24 MB) liegen in `assets/powerpoints/` im Repo;
  keine weiteren ohne Rückfrage hinzufügen.
- `_config.yml` enthält `google_site_verification` und die Autor-/Kontaktdaten —
  beim Umbau nicht verlieren.
- Jekyll rendert jedes `.md` im Root als Seite. `AGENTS.md`, `README.md` und die
  Shell-Skripte stehen darum in `exclude:` in `_config.yml` — sonst landet die
  Agenten-Doku unter `/AGENTS/` auf dem öffentlichen Blog. Neue Root-Dokumente
  dort ebenfalls eintragen.
