from operator import or_

from app.common.exception import BusinessException
from app.common.response import PageResponse
from app.models.user import User
from app.schemas.user import (
    PasswordUpdateRequest,
    UserCreateRequest,
    UserResponse,
    UserUpdateRequest,
)
from sqlalchemy.orm import Session

from app.utils import password
from app.utils.password import hash_password, verify_password


def get_user_info(user: User) -> UserResponse:
    return UserResponse.model_validate(user)


def update_user_info(db: Session, user: User, data: UserUpdateRequest):
    user_dict = data.model_dump(
        exclude_none=True, exclude={"role", "status"}
    )  # pydatic对象转换成字典
    for field, value in user_dict.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)


def update_password(db: Session, user: User, data: PasswordUpdateRequest):
    """更新用户密码"""
    if not verify_password(data.old_password, user.password):
        raise BusinessException("旧密码不正确")
    if data.old_password == data.new_password:
        raise BusinessException("新密码不能与旧密码相同")
    user.password = hash_password(data.new_password)
    db.commit()


"""分页模糊查询分页列表"""


def get_user_page(
    db: Session,
    page: int,
    page_size: int,
    username: str | None = None,
):
    query = db.query(User)
    if username:

        query = query.filter(
            or_(User.username.like(f"%{username}%"), User.name.like(f"%{username}%"))
        )
    total = query.count()
    items = (
        query.order_by(User.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return PageResponse(
        list=[UserResponse.model_validate(item) for item in items], total=total
    )


def create_user(db: Session, data: UserCreateRequest):
    """新增用户"""
    exist = db.query(User).filter(User.username == data.username).first()
    if exist:
        raise BusinessException(message="账号已存在 ")

    user = User(
        username=data.username,
        password=hash_password(data.password),
        name=data.name,
        role=data.role,
        email=data.email,
        avatar=data.avatar,
        status=data.status if data.status is not None else 1,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)


def update_user(db: Session, user_id: int, data: UserUpdateRequest):
    """更新用户"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise BusinessException(message="账号不存在 ")

    payload = data.model_dump(exclude_none=True)

    for field, value in payload.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)


def delete_user(db: Session, user_id: int, current_user: User):
    """删除用户"""
    if user_id == current_user:
        raise BusinessException(message="不能删除当前登录的账号")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise BusinessException(message="用户不存在")
    db.delete(user)
    db.commit()
