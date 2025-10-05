# CPES diagram
Cyber-Physical Energy Systems diagram drawing library.

The current version is work in progres, but ready for initial use. It is expected that 

## Setup
Before this icon set can be used, you need to download and convert the Material Design Symbols provided by Google to PDF format. For this we have provided a Python script.

#### Dependencies
The following software and libraries are required:

Software:
- python
- git

For Python, the following packages are required (install using e.g., pip):
- cairosvg

In latex, the following packages are required (please refer to the examples):
- tikz
- pgfplots
- transparency


#### Installation with docker
Docker is the most convenient way of installation, especially under Windows. This readme assumes you have Git and Docker intalled and running on your machine. We explain how to cloen the project and generate the icon sets from their sources. Start a terminal in your user folder, e.g., under Windows press start and search for "cmd" to open a terminal. Execute the following steps, the last step takes a long time due to the large icon set.

    git clone https://github.com/utwente-energy/cpesdiagram.git
	cd cpesdiag
	docker build -t cpesdiag .
	docker run docker run -v "C:\Users\<yourname>\cpesdiagram\cpesdiag\icons:/app/cpesdiag/icons" cpesdiag


#### Installation without docker
Please follow the following steps using the commandline from the root directory of this repository (we assume you have already cloned the project):

    git clone https://github.com/google/material-design-icons.git
    git clone https://github.com/Templarian/MaterialDesign
    python convertIcons.py

Note that Windows and Mac OS may require additional steps to make this Cairo SVG2PDFconverter work, so please read the CairoSVG documentation carefully. A Docker container to produce the pdf files is envisioned in future updates.

## Usage
To be written later. For now please refer to the provided examples, together with the following brief description.

The icons can be used by including.
    
    \input{cpesdiag/cpesdiag.tex}
    \importcpesstyle
    
Note that a greyscale version also exists:

    \importcpesstylegrey

The diagram library consists of nodes (styles) for Devices (which link parts together), Cyber (e.g., controllers), Physical (e.g., grid infrastructure), and Interaction (e.g., humans). For these, different types exist, namely one for use in a matrix composition, a coordinate system (denoted with an additional x), and for both also a dual variant (allowing for two icons to be used).

This package utilizes the icons as found in the Material Design set, which can be interactively viewed here: https://fonts.google.com/icons. One can copy the "icon name" (provided in the bottom right) to insert a specific icon. For this, use the form "mds:<icon name>" where mds is short for Material Design Symbol.


This package utilizes the icons as found in the Material Design Icons set by Pictogrammers, which can be interactively viewed here: https://pictogrammers.com/library/mdi/. One can copy the "icon name" (provided in the top of the pop-up window when selecting an icon) to insert a specific icon. For this, use the form "mdi:<icon name>" where mdi is short for Material Design Icon.


## License

This code is made available under the Apache version 2.0 license: https://www.apache.org/licenses/LICENSE-2.0 .

This library depends on external icon repositories:
- Google Material Symbols, available https://github.com/google/material-design-icons - Apache 2.0 License
- Material Design Icons, available https://github.com/Templarian/MaterialDesign - Various licenses

## Contact
In case you need assistance, please contact:

Gerwin Hoogsteen:
- https://people.utwente.nl/g.hoogsteen
- g.hoogsteen [at] utwente [dot] nl
- demgroup-eemcs [at] utwente [dot] nl
