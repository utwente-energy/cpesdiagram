#!/usr/bin/python3

# Copyright 2025 University of Twente
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Tool to convert Google's Material Design Symbols into PDF format for use in LaTeX documents

import os
import cairosvg


# ==== Settings ====

# == Input ==

# Input directory of the icons
indir = "material-design-icons/symbols/web/"

# Icon style as listed on https://fonts.google.com/icons?icon.query=circles&icon.set=Material+Symbols&icon.size=24&icon.color=%231f1f1f
icons_style = "materialsymbolsoutlined"
icons_style_fill = "materialsymbolsoutlined"

# Optical size in pixels
icon_size = "48"
icon_size_fill = "48"

# Weight
icon_weight = ""
icon_weight_fill = "wght600"

# Grade
icon_grade = ""
icon_grade_fill = ""

# Add a stroke
# use an empty string to avoid adding a stroke

# Apply stroke to plain icons
stroke = ''

# Apply stroke for filled icon
stroke_fill = 'stroke="white" stroke-width="24"'




# == Output ==

# Output directory of the icons
outdir = "cpesdiag/icons"





# ==== Functions ====

# Decorator to add a stroke to the svg
def add_stroke(filename, stroke):
    # Read the file
    fin = open(filename, 'r')
    text = fin.read()
    fin.close()

    # Add the stroke
    text = text.replace("<path", "<path "+stroke)

    # Write the new output file
    filename = filename[:-4]+"_stroke.svg"
    fout = open(filename, 'w')
    fout.write(text)
    fout.close()

    # Return the new name for processing
    return filename




# ==== Execution ====

# Make sure the folders exist
os.makedirs(outdir+"/plain", exist_ok = True)
os.makedirs(outdir+"/fill", exist_ok = True)


# Process all the icons one by one
subfolders= os.listdir(indir)
for iconname in subfolders:
    print("processing "+iconname)

    # First process the plain icon

    # Extract the icon name and location
    icon = iconname + "_" + icon_weight + icon_grade + "_" + icon_size + "px.svg"
    icon = icon.replace("__", "_")  # remove double underscore
    filename = indir+iconname+"/"+icons_style+"/"+icon

    if stroke != "":
        filename = add_stroke(filename, stroke)

    # Convert to pdf
    cairosvg.svg2pdf(url=filename, write_to=outdir+"/plain/mds:"+iconname+".pdf")



    # Next do the same with the filled version

    # Extract the icon name and location
    icon = iconname + "_" + icon_weight_fill + icon_grade_fill + "fill1_" + icon_size_fill + "px.svg"
    icon = icon.replace("__", "_")  # remove double underscore
    filename = indir+iconname+"/"+icons_style_fill+"/"+icon

    if stroke_fill != "":
        filename = add_stroke(filename, stroke_fill)

    # Convert to pdf
    cairosvg.svg2pdf(url=filename, write_to=outdir+"/fill/mds:"+iconname+".pdf")
