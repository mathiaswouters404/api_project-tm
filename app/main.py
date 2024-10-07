import os
import crud, models, schemas, auth
# import auth
# import crud
# import models
# import schemas
from database import SessionLocal, engine

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "https://mathiaswouters.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ========== GET METHODS ==========
@app.get("/brand/")
def get_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_brands(db, skip=skip, limit=limit)


@app.get("/brand/id/{brand_id}", response_model=schemas.Brand)
def get_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand


@app.get("/brand/name/{brand_name}", response_model=schemas.Brand)
def get_brand_name(brand_name: str, db: Session = Depends(get_db)):
    db_brand_name = crud.get_brand_name(db, brand_name=brand_name)
    if db_brand_name is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand_name


@app.get("/model/", response_model=list[schemas.Model])
def get_models(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_models(db, skip=skip, limit=limit)


@app.get("/model/id/{model_id}", response_model=schemas.Model)
def get_model(model_id: int, db: Session = Depends(get_db)):
    db_model = crud.get_model(db, model_id=model_id)
    if db_model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return db_model


@app.get("/model/name/{model_name}", response_model=schemas.Model)
def get_model_name(model_name: str, db: Session = Depends(get_db)):
    db_model_name = crud.get_model_name(db, model_name=model_name)
    if db_model_name is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return db_model_name


@app.get("/model/year/{model_year}", response_model=schemas.Model)
def get_model_year(model_year: int, db: Session = Depends(get_db)):
    db_model_year = crud.get_model_year(db, model_year=model_year)
    if db_model_year is None:
        raise HTTPException(status_code=404, detail="Models with this year not found")
    return db_model_year


@app.get("/model/bodytype/{model_bodytype}", response_model=schemas.Model)
def get_model_bodytype(model_bodytype: str, db: Session = Depends(get_db)):
    db_model_bodytype = crud.get_model_body_type(db, model_body_type=model_bodytype)
    if db_model_bodytype is None:
        raise HTTPException(status_code=404, detail="Models with this body type not found")
    return db_model_bodytype


@app.get("/model/power/{model_power}", response_model=schemas.Model)
def get_model_power(model_power: int, db: Session = Depends(get_db)):
    db_model_power = crud.get_model_power_hp(db, model_power_hp=model_power)
    if db_model_power is None:
        raise HTTPException(status_code=404, detail="Models with this power not found")
    return db_model_power


@app.get("/model/brand/{brand_id}", response_model=schemas.Model)
def get_model_brand(brand_id: int, db: Session = Depends(get_db)):
    db_model_brand = crud.get_model_brand(db, brand_id=brand_id)
    if db_model_brand is None:
        raise HTTPException(status_code=404, detail="Models from this brand not found")
    return db_model_brand


# ========== POST METHODS ==========
@app.post("/brand/{brand_id}/model", response_model=schemas.Model)
def create_model(brand_id: int, model: schemas.ModelCreate, db: Session = Depends(get_db)):
    db_model = crud.get_model_name(db, model_name=model.name)
    if db_model:
        raise HTTPException(status_code=400, detail="Model already exists")
    return crud.create_model(db=db, model=model, brand_id=brand_id)


@app.post("/brand/", response_model= schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_brand = crud.get_brand_name(db, brand_name=brand.name)
    if db_brand:
        raise HTTPException(status_code=400, detail="Brand already exists")
    return crud.create_brand(db=db, brand=brand)


@app.post("/owner/", response_model= schemas.Owner)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_owner = crud.get_owner_name(db, owner_name=owner.name)
    if db_owner:
        raise HTTPException(status_code=400, detail="Owner already exists")
    return crud.create_owner(db=db, owner=owner)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    owner = auth.authenticate_owner(db, form_data.username, form_data.password)
    if not owner:
        raise HTTPException(
            status_code=401,
            detail="Incorrect name or password",
            headers={"WWW-Authenticate": "Bearer"})
    access_token = auth.create_access_token(data={"sub": owner.id})
    return {"access_token": access_token, "token_type": "bearer"}


# ========== DELETE METHODS ==========
@app.delete("/model/{model_id}")
def delete_model(model_id: int, db: Session = Depends(get_db)):
    db_model_delete = crud.get_model(db, model_id=model_id)
    if db_model_delete is None:
        raise HTTPException(status_code=404, detail="ID of model not found")
    return crud.delete_model(db=db, model_id=model_id)