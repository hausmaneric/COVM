from typing import Any
from Models.codigo import GeradorIDSequencial
from dataaccess.db import dbmsqls
from Models.baseClass import *
from datetime import date

class Obras_Opg(BaseClass):
    id         = 0
    obra       = 0
    opg        = 0
    parcelas   = 0
    entrada    = False
    valor      = 0.0
    vencimento = date.today()
    nomeopg    = ''

    def __init__(self, *args: Any, **kwds: Any) -> None:
        super().__init__(*args, **kwds)
        self.id         = 0
        self.obra       = 0
        self.opg        = 0
        self.parcelas   = 0
        self.entrada    = False
        self.valor      = 0.0
        self.vencimento = date.today()
        self.nomeopg    = ''

def getObras_Opg():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
        opg.Id, 
        opg.Obra, 
        opg.Opg, 
        opg.Parcelas, 
        opg.Entrada, 
        opg.Valor, 
        opg.Vencimento,
        op.nome as nomeopg
        FROM Obras_Opg as opg
        LEFT JOIN Opcao_Pagamento as op ON opg.Opg = op.id
        """
    )
    
    records = SQL.cur.fetchall()
    obras_opg_list = []
    
    for r in records:
        obras_opg              = Obras_Opg()
        obras_opg.id           = r[0]
        obras_opg.obra         = r[1]
        obras_opg.opg          = r[2]
        obras_opg.parcelas     = r[3]
        obras_opg.entrada      = r[4]
        obras_opg.valor        = r[5]
        obras_opg.vencimento   = r[6]
        obras_opg.nomeopg      = r[7]
        obras_opg_list.append(obras_opg.__dict__)
    
    SQL.cur.close()
    
    return obras_opg_list

def getObra_Opg(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
            SELECT 
            opg.Id, 
            opg.Obra, 
            opg.Opg, 
            opg.Parcelas, 
            opg.Entrada, 
            opg.Valor, 
            opg.Vencimento,
            op.nome as nomeopg
            FROM Obras_Opg as opg
            LEFT JOIN Opcao_Pagamento as op ON opg.Opg = op.id
            WHERE opg.Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    obras_opg_list = []
    
    for r in records:
        obras_opg              = Obras_Opg()
        obras_opg.id           = r[0]
        obras_opg.obra         = r[1]
        obras_opg.opg          = r[2]
        obras_opg.parcelas     = r[3]
        obras_opg.entrada      = r[4]
        obras_opg.valor        = r[5]
        obras_opg.vencimento   = r[6]
        obras_opg.nomeopg      = r[7]
        obras_opg_list.append(obras_opg.__dict__)
    
    SQL.cur.close()
    
    return obras_opg_list

def postObra_Opg(obras_opg: Obras_Opg):
    obra       = obras_opg.obra
    opg        = obras_opg.opg
    parcelas   = obras_opg.parcelas
    entrada    = obras_opg.entrada
    valor      = obras_opg.valor
    vencimento = obras_opg.vencimento

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Obras_Opg ( Obra, Opg, Parcelas, Entrada, Valor, Vencimento)
        VALUES ( ?, ?, ?, ?, ?, ?)
        """,
        ( obra, opg, parcelas, entrada, valor, vencimento)
    )

    SQL.con.commit()
    SQL.con.close()

    return obras_opg

def updateObra_Opg(id: int, obras_opg: Obras_Opg):
    obra       = obras_opg.obra
    opg        = obras_opg.opg
    parcelas   = obras_opg.parcelas
    entrada    = obras_opg.entrada
    valor      = obras_opg.valor
    vencimento = obras_opg.vencimento

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Obras_Opg
        SET Obra = ?,
            Opg = ?,
            Parcelas = ?,
            Entrada = ?,
            Valor = ?,
            Vencimento = ?
        WHERE Id = ?;
        """,
        (obra, opg, parcelas, entrada, valor, vencimento, id)
    )

    SQL.con.commit()
    SQL.con.close()

    return obras_opg

def deleteObra_Opg(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Obras_Opg WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
