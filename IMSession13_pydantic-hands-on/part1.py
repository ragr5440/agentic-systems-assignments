from pydantic import BaseModel, Field, EmailStr, ValidationError, field_validator

class Address(BaseModel):
    city: str = Field(min_length=2)
    pincode: str = Field(min_length=6)

    @field_validator("pincode", mode='before')
    @classmethod
    def check_pincode(cls, pincode:str) -> str:
        if not pincode.isdigit() or len(pincode) != 6:
            raise ValueError("Pincode must be 6 digits")
        return pincode
    
user_address = {'city':'Indore', 'pincode':'452001'}

addr_obj = Address(**user_address)

class User (BaseModel):
    user_id : int
    name : str
    email : EmailStr
    age : int = Field(ge=18)
    user_address : Address
    is_premium : bool = Field(default= False)

user_info = {'user_id':'3975','name':'Romil', 'email':'ragrawal@xyz.com', 'age':'20','user_address': user_address, 'is_premium': False}
user_obj = User(**user_info)
print("Valid input:", user_obj)

