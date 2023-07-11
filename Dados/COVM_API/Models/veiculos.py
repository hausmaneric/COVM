from typing import Any, overload
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Veiculos(BaseClass):
    id         = 0
    tipo       = 0
    nome       = ""
    placa      = ""
    cor        = ""
    situacao   = 0
    modelo     = ""
    nometipo   = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id         = 0
        self.tipo       = 0
        self.nome       = ""
        self.placa      = ""
        self.cor        = ""
        self.situacao   = 0
        self.modelo     = ""
        self.nometipo   = ''


def getVeiculosList():
    veiculos_list = []

    SQL = dbmsqls()
    SQL.cur.execute("""
                    SELECT 
                        v.Id, 
                        v.Tipo, 
                        v.Nome, 
                        v.Placa, 
                        v.Cor, 
                        v.Situacao, 
                        v.Modelo,
                        vt.nome as nometipo
                    FROM Veiculos as v
                    LEFT JOIN Veiculos_Tipo as vt ON v.tipo = vt.id
                    """)
    rows = SQL.cur.fetchall()

    for r in rows:
        veiculo             = Veiculos()
        veiculo.id          = r[0]
        veiculo.tipo        = r[1]
        veiculo.nome        = r[2]
        veiculo.placa       = r[3]
        veiculo.cor         = r[4]
        veiculo.situacao    = r[5]
        veiculo.modelo      = r[6]
        veiculo.nometipo    = r[7]
        veiculos_list.append(veiculo.__dict__)

    SQL.cur.close()

    return veiculos_list

def getVeiculo(id: int):
    veiculos_list = []

    SQL = dbmsqls()
    SQL.cur.execute(f"""
                    SELECT 
                        v.Id, 
                        v.Tipo, 
                        v.Nome, 
                        v.Placa, 
                        v.Cor, 
                        v.Situacao, 
                        v.Modelo,
                        vt.nome as nometipo
                    FROM Veiculos as v
                    LEFT JOIN Veiculos_Tipo as vt ON v.Tipo = vt.id 
                    WHERE v.Id = {id}
                    """)
    rows = SQL.cur.fetchall()

    for r in rows:
        veiculo             = Veiculos()
        veiculo.id          = r[0]
        veiculo.tipo        = r[1]
        veiculo.nome        = r[2]
        veiculo.placa       = r[3]
        veiculo.cor         = r[4]
        veiculo.situacao    = r[5]
        veiculo.modelo      = r[6]
        veiculo.nometipo    = r[7]
        veiculos_list.append(veiculo.__dict__)

    SQL.cur.close()

    return veiculos_list

def postVeiculo(veiculo: Veiculos):
    tipo        = veiculo.tipo
    nome        = veiculo.nome
    placa       = veiculo.placa
    cor         = veiculo.cor
    situacao    = veiculo.situacao
    modelo      = veiculo.modelo

    SQL = dbmsqls()
    SQL.cur.execute(
        "INSERT INTO Veiculos ( Tipo, Nome, Placa, Cor, Situacao, Modelo) VALUES ( ?, ?, ?, ?, ?, ?)",
        ( tipo, nome, placa, cor, situacao, modelo)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return veiculo


def updateVeiculo(id:int, veiculo: Veiculos):
    tipo        = veiculo.tipo
    nome        = veiculo.nome
    placa       = veiculo.placa
    cor         = veiculo.cor
    situacao    = veiculo.situacao
    modelo      = veiculo.modelo

    SQL = dbmsqls()
    SQL.cur.execute(
        "UPDATE Veiculos SET Tipo = ?, Nome = ?, Placa = ?, Cor = ?, Situacao = ?, Modelo = ? WHERE Id = ?",
        (tipo, nome, placa, cor, situacao, modelo, id)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return veiculo


def deleteVeiculo(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Veiculos WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()

    return {"msg": "Deletado"}