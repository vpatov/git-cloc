Usage: python3 gitclocl.py <path/to/git/directory>

![](gifs/gitclocdemo.gif)

Git-cloc is very simple: It goes through the git log of the repo, checks out each commit starting from the present (ending at the first commit), and calls cloc to count the lines of code in that commit. It does not use git diff - it naively counts all the lines of code in every commit (not including whitespace and comments), and prints it out in a pretty format.

