from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *

class Contas(BaseClass):
    id      = 0
    nome    = ''
    agencia = ''
    conta   = ''
    banco   = ''
    extrato = 0.0
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id      = 0
        self.nome    = ''
        self.agencia = ''
        self.conta   = ''
        self.banco   = ''
        self.extrato = 0.0
        
def getContas():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT Id, Nome, Agencia, Conta, Banco, Extrato
        FROM Contas
        """
    )
    
    records = SQL.cur.fetchall()
    conta_list = []
    
    for r in records:
        conta             = Contas()
        conta.id          = r[0]
        conta.nome        = r[1]
        conta.agencia     = r[2]
        conta.conta       = r[3]
        conta.banco       = r[4]
        conta.extrato     = r[5]
        conta_list.append(conta.__dict__)
    
    SQL.cur.close()
    
    return conta_list

def getConta(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT Id, Nome, Agencia, Conta, Banco, Extrato
        FROM Contas
        WHERE Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    conta_list = []
    
    for r in records:
        conta             = Contas()
        conta.id          = r[0]
        conta.nome        = r[1]
        conta.agencia     = r[2]
        conta.conta       = r[3]
        conta.banco       = r[4]
        conta.extrato     = r[5]
        conta_list.append(conta.__dict__)
    
    SQL.cur.close()
    
    return conta_list

def postConta(contas: Contas):
    nome    = contas.nome
    agencia = contas.agencia
    conta   = contas.conta
    banco   = contas.banco
    extrato = contas.extrato

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Contas (Nome, Agencia, Conta, Banco, Extrato)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            nome, agencia, conta, banco, extrato
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return contas

def updateConta(id: int, contas: Contas):
    nome    = contas.nome
    agencia = contas.agencia
    conta   = contas.conta
    banco   = contas.banco
    extrato = contas.extrato

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Contas
        SET Nome = ?,
            Agencia = ?,
            Conta = ?,
            Banco = ?,
            Extrato = ?
        WHERE Id = ?;
        """,
        (
            nome, agencia, conta, banco, extrato, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return contas

def deleteConta(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Contas WHERE Id = ?",
        (id,)
    )
    
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
