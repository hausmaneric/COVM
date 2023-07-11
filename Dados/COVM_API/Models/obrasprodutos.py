from typing import Any
from Models.codigo import GeradorIDSequencial
from dataaccess.db import dbmsqls
from Models.baseClass import *

class Obras_Produtos(BaseClass):
    id                = 0
    obra              = 0
    produto           = 0
    desconto          = False
    desconto_produto  = 0.0
    desconto_total    = 0.0
    frete             = 0.0
    acrescimo         = 0.0
    produtos          = False
    quantidade        = 0.0
    valor             = 0.0
    total             = 0.0
    nomeproduto       = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:
        super().__init__(*args, **kwds)
        self.id               = 0
        self.obra             = 0
        self.produto          = 0
        self.desconto         = False
        self.desconto_produto = 0.0
        self.desconto_total   = 0.0
        self.frete            = 0.0
        self.acrescimo        = 0.0
        self.produtos         = False
        self.quantidade       = 0.0
        self.valor            = 0.0
        self.total            = 0.0
        self.nomeproduto      = ''

def getObrasProdutos():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
            op.Id, 
            op.Obra, 
            op.Produto, 
            op.Desconto, 
            op.Desconto_Produto, 
            op.Desconto_Total, 
            op.Frete, 
            op.Acrescimo,
            op.Produtos, 
            op.Quantidade, 
            op.Valor, 
            op.Total,
            p.nome as nomeproduto
        FROM Obras_Produtos as op
        LEFT JOIN Produtos as p ON op.Produto = p.id
        """
    )

    records = SQL.cur.fetchall()
    obras_produtos_list = []

    for r in records:
        obra_produto                   = Obras_Produtos()
        obra_produto.id                = r[0]
        obra_produto.obra              = r[1]
        obra_produto.produto           = r[2]
        obra_produto.desconto          = r[3]
        obra_produto.desconto_produto  = r[4]
        obra_produto.desconto_total    = r[5]
        obra_produto.frete             = r[6]
        obra_produto.acrescimo         = r[7]
        obra_produto.produtos          = r[8]
        obra_produto.quantidade        = r[9]
        obra_produto.valor             = r[10]
        obra_produto.total             = r[11]
        obra_produto.nomeproduto       = r[12]
        obras_produtos_list.append(obra_produto.__dict__)

    SQL.cur.close()

    return obras_produtos_list

def getObraProduto(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT 
            op.Id, 
            op.Obra, 
            op.Produto, 
            op.Desconto, 
            op.Desconto_Produto, 
            op.Desconto_Total, 
            op.Frete, 
            op.Acrescimo,
            op.Produtos, 
            op.Quantidade, 
            op.Valor, 
            op.Total,
            p.nome as nomeproduto
        FROM Obras_Produtos as op
        LEFT JOIN Produtos as p ON op.Produto = p.id
        WHERE op.Id = {id}
        """
    )

    records = SQL.cur.fetchall()
    obras_produtos_list = []

    for r in records:
        obra_produto                   = Obras_Produtos()
        obra_produto.id                = r[0]
        obra_produto.obra              = r[1]
        obra_produto.produto           = r[2]
        obra_produto.desconto          = r[3]
        obra_produto.desconto_produto  = r[4]
        obra_produto.desconto_total    = r[5]
        obra_produto.frete             = r[6]
        obra_produto.acrescimo         = r[7]
        obra_produto.produtos          = r[8]
        obra_produto.quantidade        = r[9]
        obra_produto.valor             = r[10]
        obra_produto.total             = r[11]
        obra_produto.nomeproduto       = r[12]
        obras_produtos_list.append(obra_produto.__dict__)

    SQL.cur.close()

    return obras_produtos_list

def postObraProduto(obra_produto: Obras_Produtos):
    obra               = obra_produto.obra
    produto            = obra_produto.produto
    desconto           = obra_produto.desconto
    desconto_produto   = obra_produto.desconto_produto
    desconto_total     = obra_produto.desconto_total
    frete              = obra_produto.frete
    acrescimo          = obra_produto.acrescimo
    produtos           = obra_produto.produtos
    quantidade         = obra_produto.quantidade
    valor              = obra_produto.valor
    total              = obra_produto.total

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Obras_Produtos ( Obra, Produto, Desconto, Desconto_Produto, Desconto_Total, Frete, Acrescimo,
                                    Produtos, Quantidade, Valor, Total)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
             obra, produto, desconto, desconto_produto, desconto_total, frete, acrescimo,
            produtos, quantidade, valor, total
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return obra_produto

def updateObraProduto(id: int, obra_produto: Obras_Produtos):
    obra               = obra_produto.obra
    produto            = obra_produto.produto
    desconto           = obra_produto.desconto
    desconto_produto   = obra_produto.desconto_produto
    desconto_total     = obra_produto.desconto_total
    frete              = obra_produto.frete
    acrescimo          = obra_produto.acrescimo
    produtos           = obra_produto.produtos
    quantidade         = obra_produto.quantidade
    valor              = obra_produto.valor
    total              = obra_produto.total

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Obras_Produtos
        SET Obra = ?,
            Produto = ?,
            Desconto = ?,
            Desconto_Produto = ?,
            Desconto_Total = ?,
            Frete = ?,
            Acrescimo = ?,
            Produtos = ?,
            Quantidade = ?,
            Valor = ?,
            Total = ?
        WHERE Id = ?;
        """,
        (
            obra, produto, desconto, desconto_produto, desconto_total, frete, acrescimo,
            produtos, quantidade, valor, total, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return obra_produto

def deleteObraProduto(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Obras_Produtos WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()

    return {"msg": "Deletado"}
