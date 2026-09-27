#!/usr/bin/env python3
"""Erzeugt die Folien-Grafiken fuer Issue-Grundlage-Claude.md als SVG.

Aufruf: python3 gen_svgs.py   (schreibt *.svg nach assets/images/issue-grundlage/)
"""
import math
import os

# Gemeinsamer Ort fuer Slide Deck und Blogpost; doc/powerpoints ist in _config.yml von Jekyll ausgenommen
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "assets", "images", "issue-grundlage")

N, NL = "#1f4e79", "#e8eef5"
R, RL = "#b03a2e", "#f8e1de"
G, GL = "#2e7d32", "#e3f1e4"
A, AL = "#d68910", "#fdf0d9"
P, PL = "#6c3483", "#efe3f5"
GR, GRL = "#6b7280", "#f1f2f4"
DARK = "#1f2937"
GITLAB = "#e24329"
COLORS = {"N": N, "R": R, "G": G, "A": A, "P": P, "GR": GR}


def svg(name, body, w=1160, h=540):
    markers = "".join(
        f'<marker id="a{k}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
        f'markerHeight="5" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="{c}"/></marker>'
        for k, c in COLORS.items()
    )
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
         f'font-family="Arial, sans-serif"><defs>{markers}</defs>{"".join(body)}</svg>\n')
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(s)


def T(x, y, s, fs=24, fill=N, anchor="middle", bold=False, mono=False, italic=False, vc=False):
    lines = s.split("\n")
    lh = fs * 1.2
    if vc:
        y = y - (len(lines) - 1) * lh / 2 + fs * 0.35
    attrs = f'font-size="{fs}" fill="{fill}" text-anchor="{anchor}"'
    if bold:
        attrs += ' font-weight="bold"'
    if italic:
        attrs += ' font-style="italic"'
    if mono:
        attrs += ' font-family="Courier New, monospace"'
    out = []
    for i, ln in enumerate(lines):
        ln = ln.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        out.append(f'<text x="{x:.1f}" y="{y + i * lh:.1f}" {attrs}>{ln}</text>')
    return "".join(out)


def Rc(x, y, w, h, fill="none", stroke="none", rx=14, sw=3, dash=False, op=1):
    d = ' stroke-dasharray="10,8"' if dash else ""
    o = f' fill-opacity="{op}"' if op != 1 else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')


def C(cx, cy, r, fill="none", stroke="none", sw=3, op=1, dash=False):
    o = f' fill-opacity="{op}"' if op != 1 else ""
    d = ' stroke-dasharray="10,8"' if dash else ""
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"{o}{d}/>')


def L(x1, y1, x2, y2, color=N, sw=4, dash=False, cap="round"):
    d = ' stroke-dasharray="10,8"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="{cap}"{d}/>')


def ck(color):
    return next(k for k, c in COLORS.items() if c == color)


def Ar(x1, y1, x2, y2, color=N, sw=5, dash=False):
    d = ' stroke-dasharray="10,8"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
            f'stroke-width="{sw}"{d} marker-end="url(#a{ck(color)})"/>')


def Pa(d, color=N, sw=5, fill="none", dash=False, arrow=True):
    da = ' stroke-dasharray="10,8"' if dash else ""
    m = f' marker-end="url(#a{ck(color)})"' if arrow else ""
    return f'<path d="{d}" stroke="{color}" stroke-width="{sw}" fill="{fill}"{da}{m}/>'


def box(x, y, w, h, label, fill=NL, stroke=N, fc=N, fs=24, bold=True, rx=14, mono=False):
    return Rc(x, y, w, h, fill, stroke, rx) + T(x + w / 2, y + h / 2, label, fs, fc, bold=bold, vc=True, mono=mono)


def pill(x, y, w, h, label, fill=RL, fc=R, fs=20, mono=False):
    return Rc(x, y, w, h, fill, "none", h / 2) + T(x + w / 2, y + h / 2, label, fs, fc, bold=True, vc=True, mono=mono)


# ---------- Icons ----------

def robot(cx, cy, s=1.0, color=N, eye="white"):
    return "".join([
        L(cx, cy - 38 * s, cx, cy - 52 * s, color, 4 * s),
        C(cx, cy - 56 * s, 7 * s, color),
        Rc(cx - 42 * s, cy - 38 * s, 84 * s, 66 * s, color, "none", 16 * s),
        C(cx - 17 * s, cy - 10 * s, 9 * s, eye),
        C(cx + 17 * s, cy - 10 * s, 9 * s, eye),
        Rc(cx - 18 * s, cy + 10 * s, 36 * s, 6 * s, eye, "none", 3 * s),
    ])


def person(cx, cy, s=1.0, color=N):
    d = (f"M{cx - 32 * s:.1f},{cy + 40 * s:.1f} L{cx - 32 * s:.1f},{cy + 18 * s:.1f} "
         f"Q{cx - 32 * s:.1f},{cy - 4 * s:.1f} {cx:.1f},{cy - 4 * s:.1f} "
         f"Q{cx + 32 * s:.1f},{cy - 4 * s:.1f} {cx + 32 * s:.1f},{cy + 18 * s:.1f} "
         f"L{cx + 32 * s:.1f},{cy + 40 * s:.1f} Z")
    return C(cx, cy - 28 * s, 18 * s, color) + f'<path d="{d}" fill="{color}"/>'


def doc(x, y, w, h, stroke=N, fill="white", lines=True, sw=4):
    f = min(w, h) * 0.22
    out = [f'<path d="M{x},{y} L{x + w - f},{y} L{x + w},{y + f} L{x + w},{y + h} L{x},{y + h} Z" '
           f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>',
           f'<path d="M{x + w - f},{y} L{x + w - f},{y + f} L{x + w},{y + f}" fill="none" '
           f'stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>']
    if lines:
        ly = y + f + 16
        while ly < y + h - 14:
            out.append(L(x + 14, ly, x + w - 14, ly, stroke, 3))
            ly += 18
    return "".join(out)


def figma(cx, cy, s=1.0):
    u = 20 * s
    x0, x1 = cx - u, cx
    y0, y1, y2 = cy - 1.5 * u, cy - 0.5 * u, cy + 0.5 * u
    h = u / 2

    def left(y, c):
        return (f'<path d="M{x0 + u},{y} L{x0 + h},{y} A{h},{h} 0 0 0 {x0 + h},{y + u} '
                f'L{x0 + u},{y + u} Z" fill="{c}"/>')
    return "".join([
        left(y0, "#F24E1E"),
        f'<path d="M{x1},{y0} L{x1 + h},{y0} A{h},{h} 0 0 1 {x1 + h},{y0 + u} L{x1},{y0 + u} Z" fill="#FF7262"/>',
        left(y1, "#A259FF"),
        C(cx + h, y1 + h, h, "#1ABCFE"),
        f'<path d="M{x0 + u},{y2} L{x0 + h},{y2} A{h},{h} 0 0 0 {x0 + h},{y2 + u} '
        f'A{h},{h} 0 0 0 {x0 + u},{y2 + h} Z" fill="#0ACF83"/>',
    ])


