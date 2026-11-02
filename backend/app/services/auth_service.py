from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, RegisterRequest
from sqlalchemy.orm import Session
from app.common.exception import BusinessException
from app.schemas.user import UserResponse
from app.schemas.auth import LoginRequest, LoginResponse
from app.models.user import User
from app.utils import password
from app.utils.password import hash_password, verify_password
from app.utils.jwt import create_access_token


def login(db: Session, data: LoginRequest):
    user = db.query(User).filter(data.username == User.username).first()
    if not user or not verify_password(data.password, user.password):
        raise BusinessException(message="账号或密码错误")
    if user.status != 1:
        raise BusinessException(message="账号被禁用")

    token = create_access_token(user.id)

    return LoginResponse(token=token, user=UserResponse.model_validate(user))


def register(db: Session, data: RegisterRequest):
    user = db.query(User).filter(data.username == User.username).first()
    if user:
        raise BusinessException(message="账号已存在")
    user_model = User(
        username=data.username,
        password=hash_password(data.password),
        name=data.name or data.username,
        role="student",
        status=1,
    )
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
