from typing import Optional
from fastapi import Depends, FastAPI, Path, status, HTTPException, Header
from pydantic import BaseModel
import uvicorn
from enum import Enum

app = FastAPI()

async def verify_auth(api_token: Optional[str]=Header(None, alias="api-token")):
	if not api_token:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

class Gender(str, Enum):
	male= "male"
	female = "female"

class UserModel(BaseModel):
	id: Optional[int] = None
	username: str
	fullname: Optional[str] = None
	description: Optional[str] = None

class UserIn(UserModel):
	password: str

class UserOut(UserModel):
	...
	
# @app.get("/users/current")
# async def get_current_user():
# 	return {"user": f"this is the current user"}

# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
# 	return {"user": f"this is the user for {user_id}"}

# @app.get("/students/{gender}")
# async def get_students_gender(gender: Gender):
# 	return {"user": f"this is the students for {gender}"}


@app.get("/users", dependencies=[Depends(verify_auth)])
async def get_users(page_index: int, page_size: Optional[int]= 10):
	return {
		"page index": f"{page_index}",
		"page size": f"{page_size}"
	}



@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserIn):
	user_dict = user.model_dump()
	# user_dict.update({id: 10})
	user_dict["id"]=10
	return user_dict

@app.get("/users/{username}", status_code=status.HTTP_200_OK, response_model=UserOut)
async def get_user(username: str = Path(..., title="User name", min_length=4)):
	# user = {
	# 	"id": 10,
	# 	"username": "superman566",
	# 	"fullname": "Tony He",
	# 	"description": "Test"
	# 	}
	user = None
	if user:
		return user
	
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Non found the user")

# @app.get("/users/{user_id}/friends")
# async def get_user_friends(user_id: int, page_index: int, page_size: Optional[int]= 10):
# 	return {
# 		"user id": f"{user_id}",
# 		"page index": f"{page_index}",
# 		"page size": f"{page_size}"
# 	}

if __name__ == "__main__":
	uvicorn.run("main:app", reload=True)
