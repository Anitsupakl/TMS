#!/bin/bash

GITLAB_URL=https://gitlab.com/dos-26/cmdb/frontend.git


gitlab_download() {
  echo "Скачиваю проект ${GITLAB_URL}"
  git clone ${GITLAB_URL}
  echo
  if [ -d frontend ]; then
    echo "Проект скачан и находится в директории /frontend"
  else
    echo "Проект не скачан"
  fi
}

gitlab_download
