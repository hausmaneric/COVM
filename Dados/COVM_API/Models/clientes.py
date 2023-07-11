from typing import Any, overload
from flask import jsonify
from dataaccess.db import *
from Models.baseClass import *
from datetime import date
from Models.codigo import *

class Clientes(BaseClass):
    id                 = 0
    nome               = ''
    fantasia           = ''
    pessoa             = 0
    endereco           = ''
    numero             = ''
    complemento        = ''
    bairro             = ''
    uf                 = 0
    cidade             = 0
    cep                = ''
    telefone_1         = ''
    telefone_2         = ''
    email              = ''
    cnpj               = ''
    cpf                = ''
    rg                 = ''
    data_nascimento    = ''
    sexo               = 0
    cadastro           = ''
    ultima_compra      = ''
    nomeuf             = ''
    nomecidade         = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id                 = 0
        self.nome               = ''
        self.fantasia           = ''
        self.pessoa             = 0
        self.endereco           = ''
        self.numero             = ''
        self.complemento        = ''
        self.bairro             = ''
        self.uf                 = 0
        self.cidade             = 0
        self.cep                = ''
        self.telefone_1         = ''
        self.telefone_2         = ''
        self.email              = ''
        self.cnpj               = ''
        self.cpf                = ''
        self.rg                 = ''
        self.data_nascimento    = ''
        self.sexo               = 0
        self.cadastro           = ''
        self.ultima_compra      = ''
        self.nomeuf             = ''
        self.nomecidade         = ''
        
