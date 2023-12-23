from fastapi import FastAPI
from Repository import Repository
from Models.ConsultaModel import Consulta

app = FastAPI()
banco = Repository()


@app.post("/consulta/")
def criar_consulta(consulta: Consulta):
  banco.inserir_consulta(consulta)
  return {"mensagem": "Consulta criada com sucesso."}


@app.get("/consulta/")
def listar_consultas():
  return banco.selecionar_consultas()


@app.get("/consulta/{pk_id}")
def obter_consulta(pk_id: int):
  return banco.selecionar_consultaid(pk_id)


@app.put("/consulta/{pk_id}")
def atualizar_consulta(pk_id: int, atualiza_consulta: Consulta):
  consulta_existente = banco.selecionar_consultaid(pk_id)
  if consulta_existente:
    banco.atualizar_consulta(pk_id, atualiza_consulta)
    return {"mensagem": "Consulta atualizada com sucesso."}
  return {"mensagem": "Consulta não encontrada."}


@app.delete("/consulta/{pk_id}")
def remover_consulta(pk_id: int):
  consulta_existente = banco.selecionar_consultaid(pk_id)
  if consulta_existente:
    banco.deletar_consulta(pk_id)
    return {"mensagem": "Consulta deletada com sucesso."}
  return {"mensagem": "Consulta não encontrada."}
