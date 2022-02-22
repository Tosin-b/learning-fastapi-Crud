from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from . import models
from .dababase import engine
from . routers import post, user, auth,vote
from .config import settings
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origns =["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origns,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "welcome to My api"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
