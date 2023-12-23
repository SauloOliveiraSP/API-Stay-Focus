import sqlite3
from Models.UsuarioModel import Usuario
from Models.ClinicaModel import Clinica
from Models.ConsultaModel import Consulta
from Models.ComunidadeModel import Comunidade, ComunidadeInteracoes, ComunidadeUsuario
from datetime import datetime


class Repository:

  def __init__(self, nome_do_banco='exemplo.db'):
    self.database_name = nome_do_banco
    self.conexao = sqlite3.connect(nome_do_banco)
    self.cursor = self.conexao.cursor()

    self.tb_clinica()
    self.tb_consulta()
    self.tb_usuario()
    self.tb_comunidade()
    self.tb_comunidadeusuario()
    self.tb_comunidadeinteracoes()

    print("banco de dados iniciado!!!!")

  ### Tabelas
  def tb_usuario(self):
    create_tb_usuario = '''
      CREATE TABLE IF NOT EXISTS tb_usuario (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ds_nome TEXT,
        ds_email TEXT,
        nr_telefone TEXT,
        nr_cpfcnpj TEXT,
        nr_cep TEXT,
        ds_endereco TEXT,
        nr_endereco TEXT,
        dt_nascimento DATE,
        ds_senha TEXT,
        nr_crp TEXT,
        ds_instituicao TEXT,
        tg_tipo INTEGER,
        dt_alteracao DATETIME,
        dt_inclusao DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    '''
    self.cursor.execute(create_tb_usuario)
    self.conexao.commit()

  def tb_clinica(self):
    create_tb_clinica = '''
      CREATE TABLE IF NOT EXISTS tb_clinica (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_usuarioclinica INTEGER NOT NULL,
        ds_nome TEXT,
        ds_descricao TEXT,
        ds_imagem TEXT,
        ds_link TEXT,
        ds_endereco TEXT,
        nr_endereco TEXT,
        nr_cep TEXT,
        nr_telefone TEXT,
        ds_email TEXT,
        nr_cnpj TEXT,
        dt_alteracao DATETIME,
        dt_inclusao DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    '''
    self.cursor.execute(create_tb_clinica)
    self.conexao.commit()

  def tb_consulta(self):
    create_tb_consulta = '''
      CREATE TABLE IF NOT EXISTS tb_consulta (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_usuario INTEGER,
        fk_usuarioprofissional INTEGER,
        nr_chamadaconsulta TEXT,
        ds_chamada TEXT,
        dt_alteracao DATETIME,
        dt_inclusao DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    '''
    self.cursor.execute(create_tb_consulta)
    self.conexao.commit()

  def tb_comunidade(self):
    create_tb_comunidade = '''
      CREATE TABLE IF NOT EXISTS tb_comunidade (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ds_nome TEXT,
        ds_imagem TEXT,
        ds_descricao TEXT,
        ds_link TEXT,
        fk_usuariocriador INTEGER,
        dt_alteracao DATETIME,
        dt_inclusao DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    '''
    self.cursor.execute(create_tb_comunidade)
    self.conexao.commit()

  def tb_comunidadeusuario(self):
    create_tb_comunidadeusuario = '''
      CREATE TABLE IF NOT EXISTS tb_comunidadeusuario (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_comunidade INTEGER,
        fk_usuario INTEGER,
        dt_alteracao DATETIME,
        dt_inclusao DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    '''
    self.cursor.execute(create_tb_comunidadeusuario)
    self.conexao.commit()

  def tb_comunidadeinteracoes(self):
    create_tb_comunidadeinteracoes = '''
      CREATE TABLE IF NOT EXISTS tb_comunidadeinteracoes (
        pk_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fk_comunidade INTEGER,
        fk_usuario INTEGER,
        ds_interacao TEXT,
        dt_alteracao DATETIME,
        dt_inclusao DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    '''
    self.cursor.execute(create_tb_comunidadeinteracoes)
    self.conexao.commit()

  ### CRUD
  ### Usuario
  def inserir_usuario(self, usuario: Usuario):
    sql_insert_data = '''
      INSERT INTO tb_usuario (ds_nome, ds_email, nr_telefone, nr_cpfcnpj, nr_cep, 
      ds_endereco, nr_endereco, dt_nascimento, ds_senha, nr_crp, ds_instituicao, 
      tg_tipo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_insert_data,
        (usuario.ds_nome, usuario.ds_email, usuario.nr_telefone,
         usuario.nr_cpfcnpj, usuario.nr_cep, usuario.ds_endereco,
         usuario.nr_endereco, usuario.dt_nascimento, usuario.ds_senha,
         usuario.nr_crp, usuario.ds_instituicao, usuario.tg_tipo))
    self.conexao.commit()

  def selecionar_usuarios(self):
    sql_select_all = '''
      SELECT * FROM tb_usuario
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_all)
    print("executando busca")
    return self.cursor.fetchall()

  def selecionar_usuarioid(self, pk_id: int):
    sql_select_id = '''
      SELECT * FROM tb_usuario WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_id, (pk_id, ))
    return self.cursor.fetchone()

  def atualizar_usuario(self, pk_id: int, atulizar_usuario: Usuario):
    sql_update_data = '''
      UPDATE tb_usuario SET ds_nome = ?, ds_email = ?, nr_telefone = ?, nr_cpfcnpj = ?,
      nr_cep = ?, ds_endereco = ?, nr_endereco = ?, dt_nascimento = ?, ds_senha = ?,
      nr_crp = ?, ds_instituicao = ?, tg_tipo = ?, dt_alteracao = ? WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_update_data,
        (atulizar_usuario.ds_nome, atulizar_usuario.ds_email,
         atulizar_usuario.nr_telefone, atulizar_usuario.nr_cpfcnpj,
         atulizar_usuario.nr_cep, atulizar_usuario.ds_endereco,
         atulizar_usuario.nr_endereco, atulizar_usuario.dt_nascimento,
         atulizar_usuario.ds_senha, atulizar_usuario.nr_crp,
         atulizar_usuario.ds_instituicao, atulizar_usuario.tg_tipo,
         datetime.now(), pk_id))
    self.conexao.commit()
    self.cursor.close()

  def deletar_usuario(self, pk_id: int):
    sql_delete_data = '''
      DELETE FROM tb_usuario WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_delete_data, (pk_id, ))
    self.conexao.commit()
    self.cursor.close()

  ### Clinica
  def inserir_clinica(self, clinica: Clinica):
    sql_insert_data = '''
      INSERT INTO tb_clinica (fk_usuarioclinica, ds_nome, ds_descricao, ds_imagem,
      ds_link, ds_endereco, nr_endereco, nr_cep, nr_telefone, ds_email, nr_cnpj)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_insert_data,
        (clinica.fk_usuarioclinica, clinica.ds_nome, clinica.ds_descricao,
         clinica.ds_imagem, clinica.ds_link, clinica.ds_endereco,
         clinica.nr_endereco, clinica.nr_cep, clinica.nr_telefone,
         clinica.ds_email, clinica.nr_cnpj))
    self.conexao.commit()
    self.cursor.close()

  def selecionar_clinicas(self):
    sql_select_all = '''
      SELECT * FROM tb_clinica
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_all)
    print("executando busca")
    return self.cursor.fetchall()

  def selecionar_clinicaid(self, pk_id: int):
    sql_select_id = '''
      SELECT * FROM tb_clinica WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_id, (pk_id, ))
    return self.cursor.fetchone()

  def atualizar_clinica(self, pk_id: int, atualizar_clinica: Clinica):
    sql_update_data = '''
      UPDATE tb_clinica SET fk_usuarioclinica = ?, ds_nome = ?, ds_descricao = ?,
      ds_imagem = ?, ds_link = ?, ds_endereco = ?, nr_endereco = ?,
      nr_cep = ?, nr_telefone = ?, ds_email = ?, nr_cnpj = ?,
      dt_alteracao = ? WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_update_data,
        (atualizar_clinica.fk_usuarioclinica, atualizar_clinica.ds_nome,
         atualizar_clinica.ds_descricao, atualizar_clinica.ds_imagem,
         atualizar_clinica.ds_link, atualizar_clinica.ds_endereco,
         atualizar_clinica.nr_endereco, atualizar_clinica.nr_cep,
         atualizar_clinica.nr_telefone, atualizar_clinica.ds_email,
         atualizar_clinica.nr_cnpj, datetime.now(), pk_id))
    self.conexao.commit()
    self.cursor.close()

  def deletar_clinica(self, pk_id: int):
    sql_delete_data = '''
      DELETE FROM tb_clinica WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_delete_data, (pk_id, ))
    self.conexao.commit()
    self.cursor.close()

  ### Consulta
  def inserir_consulta(self, consulta: Consulta):
    sql_insert_data = '''
      INSERT INTO tb_consulta (fk_usuario, fk_usuarioprofissional,
      nr_chamadaconsulta, ds_chamada)
      VALUES (?, ?, ?, ?)
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_insert_data,
                        (consulta.fk_usuario, consulta.fk_usuarioprofissional,
                         consulta.nr_chamadaconsulta, consulta.ds_chamada))
    self.conexao.commit()
    self.cursor.close()

  def selecionar_consultas(self):
    sql_select_all = '''
      SELECT * FROM tb_consulta
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_all)
    print("executando busca")
    return self.cursor.fetchall()

  def selecionar_consultaid(self, pk_id: int):
    sql_select_id = '''
      SELECT * FROM tb_consulta WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_id, (pk_id, ))
    return self.cursor.fetchone()

  def atualizar_consulta(self, pk_id: int, atualizar_consulta: Consulta):
    sql_update_data = '''
      UPDATE tb_consulta SET fk_usuario = ?, fk_usuarioprofissional = ?,
      nr_chamadaconsulta = ?, ds_chamada = ?, dt_alteracao = ? 
      WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_update_data,
        (atualizar_consulta.fk_usuario,
         atualizar_consulta.fk_usuarioprofissional,
         atualizar_consulta.nr_chamadaconsulta, atualizar_consulta.ds_chamada,
         datetime.now(), pk_id))
    self.conexao.commit()
    self.cursor.close()

  def deletar_consulta(self, pk_id: int):
    sql_delete_data = '''
      DELETE FROM tb_consulta WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_delete_data, (pk_id, ))
    self.conexao.commit()
    self.cursor.close()

  ### Comunidade
  def inserir_comunidade(self, comunidade: Comunidade):
    sql_insert_data = '''
      INSERT INTO tb_comunidade (ds_nome, ds_imagem,
      ds_descricao, ds_link, fk_usuariocriador)
      VALUES (?, ?, ?, ?, ?)
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_insert_data,
        (comunidade.ds_nome, comunidade.ds_imagem, comunidade.ds_descricao,
         comunidade.ds_link, comunidade.fk_usuariocriador))
    self.conexao.commit()
    self.cursor.close()

  def selecionar_comunidades(self):
    sql_select_all = '''
      SELECT * FROM tb_comunidade
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_all)
    print("executando busca")
    return self.cursor.fetchall()

  def selecionar_comunidadeid(self, pk_id: int):
    sql_select_id = '''
      SELECT * FROM tb_comunidade WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_id, (pk_id, ))
    return self.cursor.fetchone()

  def atualizar_comunidade(self, pk_id: int,
                           atualizar_comunidade: Comunidade):
    sql_update_data = '''
      UPDATE tb_consulta SET ds_nome = ?, ds_imagem = ?,
      ds_descricao = ?, ds_link = ?, fk_usuariocriador = ?, dt_alteracao = ? 
      WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_update_data,
        (atualizar_comunidade.ds_nome, atualizar_comunidade.ds_imagem,
         atualizar_comunidade.ds_descricao,
         atualizar_comunidade.ds_link, atualizar_comunidade.fk_usuariocriador,
         datetime.now(), pk_id))
    self.conexao.commit()
    self.cursor.close()

  def deletar_comunidade(self, pk_id: int):
    sql_delete_data = '''
      DELETE FROM tb_comunidade WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_delete_data, (pk_id, ))
    self.conexao.commit()
    self.cursor.close()

  ### ComunidadeUsuario
  def inserir_comunidadeusuario(self, comunidadeusuario: ComunidadeUsuario):
    sql_insert_data = '''
      INSERT INTO tb_comunidadeusuario (fk_comunidade, fk_usuario)
      VALUES (?, ?)
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_insert_data,
        (comunidadeusuario.fk_comunidade, comunidadeusuario.fk_usuario))
    self.conexao.commit()
    self.cursor.close()

  def selecionar_comunidadeusuarios(self):
    sql_select_all = '''
      SELECT * FROM tb_comunidadeusuario
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_all)
    print("executando busca")
    return self.cursor.fetchall()

  def selecionar_comunidadeusuarioid(self, pk_id: int):
    sql_select_id = '''
      SELECT * FROM tb_comunidadeusuario WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_id, (pk_id, ))
    return self.cursor.fetchone()

  def atualizar_comunidadeusuario(
      self, pk_id: int,
      atualizar_comunidadeusuario: ComunidadeUsuario):
    sql_update_data = '''
      UPDATE tb_comunidadeusuario SET fk_comunidade = ?, fk_usuario = ?, 
      dt_alteracao = ? WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_update_data,
                        (atualizar_comunidadeusuario.fk_comunidade,
                         atualizar_comunidadeusuario.fk_usuario,
                         datetime.now(), pk_id))
    self.conexao.commit()
    self.cursor.close()

  def deletar_comunidadeusuario(self, pk_id: int):
    sql_delete_data = '''
      DELETE FROM tb_comunidadeusuario WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_delete_data, (pk_id, ))
    self.conexao.commit()
    self.cursor.close()

  ### ComunidadeInteracoes
  def inserir_comunidadeinteracoes(self,
                                   comunidadeinteracoes: ComunidadeInteracoes):
    sql_insert_data = '''
      INSERT INTO tb_comunidadeinteracoes (fk_comunidade, fk_usuario, ds_interacao)
      VALUES (?, ?, ?)
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(
        sql_insert_data,
        (comunidadeinteracoes.fk_comunidade, comunidadeinteracoes.fk_usuario,
         comunidadeinteracoes.ds_interacao))
    self.conexao.commit()
    self.cursor.close()

  def selecionar_comunidadeinteracoes(self):
    sql_select_all = '''
      SELECT * FROM tb_comunidadeinteracoes
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_all)
    print("executando busca")
    return self.cursor.fetchall()

  def selecionar_comunidadeinteracoesid(self, pk_id: int):
    sql_select_id = '''
      SELECT * FROM tb_comunidadeinteracoes WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_select_id, (pk_id, ))
    return self.cursor.fetchone()

  def atualizar_comunidadeinteracoes(
      self, pk_id: int,
      atualizar_comunidadeinteracoes: ComunidadeInteracoes):
    sql_update_data = '''
      UPDATE tb_comunidadeinteracoes SET fk_comunidade = ?, fk_usuario = ?, 
      ds_interacao = ?, dt_alteracao = ? WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_update_data,
                        (atualizar_comunidadeinteracoes.fk_comunidade,
                         atualizar_comunidadeinteracoes.fk_usuario,
                         atualizar_comunidadeinteracoes.ds_interacao,
                         datetime.now(), pk_id))
    self.conexao.commit()
    self.cursor.close()

  def deletar_comunidadeinteracoes(self, pk_id: int):
    sql_delete_data = '''
      DELETE FROM tb_comunidadeinteracoes WHERE pk_id = ?
    '''
    self.conexao = sqlite3.connect(self.database_name)
    self.cursor = self.conexao.cursor()
    self.cursor.execute(sql_delete_data, (pk_id, ))
    self.conexao.commit()
    self.cursor.close()
