#!/bin/bash

cd ../Icons/
/usr/bin/python3 build_icon_doc.py
cd ../Colors/
/usr/bin/python3 build_color_doc.py
cd ../src-docs/
mkdocs build
cd ../docs/
echo rxui-docs.rainboxlab.org > CNAME
