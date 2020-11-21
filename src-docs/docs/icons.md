# Icons

[TOC]

## Introduction

We're proposing here some guidelines to build icons based on our experience with software development and UI design, and most of all our comitment to make our software as intuitive and user-friendly as possible, as well as accessible to most people.

!!! Hint
    All of this document and these thoughts are evolutive. Also, we're not omniscient, and you have your own thoughts and experience; we would be very happy if you would share them and contribute to this document, these guidelines, these list, and these icons. Together, we could make sure all our software is the best we can imagine.

### User-friendliness

This is the most important aspect of our UI and icons. This means that after a short period of getting used to them, the user is as quick as possible using the software, which UI is unobtrusive.

- The UI and the icons must let as much as possible room to the actual work of the user (text, image, media...)
- The UI must be as discreet as possible, and let the user's work area stand out.

That means the icons has to be as small as possible while keeping readiness, and not being too difficult to click-on.

They also must be constrasting enough, with other icons and with the rest of the application, to be recognizable as fast as possible.

### Accessible

Not all users have the same way of seeing the icons. Some may be colorblind, some may have visual defficiencies. The default icons have to be as contrasted as possible, and use all tools available to help everyone differentiate them: colors, shapes, sizes.

This also means that the UI and the icons should be scalable, and it should also be possible to change the contrast (without having to manually define all colors)

Of course this may be a lot of work, especially for free software - we strongly believe it should be a priority of paid and proprietary software to build accessible UI for everyone - so the main focus may be to first build a working UI and icons following these guidelines, but it must be still easy enough for anyone to modify them and add the ability to edit them to make them more accessible. At least, the software should give access to its stylesheets and make it easy to change the one which is used, and also the source (SVG) of the icons and a way to change them too. Of course, help is always welcome for every free software!

### Intuitiveness

To help the user get used to the software, its UI and icons, they must be as intuitive as possible. This means that there should be as little as possible things to learn, and the signification of as much as possible items should be easily deducible.

We propose to base the icons on a set of predefined symbols, used across applications and tools, so that the user do not have to re-learn everything. Specific icons should use a subset and variations of the base symbols and a combination of basic visual elements (colors, shapes, badges...) to make it easy to deduce what they're symbolizing.

That being said, intuitiveness must come after user-friendliness as we believe it is more important that the software does not get in the way of the work of the user. Most of the time, it is preferrable to have software which takes a bit of time to learn but be quick to use it then, than a software which can be used as soon as it is installed but make the work slower.

Of course, this last thought has to be reconsidered for software not used very often, specific tools which are going to be used only once in a while; in which case these guidelines may not apply in their entirety and it may be interesting to write a variation of these for this specific case.

### Do not reinvent the wheel!

We're not the first to draw icons. Inspiration should be taken from other Free and Open Source project, and when applicable, it is both useful and recommended to re-use existing free and open source icons, and contribute back to the free project where they're from.