def xmark(cx, cy, s=20, color=R):
    return L(cx - s, cy - s, cx + s, cy + s, color, s * 0.4) + L(cx + s, cy - s, cx - s, cy + s, color, s * 0.4)


def check(cx, cy, s=20, color=G):
    return (f'<polyline points="{cx - s},{cy} {cx - 0.3 * s},{cy + 0.7 * s} {cx + s},{cy - 0.7 * s}" '
            f'fill="none" stroke="{color}" stroke-width="{s * 0.4}" stroke-linecap="round" stroke-linejoin="round"/>')


def badge_check(cx, cy, r=26):
    return C(cx, cy, r, G) + check(cx, cy, r * 0.5, "white")


def nosign(cx, cy, r):
    k = r * 0.7
    return C(cx, cy, r, "none", R, r * 0.13) + L(cx - k, cy - k, cx + k, cy + k, R, r * 0.13)


def imageicon(x, y, w, h):
    return "".join([
        Rc(x, y, w, h, "white", N, 12, 4),
        C(x + w * 0.72, y + h * 0.3, h * 0.11, A),
        f'<polygon points="{x + 10},{y + h - 10} {x + w * 0.35},{y + h * 0.4} {x + w * 0.55},{y + h * 0.7} '
        f'{x + w * 0.7},{y + h * 0.55} {x + w - 10},{y + h - 10}" fill="{NL}" stroke="{N}" stroke-width="3"/>',
    ])


def clock(cx, cy, r, color=A):
    return (C(cx, cy, r, "white", color, r * 0.12) + L(cx, cy, cx, cy - r * 0.6, color, r * 0.1)
            + L(cx, cy, cx + r * 0.45, cy + r * 0.2, color, r * 0.1))


def lightning(cx, cy, s=1.0, color=P):
    pts = [(10, -40), (-20, 5), (0, 5), (-10, 40), (22, -8), (2, -8)]
    p = " ".join(f"{cx + a * s:.1f},{cy + b * s:.1f}" for a, b in pts)
    return f'<polygon points="{p}" fill="{color}"/>'


def shield(cx, cy, s=1.0, color=G):
    d = (f"M{cx},{cy - 90 * s} L{cx + 70 * s},{cy - 60 * s} L{cx + 70 * s},{cy + 10 * s} "
         f"Q{cx + 70 * s},{cy + 70 * s} {cx},{cy + 100 * s} Q{cx - 70 * s},{cy + 70 * s} {cx - 70 * s},{cy + 10 * s} "
         f"L{cx - 70 * s},{cy - 60 * s} Z")
    return f'<path d="{d}" fill="{color}"/>' + check(cx, cy + 5 * s, 32 * s, "white")


def linkicon(cx, cy, color=N):
    return (f'<g transform="rotate(-35 {cx} {cy})">'
            f'<rect x="{cx - 20}" y="{cy - 8}" width="24" height="16" rx="8" fill="none" stroke="{color}" stroke-width="4"/>'
            f'<rect x="{cx - 4}" y="{cy - 8}" width="24" height="16" rx="8" fill="none" stroke="{color}" stroke-width="4"/></g>')


def cloud(cx, cy, fill=NL):
    return (C(cx - 50, cy + 10, 42, fill) + C(cx, cy - 18, 55, fill) + C(cx + 50, cy + 10, 42, fill)
            + Rc(cx - 92, cy + 5, 184, 47, fill, "none", 23))


def monitor(cx, cy, label):
    return (Rc(cx - 90, cy - 62, 180, 112, "white", N, 10, 4) + Rc(cx - 15, cy + 50, 30, 18, N, "none", 0)
            + Rc(cx - 55, cy + 66, 110, 10, N, "none", 5) + T(cx, cy - 6, label, 20, N, bold=True, vc=True))


def chevron(x, y, w, h, fill, label, fs=24, first=False):
    n = 30
    pts = [(x, y), (x + w - n, y), (x + w, y + h / 2), (x + w - n, y + h), (x, y + h)]
    if not first:
        pts.append((x + n, y + h / 2))
    p = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    return f'<polygon points="{p}" fill="{fill}"/>' + T(x + w / 2 + (0 if first else 12), y + h / 2, label, fs, "white", bold=True, vc=True)


def checklist(x, y, items, fs=22, step=48, color=G):
    out = []
    for i, it in enumerate(items):
        yy = y + i * step
        out.append(Rc(x, yy - 14, 26, 26, "white", color, 5, 3))
        out.append(T(x + 40, yy + 8, it, fs, N, anchor="start", bold=True))
    return "".join(out)


# ---------- Folien ----------

def s01_title():
    b = [doc(215, 60, 110, 140, N, "white"), T(270, 235, "Issue", 22, N, bold=True),
         figma(395, 130, 2.0), T(395, 235, "Figma", 22, N, bold=True),
         Ar(460, 130, 565, 130, N),
         C(650, 130, 75, R), T(650, 130, "Issue-\nGrundlage", 22, "white", bold=True, vc=True),
         Ar(735, 130, 800, 130, N),
         doc(810, 45, 130, 170, G, GL), badge_check(925, 200, 30), T(875, 262, "Grundlage", 22, G, bold=True)]
    svg("01-titel.svg", b, h=290)


def s01b_teil1():
    b = [person(330, 290, 2.2), C(430, 185, 12, AL, A, 3), C(470, 145, 20, AL, A, 3),
         f'<ellipse cx="740" cy="115" rx="250" ry="90" fill="{AL}" stroke="{A}" stroke-width="4"/>',
         T(740, 115, "Meine persönliche Sicht", 34, A, bold=True, vc=True),
         T(740, 280, "keine Vorgabe – niemand muss sie teilen", 26, N, bold=True),
         T(740, 325, "eine Einladung zur Diskussion", 24, GR, italic=True)]
    svg("01b-teil1.svg", b, h=390)


