import logging
import os
import platform
import subprocess
import sys
from pathlib import Path

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.DEBUG)

# 프로젝트 루트 디렉토리를 sys.path에 추가
# 상단에 위치 필수 !
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# 여기부터 router 추가
from src.app.router import (
    auth_router,
    chat_router,
    comment_router,
    post_router,
    user_router,
)

app = FastAPI(debug=True)
# 테스트용 HTTPException 발생
@app.get("/http-exception")
async def raise_http_exception():
    raise HTTPException(status_code=404, detail="테스트 404 에러입니다.")

# 테스트용 일반 Exception 발생
@app.get("/general-exception")
async def raise_general_exception():
    raise Exception("테스트 일반 예외입니다.")

app.include_router(post_router)
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(comment_router)
app.include_router(user_router)

origins = ["http://localhost:5173", "https://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_origin_regex="http://111\\.111\\.111\\.111(:\\d+)?",
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api/v1")


def run_check_script():
    system = platform.system().lower()

    if system == "darwin":  # Mac OS
        script_path = "./scripts/check.sh"
    elif system == "linux":
        script_path = "./scripts/check.sh"
    elif system == "windows":
        script_path = os.path.join(project_root, "scripts", "check.bat")
    else:
        print(f"Unsupported operating system: {system}")
        return

    try:
        print(f"Running {script_path}...")
        result = subprocess.run([script_path], capture_output=True, text=True, shell=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr, file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: {script_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # run_check_script()
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)