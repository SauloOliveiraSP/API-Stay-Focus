from pydantic import BaseModel
from datetime import datetime

class Clinica(BaseModel):
  pk_id: int
  fk_usuarioclinica: int
  ds_nome: str
  ds_descricao: str
  ds_imagem: str
  ds_link: str
  ds_endereco: str
  nr_endereco: str
  nr_cep: str
  nr_telefone: str
  ds_email: str
  nr_cnpj: str
  dt_alteracao: datetime
  dt_inclusao: datetime