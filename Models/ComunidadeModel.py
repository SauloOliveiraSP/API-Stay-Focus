from pydantic import BaseModel
from datetime import datetime

class Comunidade(BaseModel):
  pk_id: int
  ds_nome: str
  ds_imagem: str
  ds_descricao: str
  ds_link: str
  fk_usuariocriador: int
  dt_alteracao: datetime
  dt_inclusao: datetime

class ComunidadeUsuario(BaseModel):
  pk_id: int
  fk_comunidade: int
  fk_usuario: int
  dt_alteracao: datetime
  dt_inclusao: datetime

class ComunidadeInteracoes(BaseModel):
  pk_id: int
  fk_comunidade: int
  fk_usuario: int
  ds_interacao: str
  dt_alteracao: datetime
  dt_inclusao: datetime