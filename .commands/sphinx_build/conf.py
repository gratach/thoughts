import sys, os

sys.path.append(os.path.abspath('sphinxext'))

project = 'Thoughts'
author = 'Patrick Richter'

extensions = ['myst_parser']
myst_enable_extensions = [
    "html_image",
]
templates_path = ['.templates']

html_theme = 'agogo'

html_sidebars = {
   '**': ['globaltoc.html']
}

source_suffix = ['.rst', '.md']