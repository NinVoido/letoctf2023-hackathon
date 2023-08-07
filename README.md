# letoctf hackathon 2023

## goals:
 - [ ] перенесение тг бота в webui
 - [ ] расширение клиента
 - [ ] добавление webui админки
 
## client webui
- /api/tasks
- client:
- - GET - получить
- - POST - сдать
- /api/scoreboard/
- - только GET-получить список борд
- /api/scoreboard/\<scope\> - scope из списка борд, получаем борду
- - scope изначально - users, teams
- - доступны только GET
- /api/schedule/\<day>
- - только GET - получить расписание на day
- /api/support
- - GET - контакты хелперов и их роли
- - POST - оформить тикет
- - PUT - изменить тикет
- /api/login
- - POST - принимает токен, логинится
- /exit
 
## роли
егор з - support, schedule, 
никита - login, exit