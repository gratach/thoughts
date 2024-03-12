import sys, os

sys.path.append(os.path.abspath('sphinxext'))

extensions = ['myst_parser']
myst_enable_extensions = [
    "html_image",
]