def s03c_teil2():
    b = [Rc(290, 70, 22, 300, DARK, "none", 4),
         f'<polygon points="140,85 420,85 460,125 420,165 140,165" fill="{G}"/>',
         T(290, 125, "Empfehlung", 26, "white", bold=True, vc=True),
         f'<polygon points="140,190 420,190 460,230 420,270 140,270" fill="{N}"/>',
         T(290, 230, "für unser Team", 24, "white", bold=True, vc=True),
         Rc(250, 360, 100, 20, DARK, "none", 6),
         T(780, 190, "Mögliche Wege dorthin", 36, G, bold=True),
         T(780, 245, "Handlungsempfehlungen für unsere Arbeit", 24, N, bold=True),
         T(780, 290, "aus der Praxis im Projekt", 22, GR, italic=True)]
    svg("03c-teil2.svg", b, h=390)


def s02b_berufsbild():
    b = [C(130, 265, 110, "none", GR, 3, dash=True), person(130, 285, 1.8, "#c7ccd4"),
         T(130, 410, "SW-Entwickler\nheute", 22, GR, bold=True, vc=True),
         Ar(245, 235, 368, 160, GR, 4), Ar(245, 300, 368, 385, GR, 4),
         Rc(380, 80, 350, 145, NL, N, 16), person(440, 160, 1.0),
         T(490, 132, "Systemarchitekt", 24, N, anchor="start", bold=True),
         T(490, 166, "technischer Kontext", 20, GR, anchor="start", bold=True),
         pill(490, 182, 120, 30, "vielleicht", AL, A, 16),
         Rc(380, 315, 350, 145, GL, G, 16), person(440, 395, 1.0, G),
         T(490, 362, "Produktplaner /", 24, G, anchor="start", bold=True),
         T(490, 390, "Anforderungsanalyst", 20, G, anchor="start", bold=True),
         T(490, 418, "fachlicher Kontext", 20, GR, anchor="start", bold=True),
         pill(625, 432, 95, 24, "sicher", G, "white", 15),
         Ar(735, 152, 862, 245), Ar(735, 388, 862, 305, G),
         T(800, 180, "Kontext", 18, GR, bold=True), T(800, 375, "Kontext", 18, GR, bold=True),
         robot(930, 290, 1.4), Ar(1000, 275, 1032, 275),
         box(1040, 235, 105, 80, "</>", fs=30, mono=True)]
    svg("02b-berufsbild.svg", b)


def s03_guardrails():
    b = [L(40, 142, 960, 142, N, 6), L(40, 398, 960, 398, N, 6)]
    for i in range(6):
        b.append(pill(60 + i * 150, 120, 130, 44, "Skill", R, "white", 22))
        b.append(pill(60 + i * 150, 376, 130, 44, "Skill", R, "white", 22))
    b += [T(500, 100, "Architekturvorgaben", 26, N, bold=True),
          T(500, 460, "prüfbare Qualitätskriterien", 26, N, bold=True),
          robot(105, 285, 1.0)]
    xs = [320, 500, 680, 860]
    for x, lab in zip(xs, ["Code", "Review", "Test", "Deploy"]):
        b += [C(x, 270, 52, NL, N, 3), T(x, 270, lab, 20, N, bold=True, vc=True)]
    b += [Ar(160, 270, 262, 270), Ar(372, 270, 442, 270), Ar(552, 270, 622, 270), Ar(732, 270, 802, 270),
          Ar(912, 270, 985, 270, G), shield(1065, 250, 0.95),
          T(1065, 390, "100 %\nVertrauen", 24, G, bold=True)]
    svg("03-guardrails.svg", b)


def s03b_verantwortung():
    b = [T(580, 38, "Welche fremden Ressourcen können wir guten Gewissens verantworten?", 24, GR, bold=True),
         person(85, 300, 0.9), person(155, 300, 0.9), person(120, 285, 1.1, R),
         T(120, 390, "Team\nverantwortet", 22, N, bold=True, vc=True)]
    bars = [("Java\nTypeScript", G, 320, "jahrelange\nErfahrung"),
            ("Spring\nAngular", G, 280, "etabliert"),
            ("Libraries", A, 190, "je nach\nReifegrad"),
            ("GSD · BMAD\nOpenSpec", R, 95, "zu jung")]
    for i, (lab, c, h, sub) in enumerate(bars):
        x = 270 + i * 225
        top = 430 - h
        b += [Rc(x, top, 200, h, c, "none", 10),
              T(x + 100, top + (48 if h > 120 else h / 2), lab, 22, "white", bold=True, vc=True),
              T(x + 100, 470, sub, 20, GR, bold=True)]
        if c == G:
            b += [C(x + 100, top - 40, 26, GL), check(x + 100, top - 40, 14)]
        elif c == A:
            b += [C(x + 100, top - 40, 26, AL), T(x + 100, top - 40, "~", 34, A, bold=True, vc=True)]
        else:
            b += [C(x + 100, top - 40, 26, RL), xmark(x + 100, top - 40, 11)]
    b.append(L(255, 430, 1150, 430, GR, 3))
    svg("03b-verantwortung.svg", b)


def s04_eigene_skills():
    cx, cy, rr = 290, 275, 170
    nodes = [(-90, "Skill", R), (0, "Einsatz", N), (90, "Fehler", A), (180, "Fix", G)]
    b = []
    for i in range(4):
        a1 = math.radians(nodes[i][0] + 24)
        a2 = math.radians(nodes[i][0] + 90 - 24)
        x1, y1 = cx + rr * math.cos(a1), cy + rr * math.sin(a1)
        x2, y2 = cx + rr * math.cos(a2), cy + rr * math.sin(a2)
        b.append(Pa(f"M{x1:.1f},{y1:.1f} A{rr},{rr} 0 0,1 {x2:.1f},{y2:.1f}", GR, 5))
    for ang, lab, col in nodes:
        a = math.radians(ang)
        x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
        b += [C(x, y, 56, col), T(x, y, lab, 22, "white", bold=True, vc=True)]
    b += [person(cx - 42, cy + 5, 0.7), person(cx + 42, cy + 5, 0.7), person(cx, cy - 5, 0.85, R),
          T(cx, cy + 68, "unser Team", 22, N, bold=True),
          T(cx, cy + 94, "versteht jede Zeile", 18, GR, bold=True),
          T(600, 285, "vs.", 40, GR, bold=True),
          T(890, 80, "fremder Skill", 28, GR, bold=True),
          Rc(720, 100, 340, 250, "#374151", "none", 20),
          T(890, 290, "?", 170, "white", bold=True),
          pill(725, 372, 105, 42, "GSD", GRL, GR), pill(838, 372, 105, 42, "BMAD", GRL, GR),
          pill(951, 372, 115, 42, "OpenSpec", GRL, GR, 18),
          T(890, 470, "Wer fixt Fehler nachhaltig?", 28, R, bold=True)]
    svg("04-eigene-skills.svg", b)


