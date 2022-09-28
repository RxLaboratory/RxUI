magick.exe convert -size 16x16 -background transparent -depth 8 ramses-icon-small.svg ramses_16.png
magick.exe convert -size 24x24 -background transparent -depth 8 ramses-icon-small.svg ramses_24.png
magick.exe convert -size 32x32 -background transparent -depth 8 ramses-icon-small.svg ramses_32.png
magick.exe convert -size 48x48 -background transparent -depth 8 ramses-icon-small.svg ramses_48.png
magick.exe convert -size 64x64 -background transparent -depth 8 ramses-icon-small.svg ramses_64.png
magick.exe convert -size 128x128 -background transparent -depth 8 ramses-icon-medium.svg ramses_128.png
magick.exe convert -size 256x256 -background transparent -depth 8 ramses-icon-medium.svg ramses_256.png
magick.exe convert -size 512x512 -background transparent -depth 8 ramses-icon-medium.svg ramses_512.png

magick.exe convert ramses_16.png ramses_24.png ramses_32.png ramses_48.png ramses_64.png ramses_256.png ramses_512.png -compress jpeg ramses.ico