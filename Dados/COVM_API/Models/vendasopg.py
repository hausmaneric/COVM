from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Vendas_Opg(BaseClass):
    id         = 0
    venda      = 0
    opg        = 0
    parcelas   = 0
    entrada    = False
    vencimento = date.today()
    valor      = 0.0
    nomeopg    = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> None:        
        super().__init__(*args, **kwds) 
        self.id         = 0
        self.venda      = 0
        self.opg        = 0
        self.parcelas   = 0
        self.entrada    = False
        self.vencimento = date.today()
        self.valor      = 0.0
        self.nomeopg    = ''

def getVendasOpg():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
            vopg.Id, 
            vopg.Venda, 
            vopg.Opg, 
            vopg.Parcelas, 
            vopg.Entrada, 
            vopg.Vencimento, 
            vopg.Valor,
            op.nome as nomeopg
        FROM Vendas_Opg as vopg
        LEFT JOIN Opcao_Pagamento as op ON vopg.Opg = op.id
        """
    )
    
    records = SQL.cur.fetchall()
    vendas_opg_list = []
    
    for r in records:
        venda_opg                = Vendas_Opg()
        venda_opg.id             = r[0]
        venda_opg.venda          = r[1]
        venda_opg.opg            = r[2]
        venda_opg.parcelas       = r[3]
        venda_opg.entrada        = (r[4])
        venda_opg.vencimento     = r[5]
        venda_opg.valor          = (r[6])
        venda_opg.nomeopg        = r[7]
        vendas_opg_list.append(venda_opg.__dict__)
    
    SQL.cur.close()
    
    return vendas_opg_list

def getVendaOpg(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT 
            vopg.Id, 
            vopg.Venda, 
            vopg.Opg, 
            vopg.Parcelas, 
            vopg.Entrada, 
            vopg.Vencimento, 
            vopg.Valor,
            op.nome as nomeopg
        FROM Vendas_Opg as vopg
        LEFT JOIN Opcao_Pagamento as op ON vopg.Opg = op.id
        WHERE vopg.Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    vendas_opg_list = []
    
    for r in records:
        venda_opg                = Vendas_Opg()
        venda_opg.id             = r[0]
        venda_opg.venda          = r[1]
        venda_opg.opg            = r[2]
        venda_opg.parcelas       = r[3]
        venda_opg.entrada        = (r[4])
        venda_opg.vencimento     = r[5]
        venda_opg.valor          = (r[6])
        venda_opg.nomeopg        = r[7]
        vendas_opg_list.append(venda_opg.__dict__)
        
    SQL.cur.close()
    return venda_opg.__dict__

def postVendaOpg(venda_opg: Vendas_Opg):
    venda       = venda_opg.venda
    opg         = venda_opg.opg
    parcelas    = venda_opg.parcelas
    entrada     = (venda_opg.entrada)
    vencimento  = venda_opg.vencimento
    valor       = venda_opg.valor

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Vendas_Opg (Venda, Opg, Parcelas, Entrada, Vencimento, Valor)
        VALUES ( ?, ?, ?, ?, ?, ?)
        """,
        ( venda, opg, parcelas, entrada, vencimento, valor)
    )

    SQL.con.commit()
    SQL.con.close()

    return venda_opg

def updateVendaOpg(id: int, venda_opg: Vendas_Opg):
    venda       = venda_opg.venda
    opg         = venda_opg.opg
    parcelas    = venda_opg.parcelas
    entrada     = (venda_opg.entrada)
    vencimento  = venda_opg.vencimento
    valor       = venda_opg.valor

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Vendas_Opg
        SET Venda = ?,
            Opg = ?,
            Parcelas = ?,
            Entrada = ?,
            Vencimento = ?,
            Valor = ?
        WHERE Id = ?;
        """,
        (venda, opg, parcelas, entrada, vencimento, valor, id)
    )

    SQL.con.commit()
    SQL.con.close()

    return venda_opg

def deleteVendaOpg(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Vendas_Opg WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
