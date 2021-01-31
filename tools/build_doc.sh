#!/bin/bash
cd ../src-docs/
mkdocs build
echo "rxui-docs.rainboxlab.org" > ../docs/CNAME
