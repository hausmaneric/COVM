from typing import Any, overload
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Funcionarios(BaseClass):
    id                  = 0
    nome                = ''
    identificacao       = ''
    cnpj                = ''
    cpf                 = ''
    rg                  = ''
    endereco            = ''
    numero              = ''
    complemento         = ''
    bairro              = ''
    uf                  = 0
    cidade              = 0
    cep                 = ''
    telefone_1          = ''
    telefone_2          = ''
    email               = ''
    salario             = 0
    m_quadrado          = 0.0
    diaria              = 0.0
    mensal              = 0.0
    data_nascimento     = ''
    admissao            = ''
    funcao              = 0
    senha               = ''
    comissao_calculo     = 0
    comissao_produto    = 0.0
    comissao_servico    = 0.0
    desconto            = 0.0
    tipo                = 0
    nometipo            = ''
    nomefuncao          = ''
    nomeuf              = ''   
    nomecidade          = ''

    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id                 = 0
        self.nome               = ''
        self.identificacao      = ''
        self.cnpj               = ''
        self.cpf                = ''
        self.rg                 = ''
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
        self.salario            = 0
        self.m_quadrado         = 0.0
        self.diaria             = 0.0
        self.mensal             = 0.0
        self.data_nascimento    = ''
        self.admissao           = ''
        self.funcao             = 0
        self.senha              = ''
        self.comissao_calculo   = 0
        self.comissao_produto   = 0.0
        self.comissao_servico   = 0.0
        self.desconto           = 0.0
        self.tipo               = 0
        self.nometipo           = ''
        self.nomefuncao         = ''
        self.nomeuf             = ''   
        self.nomecidade         = ''

