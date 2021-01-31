#!/bin/bash

palettes_path=~/.config/inkscape/palettes

palettes=../Colors/palettes/
icons=../Icons/

# convert to absolute paths
palettes=$(cd "$palettes"; pwd)
icons=$(cd "$icons"; pwd)

for file in $palettes/*.gpl; do
    rm -f "$palettes_path/$file"
    ln -s -t "$palettes_path" "$file"
    echo "Linked $file"
done

for file in $icons/*.gpl; do
    rm -f "$palettes_path/$file"
    ln -s -t "$palettes_path" "$file"
    echo "Linked $file"
done

echo "Done!"