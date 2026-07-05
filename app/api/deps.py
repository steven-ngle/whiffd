from fastapi import Request
from app.services.ballchasing import BallchasingClient

def get_ballchasing(request: Request) -> BallchasingClient:
    return request.app.state.ballchasing