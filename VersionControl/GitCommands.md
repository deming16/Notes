# Git Commands
[index](/index.md)

## CREATE REPOSITORIES
Creates a new local repository with the specified name <br />
`git init [project-name]`
Downloads a project and its entire version history <br />
`git clone [url]`

## Configure Tooling
1. Set name to attach to commit transactions <br />
`git config --global user.name "[name]"`
1. Sets email to attached to commit transactions <br />
`git config --global user.email "[email address]"`
1. Enables helpful colorization of command line output <br/>
`git config --global color.ui auto`

## Stashing
1. Stash all tracked files <br/>
`git stash push`
1. Pop the most recently stashed files <br/>
`git stash pop`
1. List all stashed files <br/>
`git stash list`
1. Discard the most recently stashed changeset <br/>
`git stash drop`
