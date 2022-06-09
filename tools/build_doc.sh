#!/bin/bash
cd ../src-docs/
mkdocs build
echo "rxui.rxlab.io" > ../docs/CNAME
