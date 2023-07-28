from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from typing import List, Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Cliente(BaseModel):
    id: int
    nome: str
    cnpj: str
    logradouro: str
    bairro: str
    cidade: str
    estado: str
    pais: str
    status: str
    
clientes_db = [
    {
        "id": 1,
        "nome": "Cliente 1",
        "cnpj": "123456789",
        "logradouro": "Rua A",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "estado": "SP",
        "pais": "Brasil",
        "status": "Ativo"
    },
    {
        "id": 2,
        "nome": "Cliente 2",
        "cnpj": "987654321",
        "logradouro": "Avenida B",
        "bairro": "Centro",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "pais": "Brasil",
        "status": "Inativo"
    }
]

@app.middleware("http")
async def redirect_to_clientes(request: Request, call_next):
    if request.url.path == "/":
        response = RedirectResponse(url="/clientes/")
    else:
        response = await call_next(request)
    return response

@app.get("/clientes/", response_model=List[Cliente])
def get_clientes():
    return clientes_db

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def get_cliente(cliente_id: int):
    cliente = next((cli for cli in clientes_db if cli["id"] == cliente_id), None)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@app.post("/clientes/", response_model=Cliente)
def create_cliente(cliente: Cliente):
    clientes_db.append(cliente.dict())
    return cliente

@app.put("/clientes/{cliente_id}", response_model=Cliente)
def update_cliente(cliente_id: int, cliente: Cliente):
    index = next((i for i, cli in enumerate(clientes_db) if cli["id"] == cliente_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    clientes_db[index] = cliente.dict()
    return cliente

@app.patch("/clientes/{cliente_id}", response_model=Cliente)
def update_partial_cliente(cliente_id: int, cliente: Cliente):
    index = next((i for i, cli in enumerate(clientes_db) if cli["id"] == cliente_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    cliente_dict = cliente.dict(exclude_unset=True)
    clientes_db[index].update(cliente_dict)
    return clientes_db[index]

@app.delete("/clientes/{cliente_id}", response_model=Cliente)
def delete_cliente(cliente_id: int):
    cliente = next((cli for cli in clientes_db if cli["id"] == cliente_id), None)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    clientes_db.remove(cliente)
    return cliente