def s05_fakegit():
    b = [person(120, 185, 1.6, DARK), C(155, 118, 18, R), T(155, 125, "!", 22, "white", bold=True),
         T(120, 275, "Angreifer", 22, N, bold=True)]
    for dx in (30, 15, 0):
        b.append(doc(345 + dx, 95 + 15 - dx / 2, 110, 140, R, RL if dx else "white"))
    b += [T(420, 285, "Fake-Skills\n& MCP-Server", 22, N, bold=True),
          robot(700, 195, 1.3), T(700, 275, "KI-Assistent", 22, N, bold=True),
          person(990, 185, 1.6, N), C(1030, 130, 24, R), T(1030, 139, "!", 26, "white", bold=True),
          T(990, 285, "Nutzer +\nInfostealer", 22, N, bold=True),
          Ar(185, 175, 320, 175, R), T(252, 150, "publiziert", 20, GR),
          Ar(495, 175, 620, 175, R), T(558, 150, "findet", 20, GR),
          Ar(780, 175, 915, 175, R), T(848, 150, "empfiehlt", 20, GR)]
    for x, big, lab in [(60, "7.600", "Fake-Repos"), (430, "14 Mio.", "Downloads"), (800, "800+", "Fake-Skills & MCP")]:
        b += [Rc(x, 340, 300, 125, RL, "none", 16), T(x + 150, 400, big, 50, R, bold=True), T(x + 150, 442, lab, 22, N, bold=True)]
    b.append(T(580, 515, "Angreifer täuschen nicht mehr die Nutzer – sondern deren Assistenten.", 22, GR, italic=True))
    svg("05-fakegit.svg", b)


def s05b_skills_projekt():
    stages = [("Anforderungs-\nanalyse", R), ("Plan-\nerstellung", N), ("Coding", "#9ca3af"), ("QS &\nCode Review", N)]
    b = [T(165, 60, "im Fokus", 24, R, bold=True), Ar(165, 72, 165, 132, R, 5)]
    for i, (lab, c) in enumerate(stages):
        x = 30 + i * 278
        b.append(chevron(x, 145, 275, 130, c, lab, 24, first=(i == 0)))
        cx = x + 140
        if i == 2:
            b += [Rc(cx - 120, 315, 240, 60, "white", GR, 12, 3, dash=True),
                  T(cx, 353, "„setze Plan XY um\"", 20, DARK, bold=True, mono=True),
                  T(cx, 410, "kein Skill – nur Prompt", 20, GR, bold=True)]
        else:
            b.append(pill(cx - 60, 320, 120, 46, "Skill", R if i == 0 else NL, "white" if i == 0 else N, 22))
    b += [pill(60, 395, 220, 44, "issue-grundlage", RL, R, 20, mono=True),
          person(505, 480, 0.6), person(555, 480, 0.6, R), person(605, 480, 0.6, G),
          T(645, 490, "Skills von verschiedenen Entwicklern", 20, GR, anchor="start", bold=True)]
    svg("05b-skills-projekt.svg", b)


def s06_ziel():
    b = [doc(50, 150, 110, 140, N), T(105, 318, "Issue", 22, N, bold=True),
         figma(105, 420, 1.6), T(105, 495, "Figma", 22, N, bold=True),
         Ar(165, 225, 278, 280), Ar(160, 415, 278, 325),
         C(360, 300, 85, R), T(360, 300, "Issue-\nGrundlage", 24, "white", bold=True, vc=True),
         Ar(450, 300, 518, 300),
         doc(530, 220, 120, 160, G, GL), badge_check(640, 370, 28), T(590, 425, "Grundlage", 22, G, bold=True),
         Ar(665, 300, 730, 300),
         box(740, 250, 130, 100, "Plan"), Ar(875, 300, 935, 300),
         box(945, 250, 130, 100, "</>", fs=34, mono=True),
         Pa("M1010,245 C1010,80 380,80 370,205", GR, 4, dash=True),
         xmark(694, 118, 26), T(694, 70, "Korrekturschleifen", 22, GR, bold=True),
         Rc(740, 400, 335, 115, "none", N, 14, 3, dash=True), T(907, 428, "Monorepo", 20, N, bold=True),
         box(765, 445, 135, 55, "BE", fs=22), box(915, 445, 135, 55, "FE", fs=22)]
    svg("06-ziel.svg", b)


def s07_problem():
    b = [Rc(20, 20, 540, 500, GRL, "none", 20), Rc(600, 20, 540, 500, GRL, "none", 20),
         C(62, 70, 24, N), T(62, 70, "1", 24, "white", bold=True, vc=True),
         T(100, 79, "Warum selbst kopieren?", 24, N, anchor="start", bold=True),
         doc(50, 175, 100, 130, GITLAB, "#fdeee9"), T(100, 335, "GitLab", 22, GITLAB, bold=True),
         Ar(160, 240, 225, 240), T(192, 222, "Strg+C", 18, GR, bold=True),
         person(290, 250, 1.3), T(290, 335, "ich", 22, N, bold=True),
         Ar(345, 240, 405, 240), T(375, 222, "Strg+V", 18, GR, bold=True),
         robot(470, 255, 1.0), T(470, 335, "Agent", 22, N, bold=True),
         check(85, 410, 16), T(115, 418, "Backend: ok-ish", 24, N, anchor="start", bold=True),
         xmark(85, 465, 14), T(115, 473, "Frontend: nicht brauchbar", 24, R, anchor="start", bold=True),
         C(642, 70, 24, N), T(642, 70, "2", 24, "white", bold=True, vc=True),
         T(680, 79, "FE steckt im Figma", 24, N, anchor="start", bold=True),
         figma(665, 260, 1.5),
         Rc(720, 115, 390, 280, "white", GR, 10, 3, dash=True)]
    for x, y, w, h, c in [(745, 140, 120, 60, NL), (890, 135, 180, 40, AL), (750, 225, 85, 85, PL),
                          (860, 200, 110, 110, GL), (995, 190, 90, 55, RL), (990, 270, 100, 90, NL),
                          (750, 330, 210, 42, GRL)]:
        b.append(Rc(x, y, w, h, c, GR, 6, 2))
    b += [T(840, 225, "?", 44, R, bold=True), T(1045, 255, "?", 44, R, bold=True), T(990, 385, "?", 44, R, bold=True),
          T(870, 432, "noch kein finales Design System –", 22, N, bold=True),
          T(870, 462, "spartan-ng lässt viele Freiheiten", 22, N, bold=True),
          T(870, 495, "(= shadcn für Angular)", 20, GR)]
    svg("07-problem.svg", b)


