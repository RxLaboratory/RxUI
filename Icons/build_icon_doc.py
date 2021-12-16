from pathlib import Path
from shutil import copy2
from os import mkdir

badgesDir = Path('1_Badges')
symbolsDir = Path('2_Symbols')

docs_badges_path = '../src-docs/docs/icons/1_Badges/'
docs_symbols_path = '../src-docs/docs/icons/2_Symbols/'
docs_icons_path = '../src-docs/docs/icons/3_Icons/'
badges_md = Path('../src-docs/docs/icons-badges.md')
icons_md = Path('../src-docs/docs/icons-list.md')

badges_content = """# Badges / Specific actions or states (verbs or adjectives)

!!! Note
    This list is auto-generated from existing badges, do not modify it.

A small badge may be added to the icon, showing specifically the triggered action, or changed state.

These are the proposed and most basic actions.

This list is evolutive, but the actions and states listed here must be general enough to be used and understood across different applications."""

small_badges = """
## Small Badges

These versions of the badges are made to be used with the small version of icons (between 18px and 32px).

| Icon | Action or state |
|---|---|"""

large_badges = """

## Large Badges

These versions of the badges are made to be used with the large version of icons or as icons themselves.

| Icon | Action or state |
|---|---|"""

def is_small(name):
    return name[-2] == 's'

def is_dark(name):
    return name[-1] == 'd'

for badge in badgesDir.iterdir():
    filename = badge.name
    name = filename.replace('.svg', '')
    if not is_dark(name): continue
    if is_small(name):
        name = name.replace('_sd', '')
        name = ' '.join(name.split('-')).title()
        print("Getting small badge: " + name)
        small_badges = small_badges + '\n| ![](icons/1_Badges/{0}){{: style="height:15px;width:15px"}} | {1} | '.format(filename, name)
        copy2(badge, docs_badges_path)
    else:
        name = name.replace('_bd', '')
        name = ' '.join(name.split('-')).title()
        print("Getting large badge: " + name)
        large_badges = large_badges + '\n| ![](icons/1_Badges/{0}){{: style="height:25px;width:25px"}} | {1} | '.format(filename, name)
        copy2(badge, docs_badges_path)

badges_content = badges_content + small_badges + large_badges
with badges_md.open('w'):
    badges_md.write_text(badges_content)

symbols_content = """# List of icons

!!! Note
    This list is auto-generated from existing symbols, do not modify it."""

small_symbols = """

## Standard"""

large_symbols = """

## Large"""

for symbol_group in symbolsDir.iterdir():
    group_name = symbol_group.name
    group_docs_path = docs_symbols_path + group_name + '/'
    try:
        mkdir(group_docs_path)
    except:
        print(group_docs_path + " already exists")
    group_md = """

### %s

| Icon | Name |
|---|---|"""%group_name

    small_symbols = small_symbols + group_md
    large_symbols = large_symbols + group_md

    for symbol in symbol_group.iterdir():
        filename = symbol.name
        name = filename.replace('.svg', '')
        if not is_dark(name): continue
        if is_small(name):
            name = name.replace('_sd', '')
            name = ' '.join(name.split('-')).title()
            small_symbols = small_symbols + '\n| ![](icons/2_Symbols/{0}/{1}){{: style="height:18px;width:18px"}} - ![](icons/2_Symbols/{0}/{1}){{: style="height:28px;width:28px"}} | {2} |'.format( group_name, filename, name)
            copy2(symbol, group_docs_path)
            print("Got small symbol: " + name)
        else:
            name = name.replace('_bd', '')
            name = ' '.join(name.split('-')).title()
            large_symbols = large_symbols + '\n| ![](icons/2_Symbols/{0}/{1}){{: style="height:32px;width:32px"}} - ![](icons/2_Symbols/{0}/{1}){{: style="height:48px;width:48px"}} | {2} |'.format( group_name, filename, name)
            copy2(symbol, group_docs_path)
            print("Got large symbol: " + name)

symbols_content = symbols_content + small_symbols + large_symbols
with icons_md.open('w'):
    icons_md.write_text(symbols_content)
