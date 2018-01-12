# Psych711: Programming for Psychologists

This repo contains a collection of IPython Notebooks for teaching Programming
to Psychology Grad Students at UW-Madison.
=======
A collection of Jupyter Notebooks for teaching Programming to Psychology Grad Students at UW-Madison.
---

This project is based on [introtopython.org](http://introtopython.org), an open resource for teaching and learning Python created by Eric Matthes (thank you Eric!). If you think there are additional programming skills that are critical for Psych grad students to know, have examples of useful PsychoPy projects to develop experiment-design skills, and/or you have ideas for other relatedthat you want graduate students in Psychology/Cognitive Neuroscience programs to know, please contribute to the project by including additional Jupyter Notebooks.

You can view the raw notebooks using the Jupyter Notebook Viewer [(home page)](http://nbviewer.ipython.org/urls/raw.github.com/lupyanlab/programming_for_psychologists/master/notebooks/index.ipynb). The content is similar on both sites, but the [class](http://sapir.psych.wisc.edu/programming_for_psychologists/) version is easier to navigate and has some dynamic features such as collapsible Python output and a table of contents sidebar.

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

