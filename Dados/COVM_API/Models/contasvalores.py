from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *

class Contas_Valores(BaseClass):
    id         = 0
    valor      = 0.0
    descricao  = ''
    titulo     = ''
    conta      = 0
    nomeconta  = '' 
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id         = 0
        self.valor      = 0.0
        self.descricao  = ''
        self.titulo     = ''
        self.conta      = 0
        self.nomeconta  = ''
        
def getContas_Valores():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
        cv.Id, 
        cv.Valor, 
        cv.Descricao, 
        cv.Titulo, 
        cv.Conta,
        c.nome as nomeconta
        FROM Contas_Valores as cv
        LEFT JOIN Contas as c ON cv.Conta = c.id
        """
    )
    
    records = SQL.cur.fetchall()
    contas_valores_list = []
    
    for r in records:
        contas_valores              = Contas_Valores()
        contas_valores.id           = r[0]
        contas_valores.valor        = r[1]
        contas_valores.descricao    = r[2]
        contas_valores.titulo       = r[3]
        contas_valores.conta        = r[4]
        contas_valores.nomeconta    = r[5]
        contas_valores_list.append(contas_valores.__dict__)
    
    SQL.cur.close()
    
    return contas_valores_list

def getContas_Valor(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
            SELECT 
            cv.Id, 
            cv.Valor, 
            cv.Descricao, 
            cv.Titulo, 
            cv.Conta,
            c.nome as nomeconta
            FROM Contas_Valores as cv
            LEFT JOIN Contas as c ON cv.Conta = c.id
            WHERE cv.Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    contas_valores_list = []
    
    for r in records:
        contas_valores              = Contas_Valores()
        contas_valores.id           = r[0]
        contas_valores.valor        = r[1]
        contas_valores.descricao    = r[2]
        contas_valores.titulo       = r[3]
        contas_valores.conta        = r[4]
        contas_valores.nomeconta    = r[5]
        contas_valores_list.append(contas_valores.__dict__)
    
    SQL.cur.close()
    
    return contas_valores_list

def postContas_Valor(contas_valor: Contas_Valores):
    valor     = contas_valor.valor
    descricao = contas_valor.descricao
    titulo    = contas_valor.titulo
    conta     = contas_valor.conta

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Contas_Valores (Valor, Descricao, Titulo, Conta)
        VALUES (?, ?, ?, ?)
        """,
        (
            valor, descricao, titulo, conta
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return contas_valor

def updateContas_Valor(id: int, contas_valor: Contas_Valores):
    valor     = contas_valor.valor
    descricao = contas_valor.descricao
    titulo    = contas_valor.titulo
    conta     = contas_valor.conta

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Contas_Valores
        SET Valor = ?,
            Descricao = ?,
            Titulo = ?,
            Conta = ?
        WHERE Id = ?;
        """,
        (
            valor, descricao, titulo, conta, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return contas_valor

def deleteContas_Valor(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Contas_Valores WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
