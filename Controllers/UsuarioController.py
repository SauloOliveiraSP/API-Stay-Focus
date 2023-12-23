from fastapi import FastAPI
from Repository import Repository
from Models.UsuarioModel import Usuario

app = FastAPI()
banco = Repository()


@app.post("/usuario/")
def criar_usuario(usuario: Usuario):
  banco.inserir_usuario(usuario)
  return {"mensagem": "Usuário criado com sucesso."}


@app.get("/usuario/")
def listar_usuarios():
  return banco.selecionar_usuarios()


@app.get("/usuario/{pk_id}")
def obter_usuario(pk_id: int):
  return banco.selecionar_usuarioid(pk_id)


@app.put("/usuario/{pk_id}")
def atualizar_usuario(pk_id: int, atualiza_usuario: Usuario):
  usuario_existente = banco.selecionar_usuarioid(pk_id)
  if usuario_existente:
    banco.atualizar_usuario(pk_id, atualiza_usuario)
    return {"mensagem": "Usuário atualizado com sucesso."}
  return {"mensagem": "Usuário não encontrado."}


@app.delete("/usuario/{pk_id}")
def remover_usuario(pk_id: int):
  usuario_existente = banco.selecionar_usuarioid(pk_id)
  if usuario_existente:
    banco.deletar_usuario(pk_id)
    return {"mensagem": "Usuário deletado com sucesso."}
  return {"mensagem": "Usuário não encontrado."}
