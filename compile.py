import os
import re
import datetime
from io import open

with open('src/index.html', "r", encoding="utf-8") as f:
    page = f.read()
# Script tags

scriptsFinder = re.compile("""<script src="(.*)"></script>""")
scripts = scriptsFinder.findall(page)

for script in scripts:
    filename = os.path.join("src", script)
    with open(filename, "r", encoding="utf-8") as s:
        scriptContent = f"<script>{s.read()}</script>"
    scriptTag = f"""<script src="{script}"></script>"""
    page = page.replace(scriptTag, scriptContent)


# Style tags

stylesFinder = re.compile("""<link rel="stylesheet" href="(.*)">""")
styles = stylesFinder.findall(page)

for style in styles:
    filename = os.path.join("src", style)
    with open(filename, "r", encoding="utf-8") as s:
        styleContent = f"<style>{s.read()}</style>"
    styleTag = f"""<link rel="stylesheet" href="{style}">"""
    page = page.replace(styleTag, styleContent)


with open('bip39-standalone.html', 'w', encoding="utf-8") as f:
    f.write(page)
print(f"{datetime.datetime.now()} - DONE")
