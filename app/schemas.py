from pydantic import BaseModel


# ========== MODEL ==========
class ModelBase(BaseModel):
    name: str
    year: int
    body_type: str
    power_hp: int
    cylinders: int
    liters: float


class ModelCreate(ModelBase):
    pass


class Model(ModelBase):
    id: int
    brand_id: int

    class Config:
        orm_mode = True


# ========== BRAND ==========
class BrandBase(BaseModel):
    name: str
    country: str
    headquarters_city: str
    date_founded: int
    owner_id: int


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    id: int
    cars: list[Model] = []

    class Config:
        orm_mode = True


# ========== OWNER ==========
class OwnerBase(BaseModel):
    name: str


class OwnerCreate(OwnerBase):
    password: str


class Owner(OwnerBase):
    id: int
    hashed_password: str
    car_brands: list[Brand] = []

    class Config:
        orm_mode = True
