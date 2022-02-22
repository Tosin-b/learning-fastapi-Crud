#from ast import Str
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

def hash(password:str):
    return pwd_context.hash(password)

# this Function takes users password and hashed password and compares them
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)