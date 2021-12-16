cd ../Icons/
python build_icon_doc.py
cd ../Colors/
python build_color_doc.py
cd ../src-docs/
mkdocs build
cd ../docs/
echo rxui-docs.rainboxlab.org > CNAME
