#!/usr/bin/sh

git clone https://github.com/google/material-design-icons.git
git clone https://github.com/Templarian/MaterialDesign.git
python3 convertIcons.py
rm -rf material-design-icons
rm -rf MaterialDesign