from typing import Any, overload
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class VeiculosTipo(BaseClass):
    id         = 0
    nome       = ""

    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds)  
        self.id         = 0
        self.nome       = ""


def getVeiculosTipoList():
    veiculos_tipo_list = []

    SQL = dbmsqls()
    SQL.cur.execute("SELECT Id, Nome FROM Veiculos_Tipo")
    rows = SQL.cur.fetchall()

    for r in rows:
        Veiculos_Tipo            = VeiculosTipo()
        Veiculos_Tipo.id         = r[0]
        Veiculos_Tipo.nome       = r[1]
        veiculos_tipo_list.append(Veiculos_Tipo.__dict__)

    SQL.cur.close()

    return veiculos_tipo_list

def getVeiculosTipo(id: int):
    veiculos_tipo_list = []

    SQL = dbmsqls()
    SQL.cur.execute(f"SELECT Id, Nome FROM Veiculos_Tipo WHERE Id = {id}")
    rows = SQL.cur.fetchall()

    for r in rows:
        Veiculos_Tipo            = VeiculosTipo()
        Veiculos_Tipo.id         = r[0]
        Veiculos_Tipo.nome       = r[1]
        veiculos_tipo_list.append(Veiculos_Tipo.__dict__)

    SQL.cur.close()

    return veiculos_tipo_list

def postVeiculoTipo(Veiculos_Tipo: VeiculosTipo):
    nome    = Veiculos_Tipo.nome

    SQL = dbmsqls()
    SQL.cur.execute(
        "INSERT INTO Veiculos_Tipo ( Nome) VALUES ( ?)",
        ( nome)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return Veiculos_Tipo


def updateVeiculoTipo(id,Veiculos_Tipo: VeiculosTipo):
    nome    = Veiculos_Tipo.nome

    SQL = dbmsqls()
    SQL.cur.execute(
        "UPDATE Veiculos_Tipo SET Nome = ? WHERE Id = ?",
        (nome, id)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return Veiculos_Tipo
    
def deleteVeiculoTipo(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        DELETE FROM Veiculos_Tipo WHERE Id = ?
        """,
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}