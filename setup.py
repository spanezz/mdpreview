#!/usr/bin/env python3

from distutils.core import setup
import sys

setup(
    name = "mdpreview",
    requires=[ 'markdown', 'jinja2', 'livereload' ],
    version = "0.1",
    description = "Preview a Markdown file while you edit it",
    author = ["Enrico Zini"],
    author_email = ["enrico@enricozini.org"],
    url = "https://github.com/spanezz/mdpreview",
    license = "http://www.gnu.org/licenses/gpl-3.0.html",
    scripts = ['mdpreview']
)
