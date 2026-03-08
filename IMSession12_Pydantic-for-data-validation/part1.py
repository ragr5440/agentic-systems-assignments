from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserRegister (BaseModel):
    username : str = Field(min_length = 5)
    email : EmailStr
    age : int = Field(ge=18)

user_info = {'username':'Romil','email':'ragrawal@gmail', 'age':'34'}

try:
    user1 = UserRegister(**user_info)
    print("Valid input:", user1)
except ValidationError as e:
    print("invalid input:", e)


