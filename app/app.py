import uvicorn
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="AWS + FastAPI",
    description="AWS API Gateway, Lambdas and FastAPI")

# Mangum allows us to use Lambdas to process requests
handler = Mangum(app=app)

@app.get("/")
async def root():
   return {"message": "Hello World!"}

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)