We especially admire the work of [fontawesome](https://github.com/FortAwesome/Font-Awesome).

## General guidelines

- Monochrome
- Solid, no strokes
- All have a small/normal version working at 18px width, and which may still work at 15px width
- May have a large version more suited for 32px+ width
- Square SVG files

Icons are built by combining **a color** symbolizing what they're doing, one or two **symbols** symbolizing the objects involved, and possibly **a badge** showing the action.

## Colors / General Actions

The color of the icon should show its goal, i.e. what it's going to do, generally speaking.

Each one of them must be available in two shades, for use on a light or dark background. They must be contrasting with the background and with the other colors, and be as distinguishable as possible to colorblind people.

This list is evolutive, but the general actions listed here must be very general, and the list has to be small enough to be able to differentiate the actions.

It may be possible to use shades of these main colors to introduce more nuances. These nuances may be listed here in the future.

### Light

For use on dark backgrounds

| Color | Hex Code | Name | Description |
|---|---|---|---|
| ![](icons/0_Colors/neutral_l.svg) | | Neutral | Application specific color |
| ![](icons/0_Colors/creation_l.svg) | #8ad891 | Creation | Adds something new |
| ![](icons/0_Colors/modification_l.svg) | #d588f1 | Modification | Modifies existing objects |
| ![](icons/0_Colors/deletion_l.svg) | #f96969 | Deletion | Removes something |
| ![](icons/0_Colors/settings_l.svg) | #83d3f6 | Settings | Changes further behavior |

### Dark

For use on light backgrounds

| Color | Hex Code | Name | Description |
|---|---|---|---|
| ![](icons/0_Colors/neutral_d.svg) | | Neutral | Application specific color |
| ![](icons/0_Colors/creation_d.svg) | #3e8b45 | Creation | Adds something new |
| ![](icons/0_Colors/modification_d.svg) | #8109ad | Modification | Modifies existing objects |
| ![](icons/0_Colors/deletion_d.svg) | #f96969 | Deletion | Removes something |
| ![](icons/0_Colors/settings_d.svg) | #10688e | Settings | Changes further behavior |

## Badges / Specific actions or states

A small badge may be added to the icon, showing specifically the triggered action, or changed state.

These are the proposed and most basic actions.

This list is evolutive, but the actions and states listed here must be general enough to be used and understood across different applications.

### Small Badges

These versions of the badges are made to be used with the small version of icons (between 18px and 32px).

| Icon | Action or state | Corresponding color |
|---|---|---|
| ![](icons/1_Badges/add_sd.svg) | Add | Creation | 
| ![](icons/1_Badges/remove_sd.svg) | Remove | Deletion | 
| ![](icons/1_Badges/edit_sd.svg) | Edit | Modification | 
| ![](icons/1_Badges/import_sd.svg) | Import | Creation or Modification | 
| ![](icons/1_Badges/export_sd.svg) | Export | Creation | 
| ![](icons/1_Badges/new_sd.svg) | New/Create | Creation |
| ![](icons/1_Badges/load_sd.svg) | Load/Open | Creation | 
| ![](icons/1_Badges/reload_sd.svg) | Reload/Refresh | Modification | 
| ![](icons/1_Badges/save_sd.svg) | Save | Modification | 
| ![](icons/1_Badges/saveas_sd.svg) | Save As | Creation | 
| | Download | Creation | 
| | Upload | Creation | 
| | Lock(ed) | Settings | 
| | Unock(ed) | Settings | 
| | Select(ed) | Settings | 
| | Deselect(ed) | Settings | 
| | Show | Settings or Modification | 
| | Hide | Settings or Modification | 

### Large Badges

These versions of the badges are made to be used with the large version of icons or as icons themselves.

| Icon | Action or state | Corresponding color |
|---|---|---|
| ![](icons/1_Badges/add_bd.svg) | Add | Creation | 
| ![](icons/1_Badges/remove_bd.svg) | Remove | Deletion | 
| ![](icons/1_Badges/edit_bd.svg) | Edit | Modification | 
| ![](icons/1_Badges/import_bd.svg) | Import | Creation or Modification | 
| ![](icons/1_Badges/export_bd.svg) | Export | Creation | 
| ![](icons/1_Badges/new_bd.svg) | New/Create | Creation |
| ![](icons/1_Badges/load_bd.svg) | Load/Open | Creation | 
| ![](icons/1_Badges/reload_bd.svg) | Reload/Refresh | Modification | 
| ![](icons/1_Badges/save_bd.svg) | Save | Modification | 
| ![](icons/1_Badges/saveas_bd.svg) | Save As | Creation | 
| | Download | Creation | 
| | Upload | Creation | 
| | Lock(ed) | Settings | 
| | Unock(ed) | Settings | 
| | Select(ed) | Settings | 
| | Deselect(ed) | Settings | 
| | Show | Settings or Modification | 
| | Hide | Settings or Modification | 

## Base Objects / Abstract Symbols

The main symbol in the icon should show the object it is manipulating. The icon could possibly combine two of them.

[Here is the list of the symbols we propose](icons-symbols.md)

## Icon List

We've already built, and are building, icons to be used in our - and your - software, based on these guidelines and existing symbols, badges and colors.

[Here is the list of these icons](icons-list.md)
