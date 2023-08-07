# letoctf hackathon 2023

## goals:
 - [ ] перенесение тг бота в webui
 - [ ] расширение клиента
 - [ ] добавление webui админки
 
## client webui
- /tasks
- client:
- - GET - получить
- - POST - сдать
- /scoreboard/
- - только GET-получить список борд
- /scoreboard/\<scope\> - scope из списка борд, получаем борду
- - scope изначально - users, teams
- - доступны только GET
- /aschedule/\<day>
- - только GET - получить расписание на day
- /support
- - GET - контакты хелперов и их роли
- - POST - оформить тикет
- - PUT - изменить тикет
- /login
- - POST - принимает токен, логинится
- /exit
 

