from pydantic import BaseModel
import sqlite3
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from Repository import Repository

from Models.UsuarioModel import Usuario
from Models.ConsultaModel import Consulta
from Models.ComunidadeModel import Comunidade, ComunidadeUsuario, ComunidadeInteracoes
from Models.ClinicaModel import Clinica

app = FastAPI(
    title="API Stay Focus",
    description=
    "`API do aplicativo Stay Focus - Desenvolvido em 12/2023 por: Saulo de Oliveira, Lorrany Cesar Silva e Luiz Felipe Mesquita de Andrade.`"
)

banco = Repository()
print("iniciado")

# Configuração
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Controladores
### Usuario
@app.post("/usuarios/", name="Criar Usuário", tags=["Usuários"])
def criar_usuario(usuario: Usuario):
  banco.inserir_usuario(usuario)
  return {"mensagem": "Usuário criado com sucesso."}


@app.get("/usuarios/", name="Listar Usuários", tags=["Usuários"])
def listar_usuarios():
  return banco.selecionar_usuarios()


@app.get("/usuarios/{pk_id}", name="Selecionar Usuário", tags=["Usuários"])
def obter_usuario(pk_id: int):
  return banco.selecionar_usuarioid(pk_id)


@app.put("/usuarios/{pk_id}", name="Atualizar Usuário", tags=["Usuários"])
def atualizar_usuario(pk_id: int, novo_usuario: Usuario):
  usuario_existente = banco.selecionar_usuarioid(pk_id)
  if usuario_existente:
    banco.atualizar_usuario(pk_id, novo_usuario)
    return {"mensagem": "Usuário atualizado com sucesso."}
  return {"mensagem": "Usuário não encontrado."}


@app.delete("/usuarios/{pk_id}", name="Deletar Usuário", tags=["Usuários"])
def deletar_usuario(pk_id: int):
  usuario_existente = banco.selecionar_usuarioid(pk_id)
  if usuario_existente:
    banco.deletar_usuario(pk_id)
    return {"mensagem": "Usuário deletado com sucesso."}
  return {"mensagem": "Usuário não encontrado."}


### Consulta
@app.post("/consulta/", name="Criar Consulta", tags=["Consultas"])
def criar_consulta(consulta: Consulta):
  banco.inserir_consulta(consulta)
  return {"mensagem": "Consulta criada com sucesso."}


@app.get("/consulta/", name="Listar Consultas", tags=["Consultas"])
def listar_consultas():
  return banco.selecionar_consultas()


@app.get("/consulta/{pk_id}", name="Selecionar Consulta", tags=["Consultas"])
def obter_consulta(pk_id: int):
  return banco.selecionar_consultaid(pk_id)


@app.put("/consulta/{pk_id}", name="Atualizar Consulta", tags=["Consultas"])
def atualizar_consulta(pk_id: int, atualiza_consulta: Consulta):
  consulta_existente = banco.selecionar_consultaid(pk_id)
  if consulta_existente:
    banco.atualizar_consulta(pk_id, atualiza_consulta)
    return {"mensagem": "Consulta atualizada com sucesso."}
  return {"mensagem": "Consulta não encontrada."}


@app.delete("/consulta/{pk_id}", name="Deletar Consulta", tags=["Consultas"])
def remover_consulta(pk_id: int):
  consulta_existente = banco.selecionar_consultaid(pk_id)
  if consulta_existente:
    banco.deletar_consulta(pk_id)
    return {"mensagem": "Consulta deletada com sucesso."}
  return {"mensagem": "Consulta não encontrada."}


### Comunidade
@app.post("/comunidade/", name="Criar Comunidade", tags=["Comunidades"])
def criar_comunidade(comunidade: Comunidade):
  banco.inserir_comunidade(comunidade)
  return {"mensagem": "Comunidade criada com sucesso."}


@app.get("/comunidade/", name="Listar Comunidades", tags=["Comunidades"])
def listar_comunidades():
  return banco.selecionar_comunidades()


@app.get("/comunidade/{pk_id}",
         name="Selecionar Comunidade",
         tags=["Comunidades"])
def obter_comunidade(pk_id: int):
  return banco.selecionar_comunidadeid(pk_id)


@app.put("/comunidade/{pk_id}",
         name="Atualizar Comunidade",
         tags=["Comunidades"])
def atualizar_comunidade(pk_id: int, atualiza_comunidade: Comunidade):
  comunidade_existente = banco.selecionar_comunidadeid(pk_id)
  if comunidade_existente:
    banco.atualizar_comunidade(pk_id, atualiza_comunidade)
    return {"mensagem": "Comunidade atualizada com sucesso."}
  return {"mensagem": "Comunidade não encontrada."}


@app.delete("/comunidade/{pk_id}",
            name="Deletar Comunidade",
            tags=["Comunidades"])
def remover_comunidade(pk_id: int):
  comunidade_existente = banco.selecionar_comunidadeid(pk_id)
  if comunidade_existente:
    banco.deletar_comunidade(pk_id)
    return {"mensagem": "Comunidade deletada com sucesso."}
  return {"mensagem": "Comunidade não encontrada."}


### ComunidadeUsuario
@app.post("/comunidadeusuario/",
          name="Criar Comunidade Usuário",
          tags=["Comunidade Usuários"])
def criar_comunidadeusuario(comunidadeusuario: ComunidadeUsuario):
  banco.inserir_comunidadeusuario(comunidadeusuario)
  return {"mensagem": "ComunidadeUsuario criada com sucesso."}


