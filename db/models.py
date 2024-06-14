from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Boolean, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils.types import ChoiceType
from db.database import Base, ENGINE


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    address = relationship("Address", back_populates="cities")

    def __repr__(self):
        return f"City name={self.name}"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey("city.id"))
    name = Column(String(40), nullable=False)
    cities = relationship("City", back_populates="address")

    def __repr__(self):
        return f"Address name={self.name}"


class User(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    pay = relationship("Payments", back_populates="user_i")

    def __repr__(self):
        return self.first_name


class Lesson(Base):
    __tablename__ = "lesson"
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    description = Column(Text, nullable=False)
    homework = Column(Text, nullable=False)
    les = relationship("Modules", back_populates="lson")

    def __repr__(self):
        return self.title


class Modules(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    lson = relationship("Lesson", back_populates="les")
    cour = relationship("Courses", back_populates="modl")

    def __repr__(self):
        return self.name


class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    module = Column(Integer, ForeignKey("modules.id"))
    price = Column(Integer, nullable=False)

    pay = relationship("Payments", back_populates="course")
    modl = relationship("Modules", back_populates="cour")

    def __repr__(self):
        return self.name


class PayType(Base):
    __tablename__ = "pay_type"
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    payment = relationship("Payments", back_populates="pay_t")

    def __repr__(self):
        return self.type


class Payments(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("auth_user.id"))
    amount = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"))
    type = Column(Integer, ForeignKey("pay_type.id"))
    pay_t = relationship("PayType", back_populates="payment")
    user_i = relationship("User", back_populates="pay")
    course = relationship("Courses", back_populates="pay")

    def __repr__(self):
        return f'payment'


class ProductsProduct(Base):
    __tablename__ = 'products_product'

    id = Column(Integer, primary_key=True, index=True)

    # Mahsulot kategoriyasi
    category_code = Column(String(20), nullable=False)
    category_name = Column(String(50), nullable=False)

    # Mahsulot kategoriya ichida ketgoriyasi ("Go'sht"->"Mol go'shti")
    subcategory_code = Column(String(20), nullable=False)
    subcategory_name = Column(String(50), nullable=False)

    # Mahsulot haqida malumot
    productname = Column(String(50), nullable=False)
    photo = Column(String(255), nullable=True)
    price = Column(Integer, nullable=False)
    description = Column(String(3000), nullable=True)

    def __repr__(self):
        return f'{self.category_name}'


class ProductsUser(Base):
    __tablename__ = 'products_user'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)

    def __repr__(self):
        return f"full_name={self.full_name}, username={self.username}, telegram_id={self.telegram_id}"