def s08_iterationen():
    fills = ["#9fb6cd", "#6f93b6", "#3f709f", N]
    labels = ["glab +\nFigma-Prompt", "Properties statt\nScreenshot", "Skill\nIssue-Grundlage", "2 Analysten\n+ Merger"]
    b = []
    for i in range(4):
        x, top = 60 + i * 265, 430 - i * 90
        b += [Rc(x, top, 250, 510 - top, fills[i], "none", 6),
              T(x + 125, top + 52, str(i + 1), 44, "white", bold=True),
              T(x + 125, top - 50, labels[i], 22, N, bold=True)]
    b += [L(1120, 160, 1120, 40, DARK, 4), f'<polygon points="1120,40 1060,58 1120,76" fill="{G}"/>']
    svg("08-iterationen.svg", b)


def s09_iteration1():
    b = [L(30, 265, 1130, 265, GR, 2, dash=True),
         box(40, 110, 160, 80, "GitLab", "#fdeee9", GITLAB, GITLAB), Ar(205, 150, 290, 150),
         box(300, 110, 180, 80, "glab-Skill", "white", R, R), Ar(485, 150, 570, 150),
         robot(630, 165, 1.0), Ar(690, 150, 780, 150, A), C(830, 150, 34, AL, A, 4), T(830, 150, "~", 44, A, bold=True, vc=True),
         T(885, 140, "nur Backend:", 24, A, anchor="start", bold=True),
         T(885, 172, "klappt manchmal", 24, A, anchor="start", bold=True),
         pill(40, 40, 140, 38, "Backend", NL, N, 20), pill(40, 280, 140, 38, "Frontend", RL, R, 20),
         figma(120, 380, 1.4), Ar(205, 380, 290, 380),
         box(300, 340, 180, 80, "Beispiel-\nPrompt", "white", GR, GR, 22), Ar(485, 380, 570, 380),
         robot(630, 395, 1.0), Ar(690, 380, 780, 380, R),
         Rc(790, 300, 200, 160, "white", N, 10, 4), Rc(790, 300, 200, 30, N, "none", 0),
         xmark(840, 370, 16), xmark(905, 420, 16), xmark(950, 360, 16),
         Pa("M1080,335 A45,45 0 1,1 1035,380", R, 5), T(1080, 470, "1 Prompt\npro Fehler", 20, R, bold=True)]
    svg("09-iteration1.svg", b)


def s10_iteration2():
    b = [imageicon(60, 70, 220, 160), nosign(170, 150, 105), T(170, 290, "PNG-Screenshot", 22, N, bold=True),
         Ar(300, 150, 388, 150, G),
         Rc(400, 55, 330, 205, GL, G, 14, 3), badge_check(725, 60, 26)]
    for i, t in enumerate(["color: --primary", "gap: 16px", "radius: 8px", "font: 14/20"]):
        b.append(T(425, 100 + i * 45, t, 22, N, anchor="start", mono=True, bold=True))
    b.append(T(565, 290, "Design-Properties", 22, G, bold=True))
    for i, c in enumerate([NL, AL, PL]):
        y = 45 + i * 60
        b.append(f'<polygon points="820,{y + 50} 965,{y} 1120,{y + 50} 975,{y + 100}" fill="{c}" '
                 f'fill-opacity="0.9" stroke="{N}" stroke-width="2"/>')
    for x, y in [(900, 95), (1020, 90), (950, 150), (1060, 205), (880, 215), (990, 260)]:
        b.append(C(x, y, 10, R))
    b += [T(970, 290, "verteilt auf Ebenen", 22, N, bold=True),
          Rc(20, 330, 1120, 195, AL, "none", 16),
          person(110, 440, 1.2), Ar(160, 425, 228, 425, A),
          T(500, 380, "10–20 Figma-Links von Hand", 22, N, bold=True)]
    for i in range(10):
        b.append(linkicon(265 + i * 52, 430))
    b += [Ar(780, 425, 850, 425, A), doc(860, 360, 100, 130, N),
          clock(1060, 420, 45), T(1060, 505, "Handarbeit", 20, A, bold=True)]
    svg("10-iteration2.svg", b)


def s11_iteration3():
    b = [doc(40, 180, 90, 115, N), T(85, 330, "Issue 1×", 22, N, bold=True),
         figma(85, 445, 1.2),
         Ar(140, 240, 250, 265), Ar(115, 440, 255, 320),
         C(330, 280, 82, R), T(330, 280, "Issue-\nGrundlage", 22, "white", bold=True, vc=True),
         pill(225, 390, 190, 40, "Pflichtschritt F", RL, R, 18),
         Ar(415, 280, 490, 280),
         doc(500, 25, 300, 480, N, "white", lines=False)]
    for y, h, c, fc, t in [(95, 65, NL, N, "Anforderungen"), (175, 90, GL, G, "Design-Details"),
                           (280, 65, PL, P, "implizite Details"), (360, 65, AL, A, "Lücken ?")]:
        b += [Rc(525, y, 250, h, c, "none", 8), T(650, y + h / 2, t, 22, fc, bold=True, vc=True)]
    b += [T(650, 475, "3–4× so lang", 28, N, bold=True),
          Pa("M780,392 Q860,392 925,350", A, 4, dash=True), T(880, 350, "Rückfrage", 20, A, bold=True),
          person(1000, 345, 1.4), Rc(915, 150, 190, 95, AL, A, 22, 3),
          f'<polygon points="985,243 1005,243 990,270" fill="{AL}" stroke="{A}" stroke-width="3"/>',
          T(1010, 218, "?", 56, A, bold=True)]
    svg("11-iteration3.svg", b)


def s12_iteration4():
    b = [doc(30, 115, 90, 115, N), T(75, 258, "Issue", 20, N, bold=True),
         figma(75, 400, 1.2), T(75, 470, "Figma", 20, N, bold=True),
         Ar(125, 172, 222, 145, GR, 3), Ar(125, 180, 222, 390, GR, 3),
         Ar(110, 395, 222, 160, GR, 3), Ar(110, 400, 222, 400, GR, 3),
         Rc(230, 75, 210, 140, NL, N), robot(285, 155, 0.75), T(375, 145, "Claude\nOpus 5", 20, N, bold=True, vc=True),
         Rc(230, 330, 210, 140, AL, A), robot(285, 410, 0.75, A), T(375, 400, "Codex\ngpt-5.6", 20, A, bold=True, vc=True),
         Ar(445, 145, 478, 145), Ar(445, 400, 478, 400, A),
         doc(488, 92, 80, 105, N), doc(488, 348, 80, 105, A),
         Ar(575, 150, 632, 225), Ar(575, 395, 632, 318, A),
         C(690, 270, 75, P), T(690, 270, "Merger", 22, "white", bold=True, vc=True),
         Ar(770, 270, 828, 270, P),
         doc(840, 120, 150, 250, G, "white", lines=False),
         checklist(862, 200, ["U1", "U2", "U3"], 22, 55),
         T(915, 405, "offene Punkte", 22, G, bold=True),
         Ar(995, 245, 1035, 245, G),
         person(1090, 200, 0.95), T(1090, 262, "PO", 20, N, bold=True),
         person(1090, 350, 0.95, P), T(1090, 412, "UX", 20, P, bold=True)]
    svg("12-iteration4.svg", b)


