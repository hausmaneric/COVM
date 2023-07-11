from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Obras_Servicos(BaseClass):
    id              = 0
    obra            = 0
    funcionario     = 0
    funcionarios    = False
    valor           = 0.0
    tipo            = 0
    taxa            = False
    transporte      = 0.0
    alimentacao     = 0.0
    nomefuncionario = ''

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        super().__init__(*args, **kwds)
        self.id               = 0
        self.obra             = 0
        self.funcionario      = 0
        self.funcionarios     = False
        self.valor            = 0.0
        self.tipo             = 0
        self.taxa             = False
        self.transporte       = 0.0
        self.alimentacao      = 0.0
        self.nomefuncionario  = ''

def getObrasServicos():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
            os.Id, 
            os.Obra, 
            os.Funcionario, 
            os.Funcionarios, 
            os.Valor, 
            os.Tipo, 
            os.Taxa, 
            os.Transporte, 
            os.Alimentacao,
            f.nome as nomefuncionario
        FROM Obras_Servicos as os
        LEFT JOIN Funcionarios as f ON os.Funcionario = f.id
        """
    )

    records = SQL.cur.fetchall()
    obras_Servicos_list = []

    for r in records:
        obra_Servicos                   = Obras_Servicos()
        obra_Servicos.id                = r[0]
        obra_Servicos.obra              = r[1]
        obra_Servicos.funcionario       = r[2]
        obra_Servicos.funcionarios      = r[3]
        obra_Servicos.valor             = r[4]
        obra_Servicos.tipo              = r[5]
        obra_Servicos.taxa              = r[6]
        obra_Servicos.transporte        = r[7]
        obra_Servicos.alimentacao       = r[8]
        obra_Servicos.nomefuncionario   = r[9]
        obras_Servicos_list.append(obra_Servicos.__dict__)

    SQL.cur.close()

    return obras_Servicos_list

def getObraServicos(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
         SELECT 
            os.Id, 
            os.Obra, 
            os.Funcionario, 
            os.Funcionarios, 
            os.Valor, 
            os.Tipo, 
            os.Taxa, 
            os.Transporte, 
            os.Alimentacao,
            f.nome as nomefuncionario
        FROM Obras_Servicos as os
        LEFT JOIN Funcionarios as f ON os.Funcionario = f.id
        WHERE os.Id = {id}
        """
    )

    records = SQL.cur.fetchall()
    obras_Servicos_list = []

    for r in records:
        obra_Servicos                   = Obras_Servicos()
        obra_Servicos.id                = r[0]
        obra_Servicos.obra              = r[1]
        obra_Servicos.funcionario       = r[2]
        obra_Servicos.funcionarios      = r[3]
        obra_Servicos.valor             = r[4]
        obra_Servicos.tipo              = r[5]
        obra_Servicos.taxa              = r[6]
        obra_Servicos.transporte        = r[7]
        obra_Servicos.alimentacao       = r[8]
        obra_Servicos.nomefuncionario   = r[9]
        obras_Servicos_list.append(obra_Servicos.__dict__)

    SQL.cur.close()

    return obras_Servicos_list

def postObraServicos(obra_Servicos: Obras_Servicos):
    obra         = obra_Servicos.obra
    funcionario  = obra_Servicos.funcionario
    funcionarios = obra_Servicos.funcionarios
    valor        = obra_Servicos.valor
    tipo         = obra_Servicos.tipo
    taxa         = obra_Servicos.taxa
    transporte   = obra_Servicos.transporte
    alimentacao  = obra_Servicos.alimentacao

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Obras_Servicos ( Obra, Funcionario, Funcionarios, Valor, Tipo, Taxa, Transporte, Alimentacao)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ( obra, funcionario, funcionarios, valor, tipo, taxa, transporte, alimentacao)
    )

    SQL.con.commit()
    SQL.con.close()

    return obra_Servicos

def updateObraServicos(id: int, obra_Servicos: Obras_Servicos):
    obra         = obra_Servicos.obra
    funcionario  = obra_Servicos.funcionario
    funcionarios = obra_Servicos.funcionarios
    valor        = obra_Servicos.valor
    tipo         = obra_Servicos.tipo
    taxa         = obra_Servicos.taxa
    transporte   = obra_Servicos.transporte
    alimentacao  = obra_Servicos.alimentacao

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Obras_Servicos
        SET Obra = ?,
            Funcionario = ?,
            Funcionarios = ?,
            Valor = ?,
            Tipo = ?,
            Taxa = ?,
            Transporte = ?,
            Alimentacao = ?
        WHERE Id = ?;
        """,
        (obra, funcionario, funcionarios, valor, tipo, taxa, transporte, alimentacao, id)
    )

    SQL.con.commit()
    SQL.con.close()

    return obra_Servicos

def deleteObraServicos(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Obras_Servicos WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()

    return {"msg": "Deletado"}
