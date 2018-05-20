# Static Config
mgmtdir="/home/git/repo-management"

# Grab our input
reponame="$1"
urlpath="git.kde.org-$2"

# Build the remote URL up
remoteurl="git@github.com:WikiToLearn/$reponame"
# Make sure the repo exists on Github
python ./create-on-github.py "$reponame" "/srv/git/repositories/$urlpath"
# Now we push it up there
python ./update-repo-mirror.py "$reponame" "$remoteurl"
