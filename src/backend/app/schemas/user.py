from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Схема для создания нового пользователя
class UserCreate(BaseModel):
    username: str  # Уникальное имя пользователя
    full_name: str  # Полное имя пользователя
    email: EmailStr  # Адрес электронной почты
    password: str  # Пароль пользователя
    phone_number: Optional[str] = None  # Номер телефона (необязательное поле)
    created_at: Optional[datetime] = None  # Дата создания (по умолчанию None)

# Схема для обновления информации о пользователе
class UserUpdate(BaseModel):
    full_name: Optional[str] = None  # Полное имя пользователя (необязательное)
    email: Optional[EmailStr] = None  # Адрес электронной почты (необязательное)
    phone_number: Optional[str] = None  # Номер телефона (необязательное)
    status: Optional[str] = None  # Статус пользователя (например, "active" или "inactive")
    role: Optional[str] = None  # Роль пользователя (например, "admin" или "user")

# Схема для представления данных пользователя в ответе API
class UserResponse(BaseModel):
    id: int  # Уникальный идентификатор пользователя
    username: str  # Имя пользователя
    full_name: str  # Полное имя пользователя
    email: EmailStr  # Адрес электронной почты
    phone_number: Optional[str] = None  # Номер телефона (необязательное)
    status: str  # Статус пользователя
    role: str  # Роль пользователя
    created_at: datetime  # Дата и время создания аккаунта

    class Config:
        orm_mode = True  # Позволяет использовать ORM-объекты

# Схема для входа пользователя
class UserLogin(BaseModel):
    email: EmailStr  # Адрес электронной почты
    password: str  # Пароль пользователя

# Схема для ответа с токеном
class Token(BaseModel):
    access_token: str  # Токен доступа
    token_type: str  # Тип токена (например, "bearer")

# Схема для сообщения об успешном удалении
class MessageResponse(BaseModel):
    message: str  # Сообщение об успешном выполнении операции