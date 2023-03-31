## Git configuration

$ git config --global user.name “Your Name”
Set the name that will be attached to your commits and tags.

$ git config --global user.email “you@example.com”
Set the e-mail address that will be attached to your commits and tags.


## Starting a project

$ git init 
Create a new local repository.

$ git clone [project url]
Downloads a project with the entire history from the remote repository.


## Day-To-Day Work

$ git status
Displays the status of your working directory. Options include new, 
staged, and modified files. It will retrieve branch name, current commit 
identifier, and changes pending commit.

$ git add [file]
Add a file to the staging area. Use in place of the full file path to add all 
changed files from the current directory down into the directory tree.

$ git diff [file]
Show changes between working directory and staging area.

$ git commit -m "message"
Create a new commit from changes added to the staging area. 


## Git branching model
$ git branch [-a]
List all local branches in repository. With -a: show all branches 
(with remote).

$ git branch [branch_name]
Create new branch, referencing the current HEAD.

$ git checkout [-b][branch_name]
Switch working directory to the specified branch. With -b: Git will 
create the specified branch if it does not exist.

$ git merge [from name]
Join specified [from name] branch into your current branch (the one 
you are on currently)


## Review your work

$ git log [-n count]
List commit history of current branch. -n count limits list to last n 
commits.

$ git log --oneline --graph --decorate
An overview with reference labels and history graph. One commit 
per line


## Synchronizing repositories

$ git fetch [remote]
Fetch changes from the remote, but not update tracking branches.

$ git pull [remote]
Fetch changes from the remote and merge current branch with its 
upstream.

$ git push [--tags] [remote]
Push local changes to the remote. Use --tags to push tags.

$ git push -u [remote] [branch]
Push local branch to remote repository. Set its copy as an upstream.