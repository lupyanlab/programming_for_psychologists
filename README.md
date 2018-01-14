# Psych711: Programming for Psychologists

This repo contains a collection of IPython Notebooks for teaching Programming
to Psychology Grad Students at UW-Madison.

This project is based on [introtopython.org](http://introtopython.org), an open resource for teaching and learning Python created by Eric Matthes (thank you Eric!). If you think there are additional programming skills that are critical for Psych grad students to know, have examples of useful PsychoPy projects to develop experiment-design skills, and/or you have ideas for other relatedthat you want graduate students in Psychology/Cognitive Neuroscience programs to know, please contribute to the project by including additional Jupyter Notebooks.

You can view the raw notebooks using the Jupyter Notebook Viewer [(home page)](http://nbviewer.ipython.org/urls/raw.github.com/lupyanlab/programming_for_psychologists/master/notebooks/index.ipynb). The content is similar on both sites, but the [class](http://sapir.psych.wisc.edu/programming_for_psychologists/) version is easier to navigate and has some dynamic features such as collapsible Python output and a table of contents sidebar.


## Exercise repos

All exercise repos are linked to this repo as submodules. By default,
when this repo is cloned, the submodules will not be initialized or
updated. To clone all exercise repos to subdirs within the "assignments/"
directory, run the following git command.

```bash
git submodule update --init
```

When git updates submodules it points the submodule to a particular
commit within the repo. If you want to make changes and commit them,
you'll need to check out the master branch. To check out the master
branch on all submodules, run the following git command.

```bash
git submodule foreach git checkout master
```

## Install

```bash
# Recommended: Install the required packages in a virtual environment
pip2 install virtualenv
virtualenv ~/.venvs/psych711
source ~/.venvs/psych711/bin/activate

# Install the required python packages
pip install -r requirements.txt

# Download html/css/js for nbextensions
# https://github.com/ipython-contrib/jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Setup the nbextension browser interface
# https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator 
jupyter nbextensions_configurator enable --user
```

## Build the HTML pages
```
cd scripts
./build_html_pages.sh
```

