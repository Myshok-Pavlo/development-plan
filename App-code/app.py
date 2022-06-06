import uvicorn
from fastapi import FastAPI
counter = 0
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthchek")
def read_root():
    return {"status": "ok"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
