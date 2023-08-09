from fastapi import FastAPI

app = FastAPI()

@app.get("/shoaib")
def root():
   return {"message": "Hello World"}