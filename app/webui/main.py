from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from frontend import router as frontend_router
from backend import router as backend_router

# FastAPIのインスタンス取得
app = FastAPI()

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="../static"), name="static")

app.include_router(frontend_router.router)
app.include_router(backend_router.router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])