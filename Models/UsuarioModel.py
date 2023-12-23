from pydantic import BaseModel
from datetime import date
from datetime import datetime

class Usuario(BaseModel):
  pk_id: int
  ds_nome: str
  ds_email: str
  nr_telefone: str
  nr_cpfcnpj: str
  nr_cep: str
  ds_endereco: str
  nr_endereco: str
  dt_nascimento: date
  ds_senha: str
  nr_crp: str
  ds_instituicao: str
  tg_tipo: int
  dt_alteracao: datetime
  dt_inclusao: datetime