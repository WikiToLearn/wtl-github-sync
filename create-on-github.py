#!/usr/bin/python2
#
# (C) Copyright 2015, Boudhayan Gupta <bgupta@kde.org>
# No rights reserved. This file is public domain

import os
import sys
import requests

try:
    import simplejson as json
except ImportError:
    import json

# Load our configuration
ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
ORGANISATION = "WikiToLearn"

# Get the repository name we'll be working with, and the path to the repository (locally)
REPO_NAME = sys.argv[1]
REPO_PATH = sys.argv[2]

# Set a default description
REPO_DESC = "This repository an automated mirror of git.kde.org. Join us on https://t.me/WikiToLearn"

# Load the description from the path
descriptionFile = REPO_PATH + "/description"

if os.path.exists(descriptionFile):
    REPO_DESC = open( REPO_PATH + "/description", "r").read().strip()

# Set up the requests session
S = requests.Session()
S.headers.update({"Accept": "application/vnd.github.v3+json"})
S.headers.update({"Authorization": " ".join(("token", ACCESS_TOKEN))})

# Does the repository exist already?
repo_info_url = "/".join(("https://api.github.com/repos/" + ORGANISATION, REPO_NAME))
r = S.get(repo_info_url)

if (r.ok) and ("id" in r.json().keys()):
    #print "GitHub mirror repository is present"
    sys.exit(0)

# It doesn't, so we need to create the repository
repo_create_payload = {
    "name": REPO_NAME,
    "description": REPO_DESC,
    "private": False,
    "has_issues": False,
    "has_wiki": False,
    "has_downloads": False,
    "auto_init": False,
}

#print "Creating GitHub mirror repository"
repo_create_url = "https://api.github.com/orgs/" + ORGANISATION + "/repos"
r = S.post(repo_create_url, data = json.dumps(repo_create_payload))

# Check if the repo was created successfully and exit accordingly
if (r.status_code == 201) and ("id" in r.json().keys()):
    #print "GitHub mirror repository created"
    sys.exit(0)
else:
    #print "GitHub mirror repository creation failed"
    sys.exit(1)
