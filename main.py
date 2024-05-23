from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "é só Sucesso 3"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)
