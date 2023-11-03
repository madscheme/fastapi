from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/small/{name}")
async def download_small_file(name):
    return FileResponse(name)
