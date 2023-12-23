from fastapi import FastAPI
from Repository import Repository
from Models.ClinicaModel import Clinica

app = FastAPI()
banco = Repository()


@app.post("/clinica/")
def inserir_clinica(clinica: Clinica):
  banco.inserir_clinica(clinica)
  return {"mensagem": "Clinica criada com sucesso."}


@app.get("/clinica/")
def listar_clinicas():
  return banco.selecionar_clinicas()


@app.get("/clinica/{pk_id}")
def obter_clinica(pk_id: int):
  return banco.selecionar_clinicaid(pk_id)


@app.put("/clinica/{pk_id}")
def atualizar_clinica(pk_id: int, atualiza_clinica: Clinica):
  atualizar_clinicaid = banco.selecionar_clinicaid(pk_id)
  if atualizar_clinicaid:
    banco.atualizar_clinica(pk_id, atualiza_clinica)
    return {"mensagem": "Clinica atualizada com sucesso."}
  return {"mensagem": "Clinica não encontrada."}


@app.delete("/clinia/{pk_id}")
def remover_clinica(pk_id: int):
  buscar_clinicaid = banco.selecionar_clinicaid(pk_id)
  if buscar_clinicaid:
    banco.deletar_clinica(pk_id)
    return {"mensagem": "Clinica deletada com sucesso."}
  return {"mensagem": "Clinica não encontrada"}
