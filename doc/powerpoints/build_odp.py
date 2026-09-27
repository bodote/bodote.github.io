#!/usr/bin/env python3
"""Baut Issue-Grundlage-Claude.odp aus der Marp-Quelle Issue-Grundlage-Claude.md.

Schritte: SVG-Grafiken erzeugen -> Marp (editierbares PPTX, braucht LibreOffice)
-> LibreOffice (ODP) -> Sprechernotizen aus den <!-- ... -->-Kommentaren einfuegen.
Marp verliert die Notizen im editierbaren Modus, darum werden sie hier nachgetragen.

Aufruf: python3 build_odp.py
"""
import html
import os
import re
import shutil
import subprocess
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
NAME = "Issue-Grundlage-Claude"
SOFFICE_DIR = "/Applications/LibreOffice.app/Contents/MacOS"


def slide_notes(md):
    body = md.split("\n---\n", 1)[1]  # Front Matter abtrennen
    notes = []
    for slide in re.split(r"\n---\n", body):
        comments = re.findall(r"<!--(.*?)-->", slide, re.S)
        text = [c.strip() for c in comments if not c.strip().startswith("_")]
        notes.append("\n".join(text))
    return notes


def para(line):
    # fuehrende Leerzeichen als <text:s/>, sonst fasst ODF die Einrueckung zusammen
    n = len(line) - len(line.lstrip(" "))
    indent = f'<text:s text:c="{n}"/>' if n else ""
    return f"<text:p>{indent}{html.escape(line.lstrip(' '))}</text:p>"


def inject_notes(odp, notes):
    with zipfile.ZipFile(odp) as z:
        entries = {i.filename: z.read(i.filename) for i in z.infolist()}
    content = entries["content.xml"].decode("utf-8")
    it = iter(notes)

    def fill(m):
        lines = [l for l in next(it, "").splitlines() if l.strip()]
        paras = "".join(para(l) for l in lines)
        return f'presentation:class="notes"{m.group(1)}><draw:text-box>{paras}</draw:text-box>'

    content = re.sub(r'presentation:class="notes"([^>]*)><draw:text-box/>', fill, content)
    entries["content.xml"] = content.encode("utf-8")
    with zipfile.ZipFile(odp, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), entries.pop("mimetype"), zipfile.ZIP_STORED)
        for name, data in entries.items():
            z.writestr(name, data, zipfile.ZIP_DEFLATED)


def main():
    subprocess.run(["python3", os.path.join(HERE, "img", "gen_svgs.py")], check=True)
    env = dict(os.environ, PATH=SOFFICE_DIR + ":" + os.environ["PATH"])
    with tempfile.TemporaryDirectory() as tmp:
        pptx = os.path.join(tmp, NAME + ".pptx")
        subprocess.run(["marp", "--pptx", "--pptx-editable", "--allow-local-files",
                        NAME + ".md", "-o", pptx], cwd=HERE, env=env, check=True,
                       stdin=subprocess.DEVNULL)
        # eigenes Profil, damit eine offene LibreOffice-Instanz nicht stoert
        profile = "-env:UserInstallation=file://" + os.path.join(tmp, "lo-profile")
        subprocess.run([os.path.join(SOFFICE_DIR, "soffice"), profile, "--headless",
                        "--convert-to", "odp", "--outdir", tmp, pptx], check=True,
                       stdin=subprocess.DEVNULL)
        odp = os.path.join(tmp, NAME + ".odp")
        if not os.path.exists(odp):
            raise SystemExit("LibreOffice hat keine ODP erzeugt")
        with open(os.path.join(HERE, NAME + ".md"), encoding="utf-8") as f:
            notes = slide_notes(f.read())
        inject_notes(odp, notes)
        # erst am Ende ersetzen: ist die Datei in Impress offen, bleibt sonst der alte Stand liegen
        shutil.move(odp, os.path.join(HERE, NAME + ".odp"))
    print(f"{NAME}.odp erstellt, {len(notes)} Folien")


if __name__ == "__main__":
    main()