def getClientes():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT Id, Nome, Fantasia, Pessoa, Endereco, Numero, Complemento, Bairro, UF, Cidade, Cep,
               Telefone_1, Telefone_2, Email, CNPJ, CPF, RG, DataNascimento, Sexo, Cadastro, Ultima_Compra, UF_Nome, Cidade_Nome
        FROM Clientes
        """
    )
    
    records = SQL.cur.fetchall()
    cliente_list = []
    
    for r in records:
        cliente                 = Clientes()
        cliente.id              = r[0]
        cliente.nome            = r[1]
        cliente.fantasia        = r[2]
        cliente.pessoa          = r[3]
        cliente.endereco        = r[4]
        cliente.numero          = r[5]
        cliente.complemento     = r[6]
        cliente.bairro          = r[7]
        cliente.uf              = r[8]
        cliente.cidade          = r[9]
        cliente.cep             = r[10]
        cliente.telefone_1      = r[11]
        cliente.telefone_2      = r[12]
        cliente.email           = r[13]
        cliente.cnpj            = r[14]
        cliente.cpf             = r[15]
        cliente.rg              = r[16]
        cliente.data_nascimento = r[17]
        cliente.sexo            = r[18]
        cliente.cadastro        = r[19]
        cliente.ultima_compra   = r[20]
        cliente.nomeuf          = r[21]
        cliente.nomecidade      = r[22]
        cliente_list.append(cliente.__dict__)
    
    SQL.cur.close()
    
    return cliente_list

def getCliente(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT Id, Nome, Fantasia, Pessoa, Endereco, Numero, Complemento, Bairro, UF, Cidade, Cep,
               Telefone_1, Telefone_2, Email, CNPJ, CPF, RG, DataNascimento, Sexo, Cadastro, Ultima_Compra, UF_Nome, Cidade_Nome
        FROM Clientes
        WHERE Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    cliente_list = []
    
    for r in records:
        cliente                 = Clientes()
        cliente.id              = r[0]
        cliente.nome            = r[1]
        cliente.fantasia        = r[2]
        cliente.pessoa          = r[3]
        cliente.endereco        = r[4]
        cliente.numero          = r[5]
        cliente.complemento     = r[6]
        cliente.bairro          = r[7]
        cliente.uf              = r[8]
        cliente.cidade          = r[9]
        cliente.cep             = r[10]
        cliente.telefone_1      = r[11]
        cliente.telefone_2      = r[12]
        cliente.email           = r[13]
        cliente.cnpj            = r[14]
        cliente.cpf             = r[15]
        cliente.rg              = r[16]
        cliente.data_nascimento = r[17]
        cliente.sexo            = r[18]
        cliente.cadastro        = r[19]
        cliente.ultima_compra   = r[20]
        cliente.nomeuf          = r[21]     
        cliente.nomecidade      = r[22]   
        cliente_list.append(cliente.__dict__)
    
    SQL.cur.close()
    
    return cliente_list

def postCliente(cliente: Clientes):
    nome                = cliente.nome
    fantasia            = cliente.fantasia
    pessoa              = cliente.pessoa
    endereco            = cliente.endereco
    numero              = cliente.numero
    complemento         = cliente.complemento
    bairro              = cliente.bairro
    uf                  = cliente.uf
    cidade              = cliente.cidade
    cep                 = cliente.cep
    telefone_1          = cliente.telefone_1
    telefone_2          = cliente.telefone_2
    email               = cliente.email
    cnpj                = cliente.cnpj
    cpf                 = cliente.cpf
    rg                  = cliente.rg
    data_nascimento     = cliente.data_nascimento
    sexo                = cliente.sexo
    cadastro            = cliente.cadastro
    ultima_compra       = cliente.ultima_compra
    nomeuf              = cliente.nomeuf
    nomecidade          = cliente.nomecidade

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Clientes (Nome, Fantasia, Pessoa, Endereco, Numero, Complemento, Bairro, UF, Cidade, Cep,
                              Telefone_1, Telefone_2, Email, CNPJ, CPF, RG, DataNascimento, Sexo, Cadastro, Ultima_Compra, UF_Nome, Cidade_Nome)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            nome, fantasia, pessoa, endereco, numero, complemento, bairro, uf, cidade, cep,
            telefone_1, telefone_2, email, cnpj, cpf, rg, data_nascimento, sexo, cadastro, ultima_compra, nomeuf, nomecidade
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return cliente

def updateCliente(id: int, cliente: Clientes):
    nome                = cliente.nome
    fantasia            = cliente.fantasia
    pessoa              = cliente.pessoa
    endereco            = cliente.endereco
    numero              = cliente.numero
    complemento         = cliente.complemento
    bairro              = cliente.bairro
    uf                  = cliente.uf
    cidade              = cliente.cidade
    cep                 = cliente.cep
    telefone_1          = cliente.telefone_1
    telefone_2          = cliente.telefone_2
    email               = cliente.email
    cnpj                = cliente.cnpj
    cpf                 = cliente.cpf
    rg                  = cliente.rg
    data_nascimento     = cliente.data_nascimento
    sexo                = cliente.sexo
    cadastro            = cliente.cadastro
    ultima_compra       = cliente.ultima_compra
    nomeuf              = cliente.nomeuf
    nomecidade          = cliente.nomecidade

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Clientes
        SET Nome = ?,
            Fantasia = ?,
            Pessoa = ?,
            Endereco = ?,
            Numero = ?,
            Complemento = ?,
            Bairro = ?,
            UF = ?,
            Cidade = ?,
            Cep = ?,
            Telefone_1 = ?,
            Telefone_2 = ?,
            Email = ?,
            CNPJ = ?,
            CPF = ?,
            RG = ?,
            DataNascimento = ?,
            Sexo = ?,
            Cadastro = ?,
            Ultima_Compra = ?,
            UF_Nome = ?,
            Cidade_Nome = ?
        WHERE Id = ?;
        """,
        (
            nome, fantasia, pessoa, endereco, numero, complemento, bairro, uf, cidade, cep,
            telefone_1, telefone_2, email, cnpj, cpf, rg, data_nascimento, sexo, cadastro, ultima_compra, nomeuf, nomecidade, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return cliente

def deleteCliente(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Clientes WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}

