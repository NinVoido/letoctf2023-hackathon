from fastapi import FastAPI,Response,status, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()
letoctf_api = "http://192.168.14.39:8000/api/v1"

@app.get("/api/v1/user/token/{token}")
async def login(token: str):
    """Get user token and send his id for login functionality"""
    try:
        user = requests.get(f"{letoctf_api}/user/token/{token}").json()
        return {'id': user['data']['id']}
    except:
        return HTTPException(status_code=401)

@app.get("/api/v1/challenge/{task_id}/submit")
async def challenge_submit(task_id: str):
    """Submit task via task_id"""
    task = requests.get(f"{letoctf_api}/challenge/{task_id}/submit").json()
    return task

@app.get("/api/v1/event")
async def event(date: str = "2023-06-30"):
    """Get all events from api by date"""
    events = requests.get(f"{letoctf_api}/event?date={date}").json()

    for event in events['data']['content']:
        event['start']=event['start'].split(" ")[1].split(':')[0]+':'+event['start'].split(" ")[1].split(':')[1]
        event['end']=event['end'].split(" ")[1].split(':')[0]+':'+event['end'].split(" ")[1].split(':')[1]

    return events

@app.get("/api/v1/challenge")
async def challenge(userId: str):
    """Get challenges for user"""
    challenges = requests.get(f"{letoctf_api}/challenge?userId={userId}").json()
    return challenges

@app.get("/api/v1/challenge/{task_id}")
async def challenge_description(task_id: str):
    """Get task description by task_id"""
    task = requests.get(f"{letoctf_api}/challenge/{task_id}").json()
    return task

@app.get("/api/v1/score/profile/{user_id}")
async def profile(user_id: str):
    """Get user score by his id"""
    user_data = requests.get(f"{letoctf_api}/challenge/{user_id}").json()
    return user_data


@app.get("/api/v1/scoreboard/users")
async def score_users():
    """Return user scoreboard"""
    users = requests.get(f"{letoctf_api}/user").json()['data']['content']
    out = [{"name": user['name'], "data": []} for user in users if user['admin']==False]
    users_id = [user['id'] for user in users if user['admin']==False]

    for i in range(len(users_id)):
        user_data = requests.get(f"{letoctf_api}/score/user/{users_id[i]}/history").json()['data']['items']['content']
        data = [{'x': i['submitted'], 'y': i['challenge']['weight']} for i in user_data]
        out[i]["data"] = data

    return out


@app.get("/api/v1/scoreboard/teams")
async def score_teams():
    """Return team scoreboard"""
    teams = requests.get(f"{letoctf_api}/team").json()['data']['content']
    out = [{"name": team['name'], "data": []} for team in teams if team['admin']==False]
    teams_id = [team['id'] for team in teams if team['admin']==False]

    for i in range(len(teams_id)):
        team_data = requests.get(f"{letoctf_api}/score/team/{teams_id[i]}/history").json()['data']['items']['content']
        data = [{'x': i['submitted'], 'y': i['challenge']['weight']} for i in team_data]
        out[i]["data"] = data

    return out

@app.get("/api/v1/user/token/{token}")
async def admin_login(token):
    """Авторизация администратора с помощью токена"""
    try:
        response = requests.get(f"{letoctf_api}/user/token/{token}")
        response.raise_for_status()
        admin = response.json()
        return {'id': admin['data']['id']}
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/api/v1/challenge/{task_id}")
async def admin_get_challenge(task_id: str):
    """Получение описания задачи администратором по идентификатору"""
    try:
        response = requests.get(f"{letoctf_api}/challenge/{task_id}")
        response.raise_for_status()
        challenge = response.json()
        return challenge
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=404, detail="Challenge not found")

@app.post("/api/v1/challenge")
async def admin_create_challenge(challenge_data: dict):
    """Создание новой задачи администратором"""
    try:
        response = requests.post(f"{letoctf_api}/admin/challenge", json=challenge_data)
        response.raise_for_status()
        created_challenge = response.json()
        return created_challenge
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=400, detail="Failed to create challenge")

@app.put("/api/v1/challenge/{task_id}")
async def admin_update_challenge(task_id: str, challenge_data: dict):
    """Обновление задачи администратором по идентификатору"""
    try:
        response = requests.put(f"{letoctf_api}/admin/challenge/{task_id}", json=challenge_data)
        response.raise_for_status()
        updated_challenge = response.json()
        return updated_challenge
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=400, detail="Failed to update challenge")

@app.delete("/api/v1/admin/challenge/{task_id}")
async def admin_delete_challenge(task_id: str):
    """Удаление задачи администратором по идентификатору"""
    try:
        response = requests.delete(f"{letoctf_api}/admin/challenge/{task_id}")
        response.raise_for_status()
        return {"message": "Challenge deleted successfully"}
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=400, detail="Failed to delete challenge")