def s13_regeln():
    b = []
    labels = ["Code lesen –\nnicht ändern", "Keine\nScreenshots", "Jede Aussage\nbelegt", "Nichts\nerfinden"]
    for i in range(4):
        x = 30 + i * 285
        b += [Rc(x, 50, 265, 430, GRL, "none", 20), T(x + 132, 390, labels[i], 26, N, bold=True, vc=True)]
    cx = 30 + 132
    b += [Rc(cx - 85, 130, 150, 115, "white", N, 12, 4), T(cx - 10, 205, "</>", 48, N, bold=True, mono=True),
          f'<ellipse cx="{cx + 45}" cy="{265}" rx="48" ry="28" fill="{GL}" stroke="{G}" stroke-width="5"/>',
          C(cx + 45, 265, 13, G)]
    cx += 285
    b += [imageicon(cx - 85, 140, 170, 120), nosign(cx, 200, 95)]
    cx += 285
    b += [doc(cx - 70, 110, 110, 140, N),
          f'<polygon points="{cx - 45},230 {cx + 100},230 {cx + 120},255 {cx + 100},280 {cx - 45},280" fill="{G}"/>',
          T(cx + 33, 262, "Figma-Node-ID", 17, "white", bold=True)]
    cx += 285
    b += [xmark(cx - 95, 163, 13), T(cx - 70, 175, "vermutlich", 30, GR, anchor="start", italic=True),
          xmark(cx - 95, 238, 13), T(cx - 70, 250, "analog zu", 30, GR, anchor="start", italic=True)]
    svg("13-regeln.svg", b)


def s14_pflichtschritt_f():
    b = [T(160, 75, "Instanz", 26, N, bold=True), Rc(40, 95, 240, 190, "white", N, 12, 4),
         Rc(80, 165, 160, 56, N, "none", 10), T(160, 193, "Button", 22, "white", bold=True, vc=True),
         T(160, 322, "zeigt nur 1 State", 22, GR, bold=True),
         Ar(295, 190, 405, 190, P, 5, dash=True),
         Rc(420, 45, 710, 300, PL, P, 16, 3, dash=True), T(445, 82, "Component-Set", 22, P, anchor="start", bold=True)]
    states = [("Default", "d"), ("Hover", "h"), ("Disabled", "x"), ("Error", "e"), ("Empty", "m"), ("Skeleton", "s")]
    for k, (lab, t) in enumerate(states):
        i, j = divmod(k, 3)
        x, y = 450 + j * 225, 105 + i * 115
        border = G if t == "d" else GR
        b.append(Rc(x, y, 200, 100, "white", border, 10, 4 if t == "d" else 2))
        mx, my = x + 45, y + 18
        if t == "d":
            b.append(Rc(mx, my, 110, 36, N, "none", 8))
        elif t == "h":
            b.append(Rc(mx, my, 110, 36, "#3f7cb8", "none", 8))
        elif t == "x":
            b.append(Rc(mx, my, 110, 36, "#d1d5db", "none", 8))
        elif t == "e":
            b += [Rc(mx, my, 110, 36, "white", R, 8, 3), T(mx + 55, my + 27, "!", 24, R, bold=True)]
        elif t == "m":
            b.append(Rc(mx, my, 110, 36, "none", GR, 8, 2, dash=True))
        else:
            b += [Rc(mx, my + 4, 110, 12, "#e5e7eb", "none", 6), Rc(mx, my + 22, 70, 12, "#e5e7eb", "none", 6)]
        b.append(T(x + 100, y + 84, lab, 18, N if t == "d" else GR, bold=True))
    b.append(T(775, 380, "5 von 6 States in der Instanz unsichtbar", 22, R, bold=True))
    fills = ["#9fb6cd", "#6f93b6", "#3f709f", N]
    labs = ["1 Inventar", "2 Matchen", "3 Disponieren", "4 Node-ID belegen"]
    for i in range(4):
        b.append(chevron(40 + i * 275, 425, 270, 80, fills[i], labs[i], 22, first=(i == 0)))
    svg("14-pflichtschritt-f.svg", b)


def s15_figma_zugang():
    b = [robot(90, 145, 1.0), T(90, 215, "Claude Code", 20, N, bold=True),
         robot(90, 375, 1.0, A), T(90, 445, "Codex", 20, A, bold=True),
         Ar(145, 130, 162, 130), Ar(145, 360, 162, 360, A),
         pill(170, 105, 300, 50, "mcp__figma-desktop__", NL, N, 18, mono=True),
         T(320, 182, "Bindestrich", 18, GR, bold=True),
         pill(170, 335, 300, 50, "mcp__figma_desktop__", AL, A, 18, mono=True),
         T(320, 412, "Unterstrich", 18, GR, bold=True),
         Ar(475, 140, 562, 215), Ar(475, 350, 562, 305, A),
         Rc(570, 190, 230, 140, N, "none", 16),
         T(685, 245, "figma-desktop MCP", 22, "white", bold=True),
         T(685, 290, "127.0.0.1:3845", 18, "white", bold=True, mono=True),
         lightning(600, 140, 0.6, G), T(625, 150, "schneller als Cloud", 22, G, anchor="start", bold=True),
         Ar(805, 260, 872, 260),
         monitor(990, 255, "Figma\nDesktop"),
         pill(895, 355, 190, 44, "nur nodeId", AL, A, 20, mono=True),
         T(990, 428, "aktives Dokument", 20, GR, bold=True),
         L(30, 465, 1130, 465, GR, 2, dash=True),
         T(60, 510, "nicht autorisiert:", 22, GR, anchor="start", bold=True)]
    for x, lab in [(300, "Cloud-Connector"), (580, "REST-API"), (780, "Web-Browsing")]:
        b += [xmark(x, 503, 13), T(x + 25, 511, lab, 22, R, anchor="start", bold=True)]
    svg("15-figma-zugang.svg", b)