@app.get("/comunidadeusuario/",
         name="Listar Comunidade Usuário",
         tags=["Comunidade Usuários"])
def listar_comunidadeusuarios():
  return banco.selecionar_comunidadeusuarios()


@app.get("/comunidadeusuario/{pk_id}",
         name="Selecionar Comunidade Usuário",
         tags=["Comunidade Usuários"])
def obter_comunidadeusuario(pk_id: int):
  return banco.selecionar_comunidadeusuarioid(pk_id)


@app.put("/comunidadeusuario/{pk_id}",
         name="Atualizar Comunidade Usuário",
         tags=["Comunidade Usuários"])
def atualizar_comunidadeusuario(pk_id: int,
                                atualiza_comunidadeusuario: ComunidadeUsuario):
  comunidadeusuario_existente = banco.selecionar_comunidadeusuarioid(pk_id)
  if comunidadeusuario_existente:
    banco.atualizar_comunidadeusuario(pk_id, atualiza_comunidadeusuario)
    return {"mensagem": "ComunidadeUsuario atualizada com sucesso."}
  return {"mensagem": "ComunidadeUsuario não encontrada."}


@app.delete("/comunidadeusuario/{pk_id}",
            name="Deletar Comunidade Usuário",
            tags=["Comunidade Usuários"])
def remover_comunidadeusuario(pk_id: int):
  comunidadeusuario_existente = banco.selecionar_comunidadeusuarioid(pk_id)
  if comunidadeusuario_existente:
    banco.deletar_comunidadeusuario(pk_id)
    return {"mensagem": "ComunidadeUsuario deletada com sucesso."}
  return {"mensagem": "ComunidadeUsuario não encontrada."}


## ComunidadeInteracoes
@app.post("/comunidadeinteracoes/",
          name="Criar Comunidade Interações",
          tags=["Comunidade Interações"])
def criar_comunidadeinteracoes(comunidadeinteracoes: ComunidadeInteracoes):
  banco.inserir_comunidadeinteracoes(comunidadeinteracoes)
  return {"mensagem": "ComunidadeInteracoes criada com sucesso."}


@app.get("/comunidadeinteracoes/",
         name="Listar Comunidade Interações",
         tags=["Comunidade Interações"])
def listar_comunidadeinteracoes():
  return banco.selecionar_comunidadeinteracoes()


@app.get("/comunidadeinteracoes/{pk_id}",
         name="Selecionar Comunidade Interações",
         tags=["Comunidade Interações"])
def obter_comunidadeinteracoes(pk_id: int):
  return banco.selecionar_comunidadeinteracoesid(pk_id)


@app.put("/comunidadeinteracoes/{pk_id}",
         name="Atualizar Comunidade Interações",
         tags=["Comunidade Interações"])
def atualizar_comunidadeinteracoes(
    pk_id: int, atualiza_comunidadeinteracoes: ComunidadeInteracoes):
  comunidadeinteracoes_existente = banco.selecionar_comunidadeinteracoesid(
      pk_id)
  if comunidadeinteracoes_existente:
    banco.atualizar_comunidadeinteracoes(pk_id, atualiza_comunidadeinteracoes)
    return {"mensagem": "ComunidadeInteracoes atualizada com sucesso."}
  return {"mensagem": "ComunidadeInteracoes não encontrada."}


@app.delete("/comunidadeinteracoes/{pk_id}",
            name="Deletar Comunidade Interações",
            tags=["Comunidade Interações"])
def remover_comunidadeinteracoes(pk_id: int):
  comunidadeinteracoes_existente = banco.selecionar_comunidadeinteracoesid(
      pk_id)
  if comunidadeinteracoes_existente:
    banco.deletar_comunidadeinteracoes(pk_id)
    return {"mensagem": "ComunidadeInteracoes deletada com sucesso."}
  return {"mensagem": "ComunidadeInteracoes não encontrada."}


### Clinica
@app.post("/clinica/", name="Criar Clínica", tags=["Clínicas"])
def inserir_clinica(clinica: Clinica):
  banco.inserir_clinica(clinica)
  return {"mensagem": "Clinica criada com sucesso."}


@app.get("/clinica/", name="Listar Clínicas", tags=["Clínicas"])
def listar_clinicas():
  return banco.selecionar_clinicas()


@app.get("/clinica/{pk_id}", name="Selecionar Clínica", tags=["Clínicas"])
def obter_clinica(pk_id: int):
  return banco.selecionar_clinicaid(pk_id)


@app.put("/clinica/{pk_id}", name="Atualizar Clínica", tags=["Clínicas"])
def atualizar_clinica(pk_id: int, atualiza_clinica: Clinica):
  atualizar_clinicaid = banco.selecionar_clinicaid(pk_id)
  if atualizar_clinicaid:
    banco.atualizar_clinica(pk_id, atualiza_clinica)
    return {"mensagem": "Clinica atualizada com sucesso."}
  return {"mensagem": "Clinica não encontrada."}


@app.delete("/clinia/{pk_id}", name="Deletar Clínica", tags=["Clínicas"])
def remover_clinica(pk_id: int):
  buscar_clinicaid = banco.selecionar_clinicaid(pk_id)
  if buscar_clinicaid:
    banco.deletar_clinica(pk_id)
    return {"mensagem": "Clinica deletada com sucesso."}
  return {"mensagem": "Clinica não encontrada"}


### Main
@app.get("/", tags=["Main"])
def main():
  return RedirectResponse(url="/docs")


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
