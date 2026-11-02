from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.common.response import Response
from app.schemas.auth import LoginRequest, RegisterRequest
from app.database import get_db
from app.services import auth_service

router = APIRouter(tags=["权限验证"], prefix="/auth")


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    """登录的接口"""
    result = auth_service.login(db, data)

    return Response.success(
        message="登录成功",
        data=result,
    )


@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    """登录的接口"""
    auth_service.register(db, data)

    return Response.success(message="注册成功")
