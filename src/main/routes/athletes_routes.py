from fastapi import APIRouter
from fastapi.responses import JSONResponse

athletes_routes = APIRouter(tags=["athletes"])

@athletes_routes.post("/athletes")
async def criar_atleta():

    return JSONResponse(
        status_code=201, 
        content={"message": "Atleta criado com sucesso"}
    )