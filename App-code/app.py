
  
import uvicorn
from fastapi import FastAPI
app = FastAPI()
counter =1

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/metrics")
def read_root():
    global counter
    counter = counter + 1
    return {"replies_counter " : counter}

@app.get("/healthchek")
def read_root():
    return {"status": "ok"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
