import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi import Cookie
from app.models.models import User

app = FastAPI()
user_example: dict = {"username": "Jerry", "password": "qwerty"}
SESSIONS: dict = {}
DB: list[User] = [User(**user_example)]

@app.post("/login")
async def auth(user: User, response: Response):
    ''' Аутентифицирует пользователя (игрушечная реализация) '''
    for person in DB:
        if user.username == person.username and user.password == person.password:
            session_token = "abc123xyz456"
            SESSIONS[session_token] = user
            response.set_cookie(key="session_token", value=session_token, httponly=True)
            return {"message": "Authentification successfull!"}
    return {"error": "Invalid username or password"}


@app.get("/user")
async def get_user_info(session_token = Cookie()):
    ''' Возвращает данные о пользователе, если он аутенитифицирован'''
    if session_token in SESSIONS:
        return DB[0].model_dump()
    return {"error": "Access denied"}


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)