def s16_analysekatalog():
    cols = [("Erfassen", N, [("A1", "Akzeptanzkriterien"), ("A2", "Tasks"), ("A3", "Figma-Inventar")]),
            ("Zuordnen", "#3f709f", [("A4", "AK → Figma"), ("A5", "Detail-Spec"), ("A6", "Über-/Unterdeckung"),
                                     ("A6b", "Bestandsanalyse")]),
            ("Prüfen", P, [("A7", "Widersprüche"), ("A8", "Vollständigkeit"), ("A9", "Klärungsliste")])]
    b = []
    for i, (title, col, items) in enumerate(cols):
        x = 30 + i * 375
        b.append(chevron(x, 40, 370, 120, col, title, 34, first=(i == 0)))
        for k, (aid, it) in enumerate(items):
            y = 230 + k * 75
            new = aid == "A6b"
            b += [C(x + 60, y, 28, R if new else col), T(x + 60, y, aid, 16 if new else 18, "white", bold=True, vc=True),
                  T(x + 105, y + 8, it, 24, R if new else N, anchor="start", bold=True)]
    svg("16-analysekatalog.svg", b)


def s17_zuordnung():
    aks = ["AK1.1", "AK1.2", "AK2.1", "AKK1", "T93.1"]
    st = [G, A, R, GR, P]
    b = []
    for i, (ak, c) in enumerate(zip(aks, st)):
        y = 60 + i * 80
        b += [pill(50, y, 170, 52, ak, NL, N, 22, mono=True), C(255, y + 26, 15, c)]
    frames = [(55, "12:345"), (155, "12:410"), (360, "14:002")]
    for y, nid in frames:
        b += [Rc(620, y, 220, 64, "white", N, 10, 3), figma(655, y + 32, 0.7), T(760, y + 40, nid, 22, N, bold=True, mono=True)]
    b += [L(275, 86, 615, 87, G, 5), L(275, 166, 615, 187, A, 5), L(275, 246, 690, 300, R, 4, dash=True),
          C(720, 300, 30, RL, R, 3), T(720, 300, "?", 32, R, bold=True, vc=True),
          T(360, 335, "kein UI", 20, GR, bold=True, italic=True),
          L(275, 406, 615, 392, P, 5), C(445, 399, 28, "white"), lightning(445, 399, 0.8)]
    leg = [(G, "belegt"), (A, "teilweise belegt"), (R, "nicht gefunden *"), (GR, "kein Figma-Bezug"), (P, "widersprüchlich")]
    b.append(Rc(880, 45, 260, 400, GRL, "none", 16))
    for i, (c, lab) in enumerate(leg):
        y = 100 + i * 75
        b += [C(915, y, 15, c), T(945, y + 8, lab, 22, N, anchor="start", bold=True)]
    b.append(T(580, 505, "* erst nach vollständigem Pflichtschritt F", 22, R, bold=True))
    svg("17-zuordnung.svg", b)


def s17b_bestand():
    rows = [("AK1.1", "neu", N, "–", None),
            ("AK1.2", "Wiederverwendung", G, "user.service.ts:42", None),
            ("AK2.1", "Erweiterung", A, "list.component.ts:88", None),
            ("AK2.2", "Änderung", R, "OrderController.java:17", "→ Widersprüche"),
            ("AKK1", "unklar", GR, "?", "→ Klärungsliste")]
    b = [Rc(30, 20, 250, 70, DARK, "none", 12),
         T(50, 52, "backend/src", 20, "#4ade80", anchor="start", bold=True, mono=True),
         T(50, 78, "frontend/src", 20, "#4ade80", anchor="start", bold=True, mono=True),
         f'<ellipse cx="330" cy="55" rx="38" ry="22" fill="{GL}" stroke="{G}" stroke-width="4"/>', C(330, 55, 10, G),
         T(385, 64, "nur lesen", 24, G, anchor="start", bold=True)]
    for i, (ak, lab, c, path, extra) in enumerate(rows):
        y = 125 + i * 78
        b += [pill(30, y, 150, 50, ak, NL, N, 22, mono=True), Ar(190, y + 25, 250, y + 25, GR, 4),
              Rc(260, y, 280, 50, c, "none", 25), T(400, y + 25, lab, 22, "white", bold=True, vc=True),
              T(565, y + 33, path, 20, N, anchor="start", bold=True, mono=True)]
        if extra:
            b.append(T(900, y + 33, extra, 22, c, anchor="start", bold=True))
    b.append(T(870, 64, "Befund – keine Lösung", 24, GR, bold=True, italic=True))
    svg("17b-bestand.svg", b)


def s18_ablauf():
    b = [C(60, 260, 36, N), T(60, 260, "0", 30, "white", bold=True, vc=True), T(60, 328, "Snapshot", 20, N, bold=True),
         Ar(98, 260, 138, 260),
         f'<polygon points="195,202 250,260 195,318 140,260" fill="{N}"/>', T(195, 260, "1", 30, "white", bold=True, vc=True),
         T(195, 184, "Figma-Link?", 20, N, bold=True),
         Ar(195, 323, 195, 393, R, 4, dash=True), T(207, 366, "fehlt", 18, R, anchor="start", bold=True),
         person(195, 448, 0.75, R), T(243, 458, "fragen", 18, R, anchor="start", bold=True),
         Ar(252, 255, 300, 160), Ar(252, 265, 300, 365, A),
         Rc(308, 110, 180, 90, NL, N), robot(350, 165, 0.6), T(438, 155, "2\nOpus 5", 20, N, bold=True, vc=True),
         Rc(308, 320, 180, 90, AL, A), robot(350, 375, 0.6, A), T(438, 365, "3\nCodex", 20, A, bold=True, vc=True),
         Ar(492, 155, 548, 235), Ar(492, 365, 548, 285, A),
         Rc(555, 195, 30, 130, A, "none", 6), T(570, 260, "4", 22, "white", bold=True, vc=True),
         T(570, 355, "Barriere", 20, N, bold=True),
         Ar(590, 260, 630, 260),
         C(685, 260, 50, P), T(685, 260, "5\nMerger", 18, "white", bold=True, vc=True),
         Ar(738, 260, 772, 260, P)]
    for k, c in enumerate([G, P, R]):
        b.append(doc(782 + k * 14, 200 + k * 22, 70, 90, c, "white", lines=(k == 2)))
    b += [T(836, 355, "3 Dokumente", 18, N, bold=True),
          Ar(870, 260, 905, 260),
          Rc(912, 212, 100, 96, AL, A, 12), T(962, 245, "5b", 24, A, bold=True, vc=True),
          T(962, 282, "todo.md", 16, A, bold=True, mono=True),
          T(962, 340, "Nutzer\nentscheidet", 16, A, bold=True, vc=True),
          Ar(1016, 260, 1052, 260, G),
          C(1100, 260, 45, G), T(1100, 260, "6", 30, "white", bold=True, vc=True),
          T(1100, 328, "Bericht", 20, G, bold=True),
          L(308, 60, 880, 60, G, 4), L(308, 50, 308, 70, G, 4), L(880, 50, 880, 70, G, 4),
          T(594, 45, "läuft am Stück – keine Rückfragen", 22, G, bold=True)]
    svg("18-ablauf.svg", b)


