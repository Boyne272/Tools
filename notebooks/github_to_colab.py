"""
This is a small section fo code to pull a github repo into the google colab
environment. Caution is needed as the password you give is stored in the git
remotes, hence if you run anything like 'git remote -v' will show your password.
Note if your github password has an @ in it then this will not work.
"""


import os
from getpass import getpass


# inputs
username = "Boyne272"
clone_url = "https://github.com/Boyne272/Richs_Cycle_GAN.git"
name = "Richard Boyne"
email = "rmb115@ic.ac.uk"


# remove sample data if it is there
if os.path.isdir("sample_data"):
    !rm -r sample_data


# if we are not currently in a repo
if not os.path.isdir(".git"):
    
    # get password
    password = getpass('github password: ')
    os.environ['GITHUB_AUTH'] = clone_url[:8] + username + ':' + password + '@' + clone_url[8:]
    del password
    
    # clone the repo here
    !git clone $GITHUB_AUTH repo --quiet # reduce the output of clone
    !cp -r repo/.git .
    !cp repo/.gitignore .
    !rm -r repo
    
    
# set name and email for commits
os.environ['GITHUB_AUTH'] = email
!git config --global user.email $GITHUB_AUTH
os.environ['GITHUB_AUTH'] = name
!git config --global user.name $GITHUB_AUTH


# show where we are
!git show --summary
