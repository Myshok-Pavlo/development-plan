from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthchek")
def read_root():
    return {"status": "ok"}