def s19_merger():
    b = [C(330, 280, 190, NL, N, 3, op=0.85), C(590, 280, 190, AL, A, 3, op=0.7),
         T(230, 280, "nur\nOpus 5", 26, N, bold=True, vc=True),
         T(695, 280, "nur\ngpt-5.6-sol", 26, A, bold=True, vc=True),
         T(460, 280, "beide", 30, DARK, bold=True, vc=True),
         C(460, 125, 34, "white", P, 3), lightning(460, 125, 0.75),
         T(460, 520, "nichts wegkürzen · nichts mitteln", 22, GR, bold=True),
         doc(880, 20, 100, 125, G, GL), T(1000, 90, "Haupt-\ndokument", 20, G, anchor="start", bold=True, vc=True),
         doc(880, 195, 100, 125, P, PL, lines=False), lightning(930, 265, 0.7),
         T(1000, 265, "Wider-\nsprüche", 20, P, anchor="start", bold=True, vc=True),
         doc(880, 370, 100, 125, R, "white", lines=False),
         checklist(897, 420, ["U1", "U2"], 18, 36, R),
         T(1000, 420, "Klärung", 20, R, anchor="start", bold=True),
         T(1000, 448, "Nutzer", 18, R, anchor="start", bold=True),
         T(1000, 472, "entscheidet", 18, R, anchor="start", bold=True),
         Pa("M690,110 Q780,55 872,80", G, 4),
         Pa("M495,120 C600,100 760,200 872,250", P, 4),
         Pa("M930,325 L930,362", R, 4, dash=True)]
    svg("19-merger.svg", b)


def s20_lessons():
    tiles = [(20 + i * 380, 15 + j * 265) for j in range(2) for i in range(3)]
    b = [Rc(x, y, 360, 245, GRL, "none", 18) for x, y in tiles]

    def caption(x, y, title, sub):
        return T(x + 180, y + 180, title, 22, N, bold=True) + T(x + 180, y + 214, sub, 18, GR, bold=True)
    x, y = tiles[0]; cx = x + 180
    b += [pill(cx - 100, y + 12, 90, 30, "MCP", RL, R, 16), pill(cx + 10, y + 12, 90, 30, "MCP", RL, R, 16),
          f'<polygon points="{cx - 110},{y + 52} {cx + 110},{y + 52} {cx + 22},{y + 105} {cx + 22},{y + 140} '
          f'{cx - 22},{y + 140} {cx - 22},{y + 105}" fill="{N}"/>',
          T(cx, y + 82, "tools:", 18, "white", bold=True, mono=True), xmark(cx + 60, y + 128, 12),
          caption(x, y, "Keine tools:-Allowlist", "filtert alle MCP-Server")]
    x, y = tiles[1]; cx = x + 180
    b += [Rc(cx - 125, y + 22, 250, 110, DARK, "none", 12),
          T(cx - 108, y + 66, "$ codex exec", 20, "#4ade80", anchor="start", bold=True, mono=True),
          T(cx - 108, y + 106, "  < /dev/null", 20, "#fbbf24", anchor="start", bold=True, mono=True),
          caption(x, y, "stdin schließen", "sonst hängt codex")]
    x, y = tiles[2]; cx = x + 180
    for k in range(4):
        b.append(doc(cx - 130 + (k % 2) * 50, y + 20 + (k // 2) * 62, 42, 55, N))
    b += [Ar(cx - 30, y + 78, cx + 30, y + 78), T(cx, y + 62, "cat", 16, GR, bold=True, mono=True),
          doc(cx + 45, y + 20, 70, 115, G, GL),
          caption(x, y, "Teil-Dateien + cat", "Enddokument passt nicht in 1 Write")]
    x, y = tiles[3]; cx = x + 180
    b += [Rc(cx - 115, y + 80, 230, 34, "white", N, 17, 3), Rc(cx - 115, y + 80, 145, 34, G, "none", 17),
          Pa(f"M{cx + 30},{y + 70} Q{cx + 65},{y + 25} {cx + 100},{y + 70}", G, 5),
          caption(x, y, "Fortsetzen statt Neustart", "U-Nummern bleiben stabil")]
    x, y = tiles[4]; cx = x + 180
    b += [monitor(cx - 55, y + 70, "Figma"), Rc(cx + 55, y + 30, 90, 80, "white", N, 12, 4),
          T(cx + 100, y + 70, "⌘Q", 30, N, bold=True, vc=True),
          caption(x, y, "Figma hängt: neu starten", "vorher curl-Check auf Port 3845")]
    x, y = tiles[5]; cx = x + 180
    b += [robot(cx - 70, y + 100, 0.9), Rc(cx - 5, y + 25, 130, 58, AL, A, 18, 3),
          f'<polygon points="{cx + 5},{y + 70} {cx + 25},{y + 82} {cx - 20},{y + 95}" fill="{AL}" stroke="{A}" stroke-width="3"/>',
          T(cx + 60, y + 54, "weiter!", 22, A, bold=True, vc=True),
          caption(x, y, "Subagent fortsetzen", "SendMessage – Kontext bleibt")]
    svg("20-lessons.svg", b)


def s21_fazit():
    xs = [160, 440, 720, 1000]
    cols = [N, G, A, R]
    labs = ["Eigene\nSkills", "Belege statt\nVermutungen", "Zwei\nAnalysten", "Mensch klärt –\nAgent setzt um"]
    b = []
    for x, c, lab in zip(xs, cols, labs):
        b += [C(x, 150, 100, c), T(x, 305, lab, 26, N, bold=True, vc=True)]
    b += [person(120, 160, 0.7, "white"), person(200, 160, 0.7, "white"), person(160, 150, 0.85, "white"),
          f'<polygon points="{390},{120} {470},{120} {495},{150} {470},{180} {390},{180}" fill="white"/>',
          T(440, 158, "ID", 26, G, bold=True),
          robot(680, 170, 0.6, "white", A), robot(760, 170, 0.6, "white", A),
          person(960, 165, 0.8, "white"), robot(1040, 170, 0.6, "white", R)]
    svg("21-fazit.svg", b, h=360)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("s") and name[1:3].isdigit() and callable(fn):
            fn()
    print("ok")
