from fastapi import Depends
from . import users

def get_letoctf_api():
    return "http://192.168.14.39:8000/api/v1"

def get_user_manager(api_url=Depends(get_letoctf_api)):
    return users.UserManager(api_url)