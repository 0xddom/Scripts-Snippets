#!/usr/bin/bash
ssh-keygen -t rsa -C "yourmail@here" -f ~/.ssh/$1
eval `ssh-agent -s`
ssh-add ~/.ssh/$1
cat ~/.ssh/${1}.pub | pbcopy

