from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def new():
    return {"message": "hello world"}

@app.get("/user/admin")
async def new_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def new_id(user_id: int = Path(min_length=1, max_length=100, description='Enter User ID', example= 1)):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/new_user/{username}/{age}")
async def new_name(username: str = Path(min_length=5, max_length=20, description='Enter username', example=  'UrbanUser' ),
                    age: int = Path(ge=18, le=120, description='Enter age', example= 24)):
    return {"mssage": f"Информация о пользователе.Имя: {username}, Возраст: {age}"}