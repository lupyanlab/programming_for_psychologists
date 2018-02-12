# Psych711: Programming for Psychologists

This repo contains a collection of IPython Notebooks for teaching Programming
to Psychology Grad Students at UW-Madison.

This project is based on [introtopython.org](http://introtopython.org), an open resource for teaching and learning Python created by Eric Matthes (thank you Eric!). If you think there are additional programming skills that are critical for Psych grad students to know, have examples of useful PsychoPy projects to develop experiment-design skills, and/or you have ideas for other relatedthat you want graduate students in Psychology/Cognitive Neuroscience programs to know, please contribute to the project by including additional Jupyter Notebooks.

You can view the raw notebooks using the Jupyter Notebook Viewer [(home page)](http://nbviewer.ipython.org/urls/raw.github.com/lupyanlab/programming_for_psychologists/master/notebooks/index.ipynb). The content is similar on both sites, but the [class](http://sapir.psych.wisc.edu/programming_for_psychologists/) version is easier to navigate and has some dynamic features such as collapsible Python output and a table of contents sidebar.

## Creating a Github Classroom assignment

Here are the steps for creating a new Github Classroom assignment.

1. (Optional) Create a new repo on Github. This repo will be used as the "base" repo that all students will receive when they start on this assignment. For example, [github.com/programming-for-psychologists/exercise-1](https://github.com/programming-for-psychologists/exercise-1) was created as the base repo for Exercise 1. If you do not create a new repo, you can still make the assignment, but all students will start off with an empty repo.
1. Create the Github Classroom Assignment. Go to the Classroom page for the Programming for Psychologists classroom [here](https://classroom.github.com/classrooms/35153597-programming-for-psychologists). Select "New assignment". Give the assignment a title and a repository prefix. For Exercise 1, both the title and the repository prefix were "exercise-1". In the question for "Add your starter code", find the repo you created above. Then select "Create Assignment".
1. After you have created the assignment, you receive a link to distribute to everyone in the class. When they click on this link, they will be prompted to sign in to Github.com, and it will create a clone of the base repo for their use.

### Debugging Github Classroom

Occasionally a student will get stuck on the "import" page, after clicking on the link. When this happens, they often have a repo created on Github.com (e.g., https://github.com/programming-for-psychologists/exercise-1-pedmiston), but it may be empty.

To fix this issue, first clone the student's empty repo, then fill it with the correct exercise files, then push those new files to their remote repo on Github.

These steps are summarized in a simple bash script, `bin/populate-exercise`. Use it like this:

```bash
bin/populate-exercise pedmiston exercise-1
# Clones github.com/programming-for-psychologists/exercise-1-pedmiston.
# Then moves files from ./assignments/exercise-1/* into the repo.
# Then pushes the new files to Github.com
```


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

### Updating files in exercise submodules

```bash
# Copies notebooks/Exercise1-square.ipynb to assignments/exercise-1/
bin/cp-notebook-to-exercise Exercise1-square.ipynb exercise-1
```

## Install

```bash
# Recommended: Install the required packages in a virtual environment
conda create -n psychopy python=2
source activate psychopy

# Install the required python packages
pip install -r requirements.txt

# Download html/css/js for nbextensions
# https://github.com/ipython-contrib/jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Setup the nbextension browser interface
# https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
```

### Running R in jupyter notebooks

To run R in jupyter notebooks, first install an R kernel to the conda environment.

```bash
# Install an R kernel in the conda environment
conda install --channel r r-irkernel
```

Then install the required R packages.

```R
install.packages("devtools")
devtools::install_github("IRkernel/IRkernel")
IRkernel::installspec()
```

## Build the HTML pages
```
cd scripts
./build_html_pages.sh
```

