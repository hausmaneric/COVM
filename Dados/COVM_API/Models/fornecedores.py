from typing import Any, overload
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Fornecedores(BaseClass):
    id              = 0
    nome            = ''
    endereco        = ''
    numero          = ''
    complemento     = ''
    bairro          = ''
    uf              = 0
    cidade          = 0
    cep             = ''
    telefone_1      = ''
    telefone_2      = ''
    email           = ''
    cnpj            = ''
    cpf             = ''
    rg              = ''
    nomeuf          = ''
    nomecidade      = ''
    fantasia        = ''

    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id             = 0
        self.nome           = ''
        self.endereco       = ''
        self.numero         = ''
        self.complemento    = ''
        self.bairro         = ''
        self.uf             = 0
        self.cidade         = 0
        self.cep            = ''
        self.telefone_1     = ''
        self.telefone_2     = ''
        self.email          = ''
        self.cnpj           = ''
        self.cpf            = ''
        self.rg             = ''
        self.nomeuf         = ''
        self.nomecidade     = ''
        self.fantasia       = ''

def getFornecedores():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT Id, Nome, Endereco, Numero, Complemento, Bairro, UF, Cidade, Cep,
               Telefone_1, Telefone_2, Email, CNPJ, CPF, RG, UF_Nome, Cidade_Nome, Fantasia
        FROM Fornecedores
        """
    )

    records = SQL.cur.fetchall()
    fornecedor_list = []

    for r in records:
        fornecedor              = Fornecedores()
        fornecedor.id           = r[0]
        fornecedor.nome         = r[1]
        fornecedor.endereco     = r[2]
        fornecedor.numero       = r[3]
        fornecedor.complemento  = r[4]
        fornecedor.bairro       = r[5]
        fornecedor.uf           = r[6]
        fornecedor.cidade       = r[7]
        fornecedor.cep          = r[8]
        fornecedor.telefone_1   = r[9]
        fornecedor.telefone_2   = r[10]
        fornecedor.email        = r[11]
        fornecedor.cnpj         = r[12]
        fornecedor.cpf          = r[13]
        fornecedor.rg           = r[14]
        fornecedor.nomeuf       = r[15]
        fornecedor.nomecidade   = r[16]  
        fornecedor.fantasia     = r[17]  
        fornecedor_list.append(fornecedor.__dict__)

    SQL.cur.close()

    return fornecedor_list

def getFornecedor(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT Id, Nome, Endereco, Numero, Complemento, Bairro, UF, Cidade, Cep,
               Telefone_1, Telefone_2, Email, CNPJ, CPF, RG, UF_Nome, Cidade_Nome, Fantasia
        FROM Fornecedores
        WHERE Id = {id}
        """
    )

    records = SQL.cur.fetchall()
    fornecedor_list = []

    for r in records:
        fornecedor              = Fornecedores()
        fornecedor.id           = r[0]
        fornecedor.nome         = r[1]
        fornecedor.endereco     = r[2]
        fornecedor.numero       = r[3]
        fornecedor.complemento  = r[4]
        fornecedor.bairro       = r[5]
        fornecedor.uf           = r[6]
        fornecedor.cidade       = r[7]
        fornecedor.cep          = r[8]
        fornecedor.telefone_1   = r[9]
        fornecedor.telefone_2   = r[10]
        fornecedor.email        = r[11]
        fornecedor.cnpj         = r[12]
        fornecedor.cpf          = r[13]
        fornecedor.rg           = r[14]
        fornecedor.nomeuf       = r[15]
        fornecedor.nomecidade   = r[16] 
        fornecedor.fantasia     = r[17]
        fornecedor_list.append(fornecedor.__dict__)

    SQL.cur.close()

    return fornecedor_list

def postFornecedor(fornecedor: Fornecedores):
    nome            = fornecedor.nome
    endereco        = fornecedor.endereco
    numero          = fornecedor.numero
    complemento     = fornecedor.complemento
    bairro          = fornecedor.bairro
    uf              = fornecedor.uf
    cidade          = fornecedor.cidade
    cep             = fornecedor.cep
    telefone_1      = fornecedor.telefone_1
    telefone_2      = fornecedor.telefone_2
    email           = fornecedor.email
    cnpj            = fornecedor.cnpj
    cpf             = fornecedor.cpf
    rg              = fornecedor.rg
    nomeuf          = fornecedor.nomeuf    
    nomecidade      = fornecedor.nomecidade
    fantasia        = fornecedor.fantasia

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Fornecedores (Nome, Endereco, Numero, Complemento, Bairro, UF, Cidade, Cep,
                                  Telefone_1, Telefone_2, Email, CNPJ, CPF, RG, UF_Nome, Cidade_Nome, Fantasia )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            nome, endereco, numero, complemento, bairro, uf, cidade, cep,
            telefone_1, telefone_2, email, cnpj, cpf, rg, nomeuf, nomecidade, fantasia
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return fornecedor

def updateFornecedor(id: int, fornecedor: Fornecedores):
    nome            = fornecedor.nome
    endereco        = fornecedor.endereco
    numero          = fornecedor.numero
    complemento     = fornecedor.complemento
    bairro          = fornecedor.bairro
    uf              = fornecedor.uf
    cidade          = fornecedor.cidade
    cep             = fornecedor.cep
    telefone_1      = fornecedor.telefone_1
    telefone_2      = fornecedor.telefone_2
    email           = fornecedor.email
    cnpj            = fornecedor.cnpj
    cpf             = fornecedor.cpf
    rg              = fornecedor.rg
    nomeuf          = fornecedor.nomeuf    
    nomecidade      = fornecedor.nomecidade
    fantasia        = fornecedor.fantasia

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Fornecedores
        SET Nome = ?,
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
            UF_Nome = ?, 
            Cidade_Nome = ?,
            Fantasia = ?
        WHERE Id = ?;
        """,
        (
            nome, endereco, numero, complemento, bairro, uf, cidade, cep,
            telefone_1, telefone_2, email, cnpj, cpf, rg, nomeuf, nomecidade, fantasia, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return fornecedor


def deleteFornecedor(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Fornecedores WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}