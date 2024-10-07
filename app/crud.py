from sqlalchemy.orm import Session

import auth
import models
import schemas


# ========== OWNER ==========
def get_owner(db: Session, owner_id: int):
    return db.query(models.Owner).filter(models.Owner.id == owner_id).first()


def get_owner_name(db: Session, owner_name: str):
    return db.query(models.Owner).filter(models.Owner.name == owner_name).first()


def create_owner(db: Session, owner: schemas.OwnerCreate):
    hashed_password = auth.get_password_hash(owner.password)
    db_owner = models.Owner(name=owner.name, hashed_password=hashed_password)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


# ========== BRAND ==========
def get_brand(db: Session, brand_id: int):
    return db.query(models.Brand).filter(models.Brand.id == brand_id).first()


def get_brand_name(db: Session, brand_name: str):
    return db.query(models.Brand).filter(models.Brand.name == brand_name).first()


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()


def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(name=brand.name, country=brand.country, headquarters_city=brand.headquarters_city,
                            date_founded=brand.date_founded, owner_id=brand.owner_id)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


# ========== MODEL ==========
def get_model(db: Session, model_id: int):
    return db.query(models.Model).filter(models.Model.id == model_id).first()


def get_model_name(db: Session, model_name:str):
    return db.query(models.Model).filter(models.Model.name == model_name).first()


def get_model_year(db: Session, model_year: int):
    return db.query(models.Model).filter(models.Model.year == model_year).first()


def get_model_body_type(db: Session, model_body_type: str):
    return db.query(models.Model).filter(models.Model.body_type == model_body_type).first()


def get_model_power_hp(db: Session, model_power_hp: int):
    return db.query(models.Model).filter(models.Model.power_hp == model_power_hp).first()


def get_model_brand(db: Session, brand_id: int):
    return db.query(models.Model).filter(models.Model.brand_id == brand_id).first()


def get_models(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Model).offset(skip).limit(limit).all()


def create_model(db: Session, model: schemas.ModelCreate, brand_id: int):
    db_model = models.Model(**model.dict(), brand_id=brand_id)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def delete_model(db: Session, model_id: int):
    db_model_delete = db.query(models.Model).filter(models.Model.id == model_id).first()
    db.delete(db_model_delete)
    db.commit()
    return db_model_delete
