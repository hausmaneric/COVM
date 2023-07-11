from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Vendas(BaseClass):
    id            = 0
    cliente       = 0
    vendedor      = 0
    data_inicial  = date.today()
    entrega       = False
    data_entrega  = date.today()
    frete         = 0.0
    desconto      = 0.0
    acrescimo     = 0.0
    opg           = 0
    nomecliente   = ''
    nomevendedor  = ''
    nomeopg       = ''    

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        super().__init__(*args, **kwds)
        self.id            = 0
        self.cliente       = 0
        self.vendedor      = 0
        self.data_inicial  = date.today()
        self.entrega       = False
        self.data_entrega  = date.today()
        self.frete         = 0.0
        self.desconto      = 0.0
        self.acrescimo     = 0.0
        self.opg           = 0
        self.nomecliente   = ''
        self.nomevendedor  = ''
        self.nomeopg       = ''

def getVendas():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
            v.Id, 
            v.Cliente, 
            v.Vendedor, 
            v.DataInicial, 
            v.Entrega, 
            v.DataEntrega, 
            v.Frete, 
            v.Desconto, 
            v.Acrescimo, 
            v.Opg,
            c.nome as nomecliente,
            f.nome as nomevendedor,
            op.nome as nomeopg
        FROM Vendas as v
        LEFT JOIN Clientes as c ON v.Cliente = c.id
        LEFT JOIN Funcionarios as f ON v.Vendedor = f.id
        LEFT JOIN Opcao_Pagamento as op ON v.Opg = op.id
        """
    )
    
    records = SQL.cur.fetchall()
    venda_list = []
    
    for r in records:
        venda                 = Vendas()
        venda.id              = r[0]
        venda.cliente         = r[1]
        venda.vendedor        = r[2]
        venda.data_inicial    = r[3]
        venda.entrega         = r[4]
        venda.data_entrega    = r[5]
        venda.frete           = r[6]
        venda.desconto        = r[7]
        venda.acrescimo       = r[8]
        venda.opg             = r[9]
        venda.nomecliente     = r[10]
        venda.nomevendedor    = r[11]
        venda.nomeopg         = r[12]
        venda_list.append(venda.__dict__)
    
    SQL.cur.close()
    
    return venda_list

def getVenda(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT 
            v.Id, 
            v.Cliente, 
            v.Vendedor, 
            v.DataInicial, 
            v.Entrega, 
            v.DataEntrega, 
            v.Frete, 
            v.Desconto, 
            v.Acrescimo, 
            v.Opg,
            c.nome as nomecliente,
            f.nome as nomevendedor,
            op.nome as nomeopg
        FROM Vendas as v
        LEFT JOIN Clientes as c ON v.Cliente = c.id
        LEFT JOIN Funcionarios as f ON v.Vendedor = f.id
        LEFT JOIN Opcao_Pagamento as op ON v.Opg = op.id
        WHERE v.Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    venda_list = []
    
    for r in records:
        venda                 = Vendas()
        venda.id              = r[0]
        venda.cliente         = r[1]
        venda.vendedor        = r[2]
        venda.data_inicial    = r[3]
        venda.entrega         = r[4]
        venda.data_entrega    = r[5]
        venda.frete           = r[6]
        venda.desconto        = r[7]
        venda.acrescimo       = r[8]
        venda.opg             = r[9]
        venda.nomecliente     = r[10]
        venda.nomevendedor    = r[11]
        venda.nomeopg         = r[12]
        venda_list.append(venda.__dict__)
    
    SQL.cur.close()
    
    return venda_list

def postVenda(venda: Vendas):
    cliente        = venda.cliente
    vendedor       = venda.vendedor
    data_inicial   = venda.data_inicial
    entrega        = venda.entrega
    data_entrega   = venda.data_entrega
    frete          = venda.frete
    desconto       = venda.desconto
    acrescimo      = venda.acrescimo
    opg            = venda.opg

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Vendas ( Cliente, Vendedor, DataInicial, Entrega, DataEntrega, Frete, Desconto, Acrescimo, Opg)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            cliente, vendedor, data_inicial, entrega, data_entrega, frete, desconto, acrescimo, opg
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return venda

def updateVenda(id: int, venda: Vendas):
    cliente        = venda.cliente
    vendedor       = venda.vendedor
    data_inicial   = venda.data_inicial
    entrega        = venda.entrega
    data_entrega   = venda.data_entrega
    frete          = venda.frete
    desconto       = venda.desconto
    acrescimo      = venda.acrescimo
    opg            = venda.opg

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Vendas
        SET Cliente = ?,
            Vendedor = ?,
            DataInicial = ?,
            Entrega = ?,
            DataEntrega = ?,
            Frete = ?,
            Desconto = ?,
            Acrescimo = ?,
            Opg = ?
        WHERE Id = ?;
        """,
        (
            cliente, vendedor, data_inicial, entrega, data_entrega, frete, desconto, acrescimo, opg, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return venda

def deleteVenda(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Vendas WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
