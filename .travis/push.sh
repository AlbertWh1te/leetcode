#!/bin/sh

setup_git() {
  git config --global user.email "iamwh1temark@outlook.com"
  git config --global user.name "MarkWh1te"
}

commit_website_files() {
  git add . 
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER update README.md"
}

upload_files() {
  git remote add origin https://${GH_TOKEN}@github.com/MarkWh1te/leetcode.git > /dev/null 2>&1
  git push -f origin master 
}

setup_git
commit_website_files
upload_files