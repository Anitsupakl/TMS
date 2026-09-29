#Написать скрипт, который запрашивает имя пользователя и выводит персонализированное приветствие
#!bin/bash

echo 'Enter your name: '

read NAME

if [[ -z ${NAME} ]]; then
  echo "Вы ввели пустую строку"
fi

if [[ ${NAME} ]]; then 
  echo "Hi, ${NAME}"
fi
