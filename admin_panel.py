from fastapi import FastAPI, BackgroundTasks
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = FastAPI()
letoctf_api = "http://192.168.14.39:8000/api/v1"

scheduler = BackgroundScheduler()
scheduler.start()

# Задача, которая будет выполняться каждый день в определенное время
def daily_task():
    date = "2023-08-07"  # Здесь укажите нужную дату
    events = requests.get(f"{letoctf_api}/event?date={date}").json()

    for event in events['data']['content']:
        event['start'] = event['start'].split(" ")[1].split(':')[0] + ':' + event['start'].split(" ")[1].split(':')[1]
        event['end'] = event['end'].split(" ")[1].split(':')[0] + ':' + event['end'].split(" ")[1].split(':')[1]

    # Дополнительная логика, выполняемая в задаче

scheduler.add_job(daily_task, 'cron', day_of_week='*', hour='12', minute='0')  # Здесь можно настроить время выполнения задачи

@app.get("/api/v1/user/token/{token}")
async def login(token: str):
    """Get user token and send his id for login functionality"""
    try:
        user = requests.get(f"{letoctf_api}/user/token/{token}").json()
        return {'id': user['data']['id']}
    except:
        raise HTTPException(status_code=401)

@app.get("/api/v1/challenge/{task_id}/submit")
async def challenge(task_id: str):
    """Submit task via task_id"""
    task = requests.get(f"{letoctf_api}/challenge/{task_id}/submit").json()
    return task

@app.get("/api/v1/event")
async def get_events(date: str = "2023-06-30"):
    """Get all events from API by date"""
    events = requests.get(f"{letoctf_api}/event?date={date}").json()

    for event in events['data']['content']:
        event['start'] = event['start'].split(" ")[1].split(':')[0] + ':' + event['start'].split(" ")[1].split(':')[1]
        event['end'] = event['end'].split(" ")[1].split(':')[0] + ':' + event['end'].split(" ")[1].split(':')[1]

    return events

@app.get("/api/v1/challenge")
async def get_challenges(userId: str):
    """Get challenges for user"""
    challenges = requests.get(f"{letoctf_api}/challenge?userId={userId}").json()
    return challenges

@app.get("/api/v1/challenge/{task_id}")
async def get_challenge(task_id: str):
    """Get task description by task_id"""
    task = requests.get(f"{letoctf_api}/challenge/{task_id}").json()
    return task

@app.get("/api/v1/score/profile/{user_id}")
async def get_user_score(user_id: str):
    """Get user score by his id"""
    user_data = requests.get(f"{letoctf_api}/challenge/{user_id}").json()
    return user_data

@app.get("/api/v1/scoreboard/users")
async def get_user_scoreboard():
    """Return user scoreboard"""
    users = requests.get(f"{letoctf_api}/user").json()['data']['content']
    out = [{"name": user['name'], "data": []} for user in users if not user['admin']]
    users_id = [user['id'] for user in users if not user['admin']]

    for i in range(len(users_id)):
        user_data = requests.get(f"{letoctf_api}/score/user/{users_id[i]}/history").json()['data']['items']['content']
        data = [{'x': i['submitted'], 'y': i['challenge']['weight']} for i in user_data]
        out[i]["data"] = data

    return out

@app.get("/api/v1/scoreboard/teams")
async def get_team_scoreboard():
    """Return team scoreboard"""
    teams = requests.get(f"{letoctf_api}/team").json()['data']['content']
    out = [{"name": team['name'], "data": []} for team in teams if not team['admin']]
    teams_id = [team['id'] for team in teams if not team['admin']]

    for i in range(len(teams_id)):
        team_data = requests.get(f"{letoctf_api}/score/team/{teams_id[i]}/history").json()['data']['items']['content']
        data = [{'x': i['submitted'], 'y': i['challenge']['weight']} for i in team_data]
        out[i]["data"] = data
        
@app.get("/api/v1/scoreboard/teams")
async def get_team_scoreboard():
    """Return team scoreboard"""
    teams = requests.get(f"{letoctf_api}/team").json()['data']['content']
    out = [{"name": team['name'], "data": []} for team in teams if not team['admin']]
    teams_id = [team['id'] for team in teams if not team['admin']]

    for i in range(len(teams_id)):
        team_data = requests.get(f"{letoctf_api}/score/team/{teams_id[i]}/history").json()['data']['items']['content']
        data = [{'x': i['submitted'], 'y': i['challenge']['weight']} for i in team_data]
        out[i]["data"] = data

    return out
