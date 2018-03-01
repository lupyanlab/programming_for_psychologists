# Notes on git submodules

In the main website repo, the remote named "origin" is linked to github.com/lupyanlab/programming_for_psychologists.

```
programming_for_psychologists/$ pwd
/Users/pierce/Teaching/programming_for_psychologists
programming_for_psychologists/$ git remote -v
origin	https://github.com/lupyanlab/programming_for_psychologists (fetch)
origin	https://github.com/lupyanlab/programming_for_psychologists (push)
```

Now move to one of the submodule directories. The submodule directory is it's own git repo with it's own .git/ database. This one is linked to github.com/programming-for-psychologists/project1.

```
programming_for_psychologists/$ cd projects/project1
project1/$ ls -la
total 0
drwxr-xr-x   5 pierce  staff  170 Mar  1 09:28 .
drwxr-xr-x   3 pierce  staff  102 Mar  1 09:23 ..
drwxr-xr-x  12 pierce  staff  408 Mar  1 10:15 .git
drwxr-xr-x   6 pierce  staff  204 Mar  1 09:28 memory
drwxr-xr-x   4 pierce  staff  136 Mar  1 09:28 reinforcement_learning
project1/$ git remote -v
origin	https://github.com/programming-for-psychologists/project1.git (fetch)
origin	https://github.com/programming-for-psychologists/project1.git (push)
```

You might find that when you move to the submodule directory, there is nothing in it. Strangely, the remote still points to the parent repo, and not the submodule repo.

```
programming_for_psychologists/$ cd projects/project1/
project1/$ ls
# empty!
project1/$ git remote -v
origin	git@github.com:lupyanlab/programming_for_psychologists (fetch)
origin	git@github.com:lupyanlab/programming_for_psychologists (push)
# strange! should be https://github.com/programming-for-psychologists/project1.git
```

To fix this, you need to run `git submodule init` and `git submodule update`.

```
project1/$ git submodule init .
Submodule 'projects/project1' (https://github.com/programming-for-psychologists/project1.git) registered for path './'
project1/$ git submodule update .
Cloning into '/Users/pierce/Teaching/programming_for_psychologists/projects/project1'...
Submodule path './': checked out 'd97c370132793dffcb1714e1e12532dde39213d7'
project1/$ ls
memory			reinforcement_learning
project1/$ git remote -v
origin	https://github.com/programming-for-psychologists/project1.git (fetch)
origin	https://github.com/programming-for-psychologists/project1.git (push)
```
