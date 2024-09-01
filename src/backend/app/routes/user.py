from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserUpdate, UserResponse, Token, MessageResponse
from app.dependencies.auth import get_current_user, create_access_token

router = APIRouter()

# Регистрация пользователя
@router.post("/register/", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Проверка, существует ли пользователь с таким же email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Создание нового пользователя
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Аутентификация пользователя
@router.post("/login/", response_model=Token)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    # Проверка существования пользователя
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Генерация токена (например, JWT)
    token = create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

# Получение информации о текущем пользователе
@router.get("/me/", response_model=UserResponse)
async def read_user(current_user: User = Depends(get_current_user)):
    return current_user

# Обновление данных пользователя
@router.put("/me/", response_model=UserResponse)
async def update_user(user_update: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(current_user, key, value)
    
    db.commit()
    db.refresh(current_user)
    return current_user

# Удаление пользователя
@router.delete("/me/", response_model=MessageResponse)
async def delete_user(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db.delete(current_user)
    db.commit()
    return {"message": "User deleted successfully"}