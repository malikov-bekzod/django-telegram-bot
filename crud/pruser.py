from fastapi import APIRouter
from db.database import Session, ENGINE
from db.schemas import ProductsProductBase
from db.models import ProductsUser, User
from fastapi import HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_jwt_auth import AuthJWT


session = Session(bind=ENGINE)

user_router = APIRouter(prefix="/user")


@user_router.get('/')
def get_users():
    users = session.query(ProductsUser).all()
    return jsonable_encoder(users)


@user_router.get('/{id}')
def get_user(id: int):
    user = session.query(ProductsUser).filter(ProductsUser.id == id).first()
    return jsonable_encoder(user)


@user_router.post('/create')
def create_user(user: ProductsProductBase):
    user_check = session.query(ProductsUser).filter(ProductsUser.id == user.id).first()
    if not user_check:
        new_user = ProductsUser(
            id=user.id,
            full_name=user.full_name,
            username=user.username,
            telegram_id=user.telegram_id
        )
        session.add(new_user)
        session.commit()
        return jsonable_encoder(new_user, detail="User created successfully")

    else:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

