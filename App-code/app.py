
  

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()
counter =1
output = '''# HELP http_requests_total The total number of HTTP requests.
# TYPE http_requests_total counter
'''
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/metrics", response_class=PlainTextResponse)
def read_root():
    global counter
    global output
    counter = counter + 1
    return output + "replies_counter: " + str(counter)

@app.get("/healthchek")
def read_root():
    return {"status": "ok"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)

    
