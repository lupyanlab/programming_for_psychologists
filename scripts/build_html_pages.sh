#!/bin/bash

# This script builds the entire html page.
#  Assumes need to build from basic html, and construct custom-defined pages.
#
# When starting out, need to run a full nbconvert, and then pull out css and js
#  files into 'css' and 'js' directories, in the 'notebooks' dir. This is manual
#  right now, but it would be good to automate this and create a flag such as 
#  '--initial'.
#
# Core of script involves running
#    'jupyter nbconvert --template intro_python_base.tpl'
#   Then adds appropriate sections through other templates, and scripting.
#     Also modifies some styles for better static html output.
#   Script is meant to be fairly straightforward to modify, so users can 
#   build the static pages they care to make from the core notebooks.
#
# This is meant to work well through a post-commit-hook, although you can also
#  run the script manually when you want a snapshot of the notebooks in html
#  format.
#
# All html files are ignored by git.


if [ -e scripts/ ]
then
	 # Probably running as a commit hook.
    path_to_scripts="scripts/"
	 path_to_notebooks="notebooks/"
else
	 # Probably running directly from /scripts directory.
	 path_to_scripts=""
	 path_to_notebooks="../notebooks/"
fi
printf "\npath to scripts: $path_to_scripts"
printf "\npath to notebooks: $path_to_notebooks\n"

# Build basic pages.
source "$path_to_scripts"create_common_html.sh
wait


# Add elements to toggle output on each page.
printf "Adding ability to toggle output on each page...\n"
python "$prefix"show_hide_output.py
wait
printf "  Added toggling ability.\n\n"

# Convert index.html links to ./
source "$prefix"convert_home_links.sh
wait

# Highlight lines of code.
python "$prefix"highlight_code.py
wait

# Highlight inline blocks of code.
source "$prefix"highlight_inline_code.sh
wait

# Strip input references from code cells.
python "$prefix"remove_input_references.py
wait

# Build index page.
# printf "\nBuilding index page...\n"
# python "$prefix"build_index.py
# wait
# printf "  Built index page.\n"

#  Build all exercises page.
# DEV: Holding off on this until project is more mature,
#        but don't want to lose sight of it.
#python "$prefix"build_all_exercises_page.py
#wait

printf "  Substituting link pointers in the index page.\n"
sed -i -e 's/src="js\//src="notebooks\/js\//g' "$path_to_notebooks"/index.html
sed -i -e 's/href="css/href="notebooks\/css/g' "$path_to_notebooks"/index.html
sed -i -e 's/href="css/href="notebooks\/css/g' "$path_to_notebooks"/index.html
sed -i -e 's/<li><a href="/<li><a href="notebooks\//g' "$path_to_notebooks"/index.html


printf "  Move index page to root\n"
mv "$path_to_notebooks"/index.html ../
