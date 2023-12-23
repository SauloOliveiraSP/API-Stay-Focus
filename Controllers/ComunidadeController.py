from fastapi import FastAPI
from Repository import Repository
from Models.ComunidadeModel import Comunidade, ComunidadeUsuario, ComunidadeInteracoes

app = FastAPI()
banco = Repository()

### Comunidade
@app.post("/comunidade/")
def criar_comunidade(comunidade: Comunidade):
  banco.inserir_comunidade(comunidade)
  return {"mensagem": "Comunidade criada com sucesso."}


@app.get("/comunidade/")
def listar_comunidades():
  return banco.selecionar_comunidades()


@app.get("/comunidade/{pk_id}")
def obter_comunidade(pk_id: int):
  return banco.selecionar_comunidadeid(pk_id)


@app.put("/comunidade/{pk_id}")
def atualizar_comunidade(pk_id: int, atualiza_comunidade: Comunidade):
  comunidade_existente = banco.selecionar_comunidadeid(pk_id)
  if comunidade_existente:
    banco.atualizar_comunidade(pk_id, atualiza_comunidade)
    return {"mensagem": "Comunidade atualizada com sucesso."}
  return {"mensagem": "Comunidade não encontrada."}


@app.delete("/comunidade/{pk_id}")
def remover_comunidade(pk_id: int):
  comunidade_existente = banco.selecionar_comunidadeid(pk_id)
  if comunidade_existente:
    banco.deletar_comunidade(pk_id)
    return {"mensagem": "Comunidade deletada com sucesso."}
  return {"mensagem": "Comunidade não encontrada."}


### ComunidadeUsuario
@app.post("/comunidadeusuario/")
def criar_comunidadeusuario(comunidadeusuario: ComunidadeUsuario):
  banco.inserir_comunidadeusuario(comunidadeusuario)
  return {"mensagem": "ComunidadeUsuario criada com sucesso."}


@app.get("/comunidadeusuario/")
def listar_comunidadeusuarios():
  return banco.selecionar_comunidadeusuarios()


@app.get("/comunidadeusuario/{pk_id}")
def obter_comunidadeusuario(pk_id: int):
  return banco.selecionar_comunidadeusuarioid(pk_id)


@app.put("/comunidadeusuario/{pk_id}")
def atualizar_comunidadeusuario(pk_id: int,
                                atualiza_comunidadeusuario: ComunidadeUsuario):
  comunidadeusuario_existente = banco.selecionar_comunidadeusuarioid(
      pk_id)
  if comunidadeusuario_existente:
    banco.atualizar_comunidadeusuario(pk_id,
                                      atualiza_comunidadeusuario)
    return {"mensagem": "ComunidadeUsuario atualizada com sucesso."}
  return {"mensagem": "ComunidadeUsuario não encontrada."}


@app.delete("/comunidadeusuario/{pk_id}")
def remover_comunidadeusuario(pk_id: int):
  comunidadeusuario_existente = banco.selecionar_comunidadeusuarioid(
      pk_id)
  if comunidadeusuario_existente:
    banco.deletar_comunidadeusuario(pk_id)
    return {"mensagem": "ComunidadeUsuario deletada com sucesso."}
  return {"mensagem": "ComunidadeUsuario não encontrada."}


## ComunidadeInterações
@app.post("/comunidadeinteracoes/")
def criar_comunidadeinteracoes(comunidadeinteracoes: ComunidadeInteracoes):
  banco.inserir_comunidadeinteracoes(comunidadeinteracoes)
  return {"mensagem": "ComunidadeInteracoes criada com sucesso."}


@app.get("/comunidadeinteracoes/")
def listar_comunidadeinteracoes():
  return banco.selecionar_comunidadeinteracoes()


@app.get("/comunidadeinteracoes/{pk_id}")
def obter_comunidadeinteracoes(pk_id: int):
  return banco.selecionar_comunidadeinteracoesid(pk_id)


@app.put("/comunidadeinteracoes/{pk_id}")
def atualizar_comunidadeinteracoes(
    pk_id: int,
    atualiza_comunidadeinteracoes: ComunidadeInteracoes):
  comunidadeinteracoes_existente = banco.selecionar_comunidadeinteracoesid(
      pk_id)
  if comunidadeinteracoes_existente:
    banco.atualizar_comunidadeinteracoes(pk_id,
                                         atualiza_comunidadeinteracoes)
    return {"mensagem": "ComunidadeInteracoes atualizada com sucesso."}
  return {"mensagem": "ComunidadeInteracoes não encontrada."}


@app.delete("/comunidadeinteracoes/{pk_id}")
def remover_comunidadeinteracoes(pk_id: int):
  comunidadeinteracoes_existente = banco.selecionar_comunidadeinteracoesid(
      pk_id)
  if comunidadeinteracoes_existente:
    banco.deletar_comunidadeinteracoes(pk_id)
    return {"mensagem": "ComunidadeInteracoes deletada com sucesso."}
  return {"mensagem": "ComunidadeInteracoes não encontrada."}