def getFuncionarios():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
            f.Id, 
            f.Nome, 
            f.Identificacao, 
            f.CNPJ, 
            f.CPF, 
            f.RG, 
            f.Endereco, 
            f.Numero, 
            f.Complemento,
            f.Bairro, 
            f.UF, 
            f.Cidade, 
            f.Cep, 
            f.Telefone_1, 
            f.Telefone_2, 
            f.Email, 
            f.Salario,
            f.MQuadrado, 
            f.Diaria, 
            f.Mensal, 
            f.DataNascimento, 
            f.Admissao, 
            f.Funcao, 
            f.Senha,
            f.Comissao_Calculo, 
            f.Comissao_Produto, 
            f.Comissao_Servico, 
            f.Desconto, 
            f.Tipo,
            ft.nome as nometipo,
            ff.nome as nomefuncao,
            f.UF_Nome,
            f.Cidade_Nome
        FROM Funcionarios as f
        LEFT JOIN Funcionario_Tipo as ft ON f.Tipo = ft.id
        LEFT JOIN Funcionario_Funcao as ff ON f.Funcao = ff.id
        """
    )

    records = SQL.cur.fetchall()
    funcionario_list = []

    for r in records:
        funcionario                     = Funcionarios()
        funcionario.id                  = r[0]
        funcionario.nome                = r[1]
        funcionario.identificacao       = r[2]
        funcionario.cnpj                = r[3]
        funcionario.cpf                 = r[4]
        funcionario.rg                  = r[5]
        funcionario.endereco            = r[6]
        funcionario.numero              = r[7]
        funcionario.complemento         = r[8]
        funcionario.bairro              = r[9]
        funcionario.uf                  = r[10]
        funcionario.cidade              = r[11]
        funcionario.cep                 = r[12]
        funcionario.telefone_1          = r[13]
        funcionario.telefone_2          = r[14]
        funcionario.email               = r[15]
        funcionario.salario             = r[16]
        funcionario.m_quadrado          = r[17]
        funcionario.diaria              = r[18]
        funcionario.mensal              = r[19]
        funcionario.data_nascimento     = r[20]
        funcionario.admissao            = r[21]
        funcionario.funcao              = r[22]
        funcionario.senha               = r[23]
        funcionario.comissao_calculo    = r[24]
        funcionario.comissao_produto    = r[25]
        funcionario.comissao_servico    = r[26]
        funcionario.desconto            = r[27]
        funcionario.tipo                = r[28]
        funcionario.nometipo            = r[29]
        funcionario.nomefuncao          = r[30]
        funcionario.nomeuf              = r[31]
        funcionario.nomecidade          = r[32]
        funcionario_list.append(funcionario.__dict__)

    SQL.cur.close()

    return funcionario_list

def getFuncionario(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT 
            f.Id, 
            f.Nome, 
            f.Identificacao, 
            f.CNPJ, 
            f.CPF, 
            f.RG, 
            f.Endereco, 
            f.Numero, 
            f.Complemento,
            f.Bairro, 
            f.UF, 
            f.Cidade, 
            f.Cep, 
            f.Telefone_1, 
            f.Telefone_2, 
            f.Email, 
            f.Salario,
            f.MQuadrado, 
            f.Diaria, 
            f.Mensal, 
            f.DataNascimento, 
            f.Admissao, 
            f.Funcao, 
            f.Senha,
            f.Comissao_Calculo, 
            f.Comissao_Produto, 
            f.Comissao_Servico, 
            f.Desconto, 
            f.Tipo,
            ft.nome as nometipo,
            ff.nome as nomefuncao,
            f.UF_Nome,
            f.Cidade_Nome
        FROM Funcionarios as f
        LEFT JOIN Funcionario_Tipo as ft ON f.Tipo = ft.id
        LEFT JOIN Funcionario_Funcao as ff ON f.Funcao = ff.id
        WHERE f.Id = {id}
        """
    )

    records = SQL.cur.fetchall()
    funcionario_list = []

    for r in records:
        funcionario                     = Funcionarios()
        funcionario.id                  = r[0]
        funcionario.nome                = r[1]
        funcionario.identificacao       = r[2]
        funcionario.cnpj                = r[3]
        funcionario.cpf                 = r[4]
        funcionario.rg                  = r[5]
        funcionario.endereco            = r[6]
        funcionario.numero              = r[7]
        funcionario.complemento         = r[8]
        funcionario.bairro              = r[9]
        funcionario.uf                  = r[10]
        funcionario.cidade              = r[11]
        funcionario.cep                 = r[12]
        funcionario.telefone_1          = r[13]
        funcionario.telefone_2          = r[14]
        funcionario.email               = r[15]
        funcionario.salario             = r[16]
        funcionario.m_quadrado          = r[17]
        funcionario.diaria              = r[18]
        funcionario.mensal              = r[19]
        funcionario.data_nascimento     = r[20]
        funcionario.admissao            = r[21]
        funcionario.funcao              = r[22]
        funcionario.senha               = r[23]
        funcionario.comissao_calculo    = r[24]
        funcionario.comissao_produto    = r[25]
        funcionario.comissao_servico    = r[26]
        funcionario.desconto            = r[27]
        funcionario.tipo                = r[28]
        funcionario.nometipo            = r[29]
        funcionario.nomefuncao          = r[30]
        funcionario.nomeuf              = r[31]
        funcionario.nomecidade          = r[32]
        funcionario_list.append(funcionario.__dict__)

    SQL.cur.close()

    return funcionario_list

