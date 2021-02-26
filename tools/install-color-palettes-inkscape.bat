:: Edit these variables with the correct paths on your system (you should just have to change your username)
SET inkscapePalettesPath=C:\Users\Duduf\AppData\Roaming\inkscape\palettes
:: Set this variable to the repo
SET repo=F:\DEV_SRC\RxOT\RxUI

SET palettes=%repo%\Colors\palettes
SET icons=%repo%\Icons

:: Need admin to create symlinks
@echo off
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
:: Get back to original dir
pushd "%CD%"
CD /D "%~dp0"

echo Relative path: %palettes%
echo Maps to path: %ABS_PATH%

:: Links
mklink "%inkscapePalettesPath%\RxUI-Grayscale.gpl" "%palettes%\RxUI-Grayscale.gpl"
mklink "%inkscapePalettesPath%\RxUI-Specific.gpl" "%palettes%\RxUI-Specific.gpl"
mklink "%inkscapePalettesPath%\RxUI-Tints.gpl" "%palettes%\RxUI-Tints.gpl"
mklink "%inkscapePalettesPath%\RxUI-Icons.gpl" "%icons%\RxUI-Icons.gpl"

PAUSE