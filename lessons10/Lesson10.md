1. В домашней директории создать home_works создать директорию lesson_10
2. В директории lesson_10 создать директорию available, в ней файлы app.conf, readme.md, app.log с произвольным содержимым
3. В директории lesson_10 создать директорию enabled, в ней создать symlink на available/app.conf
4. В директории lesson_10 создать директории logs и debug; переместить файл available/app.log в директорию logs, а в debug сделать hardlink на logs/app.log
![Image Alt](https://github.com/Anitsupakl/-TMS_Lessons/blob/lesson10/1-4.png?raw=true)

5. Добавить к вашей ВМ дополнительный диск.
![Image Alt](https://github.com/Anitsupakl/-TMS_Lessons/blob/lesson10/VM_disk.png?raw=true)


6. Посмотреть список блочных устройств (lsblk) и список смонтированных ФС (df -Th)

Добавлен sdb      8:16   0    2G  0 disk 
![Image Alt](https://github.com/Anitsupakl/-TMS_Lessons/blob/lesson10/5.png?raw=true)

7. Создать на новом диске ФС типа ext4
![Image Alt](https://github.com/Anitsupakl/-TMS_Lessons/blob/lesson10/7.png?raw=true)

8. Создать директорию /opt/application и смонтировать в нее новый диск (монтирование должно быть постоянным, через /etc/fstab)
![Image Alt](https://github.com/Anitsupakl/-TMS_Lessons/blob/lesson10/7.1.png?raw=true)
9.  Скопировать /opt/application все содержимое lesson_10. Должно получиться примерно такое
/opt/application/
├── available
│   └── app.conf
├── debug
│   └── app.log
├── enabled
│   └── app.conf -> available/app.conf
└── logs
    └── app.log


![Image Alt](https://github.com/Anitsupakl/-TMS_Lessons/blob/lesson10/9.png?raw=true)


    
10.Попробовать сделать hardlink на файл $HOME/home_works/lesson_10/available/readme.md в директории /opt/application (не получится); затем сделать symlink на этот же файл


![Image Alt](https://github.com/Anitsupakl/-TMS_Lessons/blob/lesson10/9.1.png?raw=true)

11.Это уже потом заметилось после ребута)
В пункте 8 недописала букву s в слове defaults, поэтому и папка lost+founds создалась, файлик не редактировала уже весь заново пропишу тут)

![Image Alt](https://github.com/Anitsupakl/TMS_Lessons/blob/lesson10/11.png?raw=true)






