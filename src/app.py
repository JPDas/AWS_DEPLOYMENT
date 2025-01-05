# import uvicorn
# from fastapi import FastAPI
import json

# app = FastAPI()


# @app.get("/")
# async def root():
#    return {"message": "Hello World!"}

# if __name__ == "__main__":
#    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Hello World!'})
    }