from pathlib import Path
from shutil import copy2
from os import mkdir

grayDir = Path('Grayscale')
specificDir = Path('Specific')
darkTintsDir = Path('Tints/Dark')
lightTintsDir = Path('Tints/Light')

docs_grayscale_path = '../src-docs/docs/colors/Grayscale'
docs_specific_path = '../src-docs/docs/colors/Specific'
docs_dark_tints_path = '../src-docs/docs/colors/Tints/Dark'
docs_light_tints_path = '../src-docs/docs/colors/Tints/Light'

colors_md = Path('../src-docs/docs/colors.md')

palette_grayscale = Path('palettes/RxUI-Grayscale.gpl')
palette_tints = Path('palettes/RxUI-Tints.gpl')
palette_specific = Path('palettes/RxUI-Specific.gpl')

def hexToRGB(hexCode):
    hexCode = hexCode.replace("#","")
    r = hexCode[0:2]
    g = hexCode[2:4]
    b = hexCode[4:6]
    r = str(int(r, 16))
    g = str(int(g, 16))
    b = str(int(b, 16))
    while (len(r) < 3): r = " "+r
    while (len(g) < 3): g = " "+g
    while (len(b) < 3): b = " "+b
    return r+" "+g+" "+b

gimp_palette_specific = """GIMP Palette
Name: RxUI Specific
#
"""

gimp_palette_grayscale = """GIMP Palette
Name: RxUI Grayscale
#
"""

gimp_palette_tints = """GIMP Palette
Name: RxUI Tints
#
"""

colors_content = """# Rx Colors

!!! note
    This document is automatically generated from the list of colors. Do not modify it.

These colors are to be used across all *Rx Open Tools*.

"""

grayscale = """## Grayscale

| Color | Name | Hex |
| ---- | --------- | ------- |"""

specific = """

## Specific colors

These colors are not part of the colors which should be used by *RxOT*, but they may be useful for intergration into host platforms.

| Color | Name | Hex |
| ---- | ------- | ----------- |"""

darkTints = """

## Tints

Some of these tints have a specific meaning, especially when used with icons. See the [icon color](icons-colors.md) section for more information and a list of those.

### Dark tints

Darker tints are to be used on lighter backgrounds (Lightness > 50%).

| Color | Name | Hex |
| ---- | --------- | ------- |"""

lightTints = """

### Light tints

Lighter tints are to be used on darker backgrounds (Lightness < 50%).

| Color | Name | Hex |
| ---- | --------- | ------- |"""

for col in grayDir.iterdir():
    filename = col.name
    name = filename.replace('.svg', '').split('_')
    hexCode = name[0]
    name = name[1]
    name = ' '.join(name.split('-')).title()
    gimp_palette_grayscale = gimp_palette_grayscale + hexToRGB(hexCode) + "\t" + name + "\n"
    grayscale = grayscale + '\n| ![](colors/Grayscale/{0}){{: style="height:25px;width:25px"}} | {1} | #{2} |'.format(filename, name, hexCode)
    copy2(col, docs_grayscale_path)

for col in darkTintsDir.iterdir():
    filename = col.name
    name = filename.replace('.svg', '').split('_')
    hexCode = name[0]
    name = name[1]
    name = ' '.join(name.split('-')).title()
    gimp_palette_tints = gimp_palette_tints + hexToRGB(hexCode) + "\t" + name + "\n"
    darkTints = darkTints + '\n| ![](colors/Tints/Dark/{0}){{: style="height:25px;width:25px"}} | {1} | #{2} |'.format(filename, name, hexCode)
    copy2(col, docs_dark_tints_path)
    
for col in lightTintsDir.iterdir():
    filename = col.name
    name = filename.replace('.svg', '').split('_')
    hexCode = name[0]
    name = name[1]
    name = ' '.join(name.split('-')).title()
    gimp_palette_tints = gimp_palette_tints + hexToRGB(hexCode) + "\t" + name + "\n"
    lightTints = lightTints + '\n| ![](colors/Tints/Light/{0}){{: style="height:25px;width:25px"}} | {1} | #{2} |'.format(filename, name, hexCode)
    copy2(col, docs_light_tints_path)

for col in specificDir.iterdir():
    filename = col.name
    name = filename.replace('.svg', '').split('_')
    hexCode = name[0]
    name = name[1]
    name = ' '.join(name.split('-')).title()
    gimp_palette_specific = gimp_palette_specific + hexToRGB(hexCode) + "\t" + name + "\n"
    specific = specific + '\n| ![](colors/Specific/{0}){{: style="height:25px;width:25px"}} | {1} | #{2} |'.format(filename, name, hexCode)
    copy2(col, docs_specific_path)

colors_content = colors_content + grayscale + darkTints + lightTints + specific

with colors_md.open('w'):
    colors_md.write_text(colors_content)

with palette_grayscale.open('w'):
    palette_grayscale.write_text(gimp_palette_grayscale)

with palette_specific.open('w'):
    palette_specific.write_text(gimp_palette_specific)

with palette_tints.open('w'):
    palette_tints.write_text(gimp_palette_tints)