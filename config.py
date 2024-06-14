from fastapi import FastAPI
from auth import a_router
from crud.city import city_router
from crud.address import address_router
from crud.lesson import lesson_router
from crud.modules import module_router
# from crud.courses import course_router
from crud.paytype import pyt_router
from crud.payment import pay_router
from crud.product import product_router
from crud.pruser import user_router
from db.schemas import JwtModel
from fastapi_jwt_auth import AuthJWT


app = FastAPI()
app.include_router(a_router)
app.include_router(city_router)
app.include_router(address_router)
app.include_router(lesson_router)
app.include_router(module_router)
# app.include_router(course_router)
app.include_router(pyt_router)
app.include_router(pay_router)
app.include_router(product_router)
app.include_router(user_router)


@AuthJWT.load_config
def get_config():
    return JwtModel()


@app.get('/')
async def root():
    return {"message": "root xabari"}


@app.get('/items')
async def read_items():
    return {'message': 'test api items'}


@app.get('/userx')
async def user():
    return {'message': 'user page'}


@app.get('/userx/{id}')
async def read_user(id: int):
    return {'message': f'user id = {id}'}

