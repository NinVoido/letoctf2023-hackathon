from fastapi import FastAPI, Response, status, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()
letoctf_api = "http://192.168.14.39:8000/api/v1"

@app.get("/api/v1/user/token/{token}")
async def login(token: str, response: Response):
    """Get user token and send his id for login functionality"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        user = requests.get(f"{letoctf_api}/user/token/{token}").json()
        return {'id': user['data']['id']}
    except:
        return HTTPException(status_code=401)

@app.get("/api/v1/challenge/{task_id}/submit")
async def challenge_submit(task_id: str, response: Response):
    """Submit task via task_id"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        task = requests.get(f"{letoctf_api}/challenge/{task_id}/submit").json()
        return task
    except:
        raise HTTPException(status_code=400, detail="Failed to submit challenge")

@app.get("/api/v1/event")
async def event(date: str, response: Response):
    """Get all events from api by date"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        events = requests.get(f"{letoctf_api}/event?date={date}").json()

        for event in events['data']['content']:
            event['start'] = event['start'].split(" ")[1].split(':')[0] + ':' + event['start'].split(" ")[1].split(':')[1]
            event['end'] = event['end'].split(" ")[1].split(':')[0] + ':' + event['end'].split(" ")[1].split(':')[1]

        return events
    except:
        raise HTTPException(status_code=500, detail="Failed to fetch events")

@app.get("/api/v1/challenge")
async def challenge(userId: str, response: Response):
    """Get challenges for user"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        challenges = requests.get(f"{letoctf_api}/challenge?userId={userId}").json()
        return challenges
    except:
        raise HTTPException(status_code=500, detail="Failed to fetch challenges")

@app.get("/api/v1/challenge/{task_id}")
async def challenge_description(task_id: str, response: Response):
    """Get task description by task_id"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        task = requests.get(f"{letoctf_api}/challenge/{task_id}").json()
        return task
    except:
        raise HTTPException(status_code=404, detail="Task not found")

@app.get("/api/v1/score/profile/{user_id}")
async def profile(user_id: str, response: Response):
    """Get user score by his id"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        user_data = requests.get(f"{letoctf_api}/challenge/{user_id}").json()
        return user_data
    except:
        raise HTTPException(status_code=500, detail="Failed to fetch user profile")


@app.get("/api/v1/challenge/{task_id}")
async def admin_get_challenge(task_id: str, response: Response):
    """Получение описания задачи администратором по идентификатору"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        response = requests.get(f"{letoctf_api}/challenge/{task_id}")
        response.raise_for_status()
        challenge = response.json()
        return challenge
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=404, detail="Challenge not found")

@app.get("/api/v1/scoreboard/users")
async def score_users(response: Response):
    """Return user scoreboard"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        users = requests.get(f"{letoctf_api}/user").json()['data']['content']
        out = [{"label": user['name'], "data": []} for user in users if user['admin'] == False]
        users_id = [user['id'] for user in users if user['admin'] == False]
        for i in range(len(users_id)):
            user_data = requests.get(f"{letoctf_api}/score/user/{users_id[i]}/history").json()['data']['items']['content']
            data = [{'x': i['submitted'], 'y': i['challenge']['weight']} for i in user_data]
            out[i]["data"] = data

        return out
    except:
        raise HTTPException(status_code=500, detail="Failed to fetch user scoreboard")

@app.get("/api/v1/scoreboard/teams")
async def score_teams(response: Response):
    """Return team scoreboard"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        teams = requests.get(f"{letoctf_api}/team").json()['data']['content']
        out = [{"label": team['name'], "data": []} for team in teams]
        teams_id = [team['id'] for team in teams]

        for i in range(len(teams_id)):
            team_data = requests.get(f"{letoctf_api}/score/team/{teams_id[i]}/history").json()['data']['items']['content']
            data = [{'x': i['submitted'], 'y': i['challenge']['weight']} for i in team_data]
            out[i]["data"] = data

        return out
    except:
        raise HTTPException(status_code=500, detail="Failed to fetch team scoreboard")

@app.get("/api/v1/score/profile/{user_id}")
async def get_user_score(user_id: str, response: Response):
    """Get user score by his id"""
    try:
        response.headers["Access-Control-Allow-Origin"] = "*"
        user_data = requests.get(f"{letoctf_api}/challenge/{user_id}").json()
        return user_data
    except:
        # Обработка исключений при получении данных о пользователе
        pass
