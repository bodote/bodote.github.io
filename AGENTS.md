# AGENTS.md

Leitfaden für KI-Agenten in diesem Repository.

## Was dieses Projekt ist

Persönlicher Software-Blog („Bodos Software Blog", `bodote.github.io`), gebaut mit
**Jekyll 3.10** über das `github-pages`-Gem und dem **Minimal Mistakes**
Remote-Theme. Deployment erfolgt automatisch durch GitHub Pages beim Push auf
`master` — es gibt **keine** eigene CI-Pipeline (`.github/workflows` existiert
nicht). Ein Push auf `master` ist damit direkt eine Veröffentlichung.

Es gibt **keinen Anwendungscode**: die Arbeit besteht aus Markdown/HTML-Inhalten,
YAML-Konfiguration und SCSS.

Inhaltssprache: **Deutsch** (einzelne Posts sind englisch). Themenschwerpunkt: TDD,
Test-First, Testautomatisierung, Softwarearchitektur, Angular/React, Spring Boot.

## Toolchain

Zwei Dinge müssen stimmen, sonst bricht der Build:

**1. Ruby 3.3** — nicht 3.4+/4.0. Das `github-pages`-Gem bringt Jekyll 3.x und
Liquid 4.0.x mit; dort fehlen unter 3.4 Stdlib-Gems (`csv`, `base64`) und Liquid
4.0.3 ruft noch `String#tainted?` auf. Auf diesem Rechner installiert als
**Ruby 3.3.12 über rbenv**, im Projekt gepinnt via `.ruby-version`. Das
macOS-System-Ruby (2.6.10 unter `/usr/bin/ruby`) wird nicht benutzt.

> Hinweis: `localserve-only-published.sh` und `serve-unpublished.sh` setzen
> `PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"` für eine Homebrew-Installation.
> Dieser Pfad existiert hier **nicht** — das Prepend bleibt wirkungslos und der
> rbenv-Shim greift, sodass trotzdem 3.3.12 läuft. Wer die Skripte anfasst:
> beide Wege führen aktuell zum Ziel, aber nur rbenv ist real installiert.

**2. Eine UTF-8-Locale.** `jekyll-sass-converter` 1.5.2 liest `.scss` sonst als
US-ASCII und scheitert an den UTF-8-Partials des Themes:

```
Conversion error: Jekyll::Converters::Scss ...
Invalid US-ASCII character "\xE2" on line 54
```

Deshalb `export LANG=en_US.UTF-8` (bzw. `LC_ALL`) — die Serve-Skripte tun das
selbst. Bei manuellem `jekyll build` in einer Shell ohne Locale tritt der Fehler
sofort auf.

**Bundler 2.5.7**; `bundle` wählt diese Version wegen `BUNDLED WITH` im Lockfile
selbst aus, auch wenn eine neuere installiert ist. Gems liegen lokal in
`vendor/bundle` (`.bundle/config`) — gitignored.

## Lokal bauen und servieren

```bash
bundle install
bundle exec jekyll build         # Verifikation (UTF-8-Locale nötig, s.o.)
./localserve-only-published.sh   # jekyll serve             -> localhost:4000
./serve-unpublished.sh           # 0.0.0.0, --watch, --unpublished (zeigt Drafts)
```

- `./serve-unpublished.sh` ist der Weg, Posts mit `published: false` vorab zu prüfen.
- Änderungen an `_config.yml` werden **nicht** automatisch neu geladen — Server neu starten.
- Es gibt keine Tests und keinen Linter. Ein fehlerfreier Build plus Sichtprüfung
  der betroffenen Seite ist die Baseline-Kontrolle vor dem Commit.
- `update.sh` ist nur eine Notiz-Datei mit auskommentierten Kommandos, kein Skript.

## Verzeichnisstruktur

| Pfad | Zweck |
|---|---|
| `_config.yml` | Site-Einstellungen, Theme, Plugins, Autor/Footer, `defaults`. Nicht hot-reloaded. |
| `_posts/` | Blogposts, `YYYY-MM-DD-Titel.md` |
| `_pages/` | Statische Seiten + Archiv-Layouts (über `include:` eingebunden) |
| `_data/navigation.yml` | Hauptnavigation |
| `_includes/` | Eigene Overrides (nur `mastodon_feed.html`) |
| `assets/` | `images/`, `css/main.scss`, `powerpoints/` (Vortragsfolien, PDF/PPTX) |
| `extra-html/` | Standalone-HTML außerhalb des Jekyll-Layouts (Slides) |
| `index.html` | Startseite, nur Front Matter (`layout: home`) |
| `.ruby-version` | Pinnt Ruby 3.3.12 für rbenv |
| `doc/`, `*.odt`, `odt_convert.sh` | Pandoc-Export von Posts nach ODT |
| `_site/`, `vendor/`, `.bundle` | Build-Output / lokale Gems / gitignored |

Das Theme liegt **nicht** im Repo (`remote_theme: mmistakes/minimal-mistakes`).
Layouts und Theme-Partials nicht suchen — zum Überschreiben muss eine Datei mit
gleichem Namen in `_layouts/` bzw. `_includes/` neu angelegt werden.

## Neuen Post anlegen

Datei `_posts/YYYY-MM-DD-Kurz-Titel.md`:

```yaml
---
title: "Titel in Anführungszeichen"
date: 2025-07-10
published: true   # false hält den Post aus dem Build heraus
visible: true
categories:
  - blog          # bestehende Werte: blog / Blog / Vorträge
tags:
  - TDD
toc: true         # Inhaltsverzeichnis
classes: wide     # breites Layout, in fast allen Posts gesetzt
---
```

- `defaults` in `_config.yml` setzt `layout: single`, `author_profile`, `read_time`,
  `comments`, `share`, `related` bereits für alle Posts — nicht pro Post wiederholen,
  außer zum Überschreiben.
- `visible:` ist ein eigenes, vom Theme **nicht** ausgewertetes Feld — beim Kopieren
  mitführen, aber keine Wirkung erwarten.
- Permalinks folgen `/:categories/:title/`; eine Änderung von Titel oder Kategorie
  eines veröffentlichten Posts **bricht die bestehende URL**.
- Kategorie-/Tag-Archive (`/categories/`, `/tags/`) existieren als Seiten, sind aber
  in `_data/navigation.yml` bewusst auskommentiert.
- Asset-Links absolut vom Site-Root schreiben: `/assets/images/foo.png`.

## Dependencies updaten

Der Kern der Toolchain ist **nicht frei wählbar**: `github-pages` pinnt Jekyll,
Liquid, Kramdown, Rouge und `jekyll-sass-converter` auf exakte Versionen, weil
GitHub Pages serverseitig mit genau diesem Set baut.

- `bundle update` ist der richtige Befehl — es löst innerhalb dieser Pins auf.
- `bundle outdated` listet u.a. `jekyll 3.10.0 -> 4.4.1`, `liquid 4.0.4 -> 5.13.0`,
  `rouge 3.30.0 -> 5.1.0`. Diese **nicht** erzwingen: lokal würde dann etwas anderes
  gebaut als auf GitHub Pages, und der Fehler fällt erst nach dem Push auf.
- Ein echter Sprung geht nur über eine neuere `github-pages`-Version (aktuell 232 =
  neueste) oder durch Umstellung auf eine eigene Build-Action. Bewusste Entscheidung
  des Projekts: **GitHub-Pages-kompatibel bleiben**, also keine eigene Action.
- Beim serverseitigen Build ignoriert GitHub Pages das `Gemfile.lock` — es betrifft
  nur die lokale Umgebung.
- Neue Plugins müssen im von GitHub Pages unterstützten Set enthalten sein. Ein
  beliebiges Gem kann den gehosteten Build brechen, auch wenn es lokal läuft.
- Updates sind per Renovate automatisiert (`renovate.json`, `config:base`).

Stand 2026-09-11 (`bundle update`): u.a. activesupport 7.1.3.4 -> 8.1.3.1,
nokogiri 1.16.7 -> 1.19.4, faraday 2.10.1 -> 2.14.3, minitest 5.24.1 -> 6.0.6.
Build und Serve verifiziert.

## Konventionen & Fallstricke

- **Sprache der bearbeiteten Datei übernehmen** — Inhalte sind überwiegend deutsch,
  Kommentare in Config-Dateien oft ebenfalls.
- Nicht `_site/` bearbeiten — wird bei jedem Build überschrieben.
- Jekyll rendert jedes `.md` im Root als Seite. `AGENTS.md`, `README.md` und die
  Shell-Skripte stehen darum in `exclude:` in `_config.yml` — sonst landet die
  Agenten-Doku unter `/AGENTS/` auf dem öffentlichen Blog. Neue Root-Dokumente
  dort ebenfalls eintragen.
- Große Binärdateien (PDFs bis ~24 MB) liegen in `assets/powerpoints/` im Repo;
  keine weiteren ohne Rückfrage hinzufügen.
- `_config.yml` enthält `google_site_verification` und die Autor-/Kontaktdaten —
  beim Umbau nicht verlieren.
- `.DS_Store` ist inzwischen in `.gitignore` — nicht committen.
- Commit-Nachrichten in der History sind durchweg `.` — keine Konvention vorhanden;
  aussagekräftige Messages sind eine Verbesserung, keine Abweichung.
