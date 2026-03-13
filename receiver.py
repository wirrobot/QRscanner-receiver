# server_fastapi_simple.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI()

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScanData(BaseModel):
    result: str
    timestamp: int
    device: str = "未知"

@app.post("/scan")
async def scan(data: ScanData):
    # 打印到控制台
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 扫码: {data.result}")
    
    # 返回成功响应
    return {
        "status": "ok",
        "received": data.result,
        "time": datetime.now().isoformat()
    }

@app.get("/")
async def root():
    return {"status": "running", "message": "扫码服务器运行中"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)