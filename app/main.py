from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.user_routes import router as user_router
from app.db.base import Base
from app.db.session import engine
import app.models  # 👈 IMPORTANTE

Base.metadata.create_all(bind=engine)


app = FastAPI(title="FastAPI + Svelte")

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(
    user_router,
    prefix="/api/v1/users",
    tags=["Users"]
)
