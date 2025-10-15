from fastapi import FastAPI
from backend.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cho phép frontend gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def trang_chu():
    return {"thong_diep": "Chào mừng đến API Quản Lý Người Dùng với MongoDB"}

# Gắn router vào app
app.include_router(router)

""" khi tách file thì k chạy trên web nữa 
  chạy lệnh uvicorn backend.main:app --reload
  nó sẽ báo lỗi là k tìm thays file file backend"""
