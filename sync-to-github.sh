# Static Config

for repo in $(cat repository_list.txt);
do
  # Grab our input
  reponame="$repo"
  urlpath="$repo"

  # Build the remote URL up
  remoteurl="git@github.com:WikiToLearn/$reponame"
  # Make sure the repo exists on Github
  python ./create-on-github.py "$reponame" "./checkout/$urlpath"

  cd "./checkout/$reponame"
  # Now we push it up there
  python ../../update-repo-mirror.py "$remoteurl"
  cd ../..
done