def postFuncionario(funcionario: Funcionarios):
    nome                = funcionario.nome
    identificacao       = funcionario.identificacao
    cnpj                = funcionario.cnpj
    cpf                 = funcionario.cpf
    rg                  = funcionario.rg
    endereco            = funcionario.endereco
    numero              = funcionario.numero
    complemento         = funcionario.complemento
    bairro              = funcionario.bairro
    uf                  = funcionario.uf
    cidade              = funcionario.cidade
    cep                 = funcionario.cep
    telefone_1          = funcionario.telefone_1
    telefone_2          = funcionario.telefone_2
    email               = funcionario.email
    salario             = funcionario.salario
    m_quadrado          = funcionario.m_quadrado
    diaria              = funcionario.diaria
    mensal              = funcionario.mensal
    data_nascimento     = funcionario.data_nascimento
    admissao            = funcionario.admissao
    funcao              = funcionario.funcao
    senha               = funcionario.senha
    comissao_calculo    = funcionario.comissao_calculo
    comissao_produto    = funcionario.comissao_produto
    comissao_servico    = funcionario.comissao_servico
    desconto            = funcionario.desconto
    tipo                = funcionario.tipo
    nomeuf              = funcionario.nomeuf    
    nomecidade          = funcionario.nomecidade   

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Funcionarios ( Nome, Identificacao, CNPJ, CPF, RG, Endereco, Numero, Complemento,
                                  Bairro, UF, Cidade, Cep, Telefone_1, Telefone_2, Email, Salario,
                                  MQuadrado, Diaria, Mensal, DataNascimento, Admissao, Funcao, Senha,
                                  Comissao_Calculo, Comissao_Produto, Comissao_Servico, Desconto, Tipo, UF_Nome, Cidade_Nome)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            nome, identificacao, cnpj, cpf, rg, endereco, numero, complemento,
            bairro, uf, cidade, cep, telefone_1, telefone_2, email, salario,
            m_quadrado, diaria, mensal, data_nascimento, admissao, funcao, senha,
            comissao_calculo, comissao_produto, comissao_servico, desconto, tipo, nomeuf, nomecidade
        )
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return funcionario

def updateFuncionario(id:int, funcionario: Funcionarios):
    nome                = funcionario.nome
    identificacao       = funcionario.identificacao
    cnpj                = funcionario.cnpj
    cpf                 = funcionario.cpf
    rg                  = funcionario.rg
    endereco            = funcionario.endereco
    numero              = funcionario.numero
    complemento         = funcionario.complemento
    bairro              = funcionario.bairro
    uf                  = funcionario.uf
    cidade              = funcionario.cidade
    cep                 = funcionario.cep
    telefone_1          = funcionario.telefone_1
    telefone_2          = funcionario.telefone_2
    email               = funcionario.email
    salario             = funcionario.salario
    m_quadrado          = funcionario.m_quadrado
    diaria              = funcionario.diaria
    mensal              = funcionario.mensal
    data_nascimento     = funcionario.data_nascimento
    admissao            = funcionario.admissao
    funcao              = funcionario.funcao
    senha               = funcionario.senha
    comissao_calculo    = funcionario.comissao_calculo
    comissao_produto    = funcionario.comissao_produto
    comissao_servico    = funcionario.comissao_servico
    desconto            = funcionario.desconto
    tipo                = funcionario.tipo
    nomeuf              = funcionario.nomeuf    
    nomecidade          = funcionario.nomecidade   

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Funcionarios SET Nome = ?, Identificacao = ?, CNPJ = ?, CPF = ?, RG = ?, Endereco = ?, Numero = ?,
                               Complemento = ?, Bairro = ?, UF = ?, Cidade = ?, Cep = ?, Telefone_1 = ?,
                               Telefone_2 = ?, Email = ?, Salario = ?, MQuadrado = ?, Diaria = ?, Mensal = ?,
                               DataNascimento = ?, Admissao = ?, Funcao = ?, Senha = ?, Comissao_Calculo = ?,
                               Comissao_Produto = ?, Comissao_Servico = ?, Desconto = ?, Tipo = ?, UF_Nome = ?, Cidade_Nome = ?
        WHERE Id = ?
        """,
        (
            nome, identificacao, cnpj, cpf, rg, endereco, numero, complemento,
            bairro, uf, cidade, cep, telefone_1, telefone_2, email, salario,
            m_quadrado, diaria, mensal, data_nascimento, admissao, funcao, senha,
            comissao_calculo, comissao_produto, comissao_servico, desconto, tipo, nomeuf, nomecidade, id
        )
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return funcionario

def deleteFuncionario(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        DELETE FROM Funcionarios WHERE Id = ?
        """,
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
