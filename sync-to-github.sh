# Static Config
mgmtdir="/home/git/repo-management"

for repo in $(cat repository_list.txt);
do
  # Grab our input
  reponame="$repo"
  urlpath="git.kde.org-$2"

  # Build the remote URL up
  remoteurl="git@github.com:WikiToLearn/$reponame"
  # Make sure the repo exists on Github
  python ./create-on-github.py "$reponame" "./checkout/$urlpath"
  # Now we push it up there
  python ./update-repo-mirror.py "$reponame" "$remoteurl"
done
