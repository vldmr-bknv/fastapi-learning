import uvicorn
from typing import Annotated
from fastapi import FastAPI, Header, HTTPException
from fastapi.requests import Request

app = FastAPI()

def checking_headers(headers: Request.headers):
    try:
        headers['user-agent']
    except:
        raise HTTPException(status_code=400, 
                            detail="The User-Agent header is not found!")
    
    try:
        headers['accept-language']
    except:
        raise HTTPException(status_code=400,
                            detail="The Accept-Language header is not found!")
        

@app.get("/headers")
async def get_headers(request: Request,
                      user_agent: Annotated[str | None, Header()] = None, 
                      accept_language: Annotated[str | None, Header()] = None):
    try:
        checking_headers(request.headers)
    except HTTPException as e:
        raise e

    return {
        "User-Agent": user_agent, 
        "Accept-Language": accept_language
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)