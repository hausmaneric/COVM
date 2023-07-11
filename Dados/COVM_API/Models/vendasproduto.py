from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Vendas_Produtos(BaseClass):
    id               = 0
    venda            = 0
    produto          = 0
    desconto         = False
    desconto_produto = 0.0
    acrescimo        = 0.0
    quantidade       = 0.0
    valor            = 0.0
    total            = 0.0
    nomeproduto      = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> None:        
        super().__init__(*args, **kwds) 
        self.id               = 0
        self.venda            = 0
        self.produto          = 0
        self.desconto         = False
        self.desconto_produto = 0.0
        self.acrescimo        = 0.0
        self.quantidade       = 0.0
        self.valor            = 0.0
        self.total            = 0.0
        self.nomeproduto      = ''

def getVendasProdutos():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
            vp.Id, 
            vp.Venda, 
            vp.Produto, 
            vp.Desconto, 
            vp.Desconto_Produto, 
            vp.Acrescimo, 
            vp.Quantidade, vp.Valor, 
            vp.Total,
            p.nome as nomeproduto
        FROM Vendas_Produtos as vp
        LEFT JOIN Produtos as p ON vp.Produto = p.Id
        """
    )
    
    records = SQL.cur.fetchall()
    vendas_produtos_list = []
    
    for r in records:
        venda_produto                     = Vendas_Produtos()
        venda_produto.id                  = r[0]
        venda_produto.venda               = r[1]
        venda_produto.produto             = r[2]
        venda_produto.desconto            = (r[3])
        venda_produto.desconto_produto    = (r[4])
        venda_produto.acrescimo           = (r[5])
        venda_produto.quantidade          = (r[6])
        venda_produto.valor               = (r[7])
        venda_produto.total               = (r[8])
        venda_produto.nomeproduto         = r[9]
        vendas_produtos_list.append(venda_produto.__dict__)
    
    SQL.cur.close()
    
    return vendas_produtos_list

def getVendaProduto(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT Id, Venda, Produto, Desconto, Desconto_Produto, Acrescimo, Quantidade, Valor, Total
        FROM Vendas_Produtos
        WHERE Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    vendas_produtos_list = []
    
    for r in records:
        venda_produto                     = Vendas_Produtos()
        venda_produto.id                  = r[0]
        venda_produto.venda               = r[1]
        venda_produto.produto             = r[2]
        venda_produto.desconto            = (r[3])
        venda_produto.desconto_produto    = (r[4])
        venda_produto.acrescimo           = (r[5])
        venda_produto.quantidade          = (r[6])
        venda_produto.valor               = (r[7])
        venda_produto.total               = (r[8])
        venda_produto.nomeproduto         = r[9]
        vendas_produtos_list.append(venda_produto.__dict__)
    
    SQL.cur.close()
    
    return vendas_produtos_list

def postVendaProduto(venda_produto: Vendas_Produtos):
    venda              = venda_produto.venda
    produto            = venda_produto.produto
    desconto           = (venda_produto.desconto)
    desconto_produto   = venda_produto.desconto_produto
    acrescimo          = venda_produto.acrescimo
    quantidade         = venda_produto.quantidade
    valor              = venda_produto.valor
    total              = venda_produto.total

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Vendas_Produtos ( Venda, Produto, Desconto, Desconto_Produto, Acrescimo, Quantidade, Valor, Total)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
             venda, produto, desconto, desconto_produto, acrescimo, quantidade, valor, total
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return venda_produto

def updateVendaProduto(id: int, venda_produto: Vendas_Produtos):
    venda              = venda_produto.venda
    produto            = venda_produto.produto
    desconto           = int(venda_produto.desconto)
    desconto_produto   = venda_produto.desconto_produto
    acrescimo          = venda_produto.acrescimo
    quantidade         = venda_produto.quantidade
    valor              = venda_produto.valor
    total              = venda_produto.total

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Vendas_Produtos
        SET Venda = ?,
            Produto = ?,
            Desconto = ?,
            Desconto_Produto = ?,
            Acrescimo = ?,
            Quantidade = ?,
            Valor = ?,
            Total = ?
        WHERE Id = ?;
        """,
        (
            venda, produto, desconto, desconto_produto, acrescimo, quantidade, valor, total, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return venda_produto

def deleteVendaProduto(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Vendas_Produtos WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
