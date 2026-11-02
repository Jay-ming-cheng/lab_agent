
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column ,DeclarativeBase
from sqlalchemy import create_engine, DateTime
from app.config import settings
from datetime import datetime


engine = create_engine(
  settings.DATABASE_URL
)

#建立数据库连接
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#给每个请求提供数据库session，并确保请求结束后自动关闭
def get_db():
  db = session()
  try:
    yield db
  finally:
    db.close()



class Base(DeclarativeBase):
  id: Mapped[int] = mapped_column(primary_key= True, autoincrement=True, comment="主键ID")
  create_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment="创建时间")
  update_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")


































