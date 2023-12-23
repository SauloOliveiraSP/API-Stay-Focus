from pydantic import BaseModel
from datetime import datetime

class Consulta(BaseModel):
  pk_id: int
  fk_usuario: int
  fk_usuarioprofissional: int
  nr_chamadaconsulta: str
  ds_chamada: str
  dt_alteracao: datetime
  dt_inclusao: datetime
