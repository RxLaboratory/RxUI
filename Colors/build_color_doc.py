from pathlib import Path
from shutil import copy2
from os import mkdir

grayDir = Path('Grayscale')
specificDir = Path('Specific')
tintsDir = Path('Tints')

docs_grayscale_path = '../src-docs/docs/colors/Grayscale'
docs_specific_path = '../src-docs/docs/colors/Specific'
docs_tints_path = '../src-docs/docs/colors/Tints'

colors_md = Path('../src-docs/docs/colors.md')

colors_content = """# Rx Colors

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

tints = """

## Tints

| Color | Name | Hex |
| ---- | --------- | ------- |"""

for col in grayDir.iterdir():
    filename = col.name
    name = filename.replace('.svg', '').split('_')
    hexCode = name[0]
    name = name[1]
    name = ' '.join(name.split('-')).title()
    grayscale = grayscale + '\n| ![](colors/Grayscale/{0}){{: style="height:25px;width:25px"}} | {1} | #{2} |'.format(filename, name, hexCode)
    copy2(col, docs_grayscale_path)

for col in tintsDir.iterdir():
    filename = col.name
    name = filename.replace('.svg', '').split('_')
    hexCode = name[0]
    name = name[1]
    name = ' '.join(name.split('-')).title()
    tints = tints + '\n| ![](colors/Tints/{0}){{: style="height:25px;width:25px"}} | {1} | #{2} |'.format(filename, name, hexCode)
    copy2(col, docs_tints_path)
    
for col in specificDir.iterdir():
    filename = col.name
    name = filename.replace('.svg', '').split('_')
    hexCode = name[0]
    name = name[1]
    name = ' '.join(name.split('-')).title()
    specific = specific + '\n| ![](colors/Specific/{0}){{: style="height:25px;width:25px"}} | {1} | #{2} |'.format(filename, name, hexCode)
    copy2(col, docs_specific_path)

colors_content = colors_content + grayscale + tints + specific

with colors_md.open('w'):
    colors_md.write_text(colors_content)