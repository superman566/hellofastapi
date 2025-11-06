from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/helloworld")
async def helloworld():
	return {"message": "hello world"}

if __name__ == "__main__":
	uvicorn.run("helloworld:app", reload=True)
