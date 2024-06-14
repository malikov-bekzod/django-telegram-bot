from fastapi import APIRouter
from db.database import Session, ENGINE
from db.schemas import ProductsProductBase
from db.models import ProductsProduct, User
from fastapi import HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_jwt_auth import AuthJWT


session = Session(bind=ENGINE)

product_router = APIRouter(prefix="/product")


@product_router.get('/')
async def get_products():
    products = session.query(ProductsProduct).all()
    return jsonable_encoder(products)


@product_router.get('/{id}')
async def get_product(id: int):
    product = session.query(ProductsProduct).filter(ProductsProduct.id == id).first()
    return jsonable_encoder(product)


@product_router.post('/create')
async def create_product(product: ProductsProductBase):
    product_c = session.query(ProductsProduct).filter(ProductsProduct.id == product.id).first()
    if not product_c:
        new_product = ProductsProduct(
            id=product.id,
            category_code=product.category_code,
            category_name=product.category_name,
            subcategory_code=product.subcategory_code,
            subcategory_name=product.subcategory_name,
            product_name=product.product_name,
            price=product.price,
            photo=product.photo,
            description=product.description,

        )
        session.add(new_product)
        session.commit()
        return jsonable_encoder(new_product, detail="Product created successfully")

    else:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product already exists")

