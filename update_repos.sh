#!/bin/sh

checkout_path="./checkout"

mkdir -p $checkout_path

for repo in $(cat repository_list.txt);
do
  if [ -d $checkout_path/$repo ]; then
    cd $checkout_path/$repo
    git pull
    cd ../..
  else
    cd $checkout_path
    git clone git://anongit.kde.org/$repo.git
    cd ..
  fi
done
