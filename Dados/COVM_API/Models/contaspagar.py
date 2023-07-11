from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class ContasPagar(BaseClass):
    id              = 0
    vencimento      = ''
    pagamento       = ''
    compra          = ''
    documento       = ''
    fornecedor      = 0
    historico       = ''
    valor           = 0.0
    juros           = 0.0
    total           = 0.0
    categoria       = 0
    nomefornecedor  = ''
    nomecategoria   = ''
    conta           = 0
    vencido         = False
    pago            = False
    nomeconta       = ''

    def __init__(self, *args: Any, **kwds: Any) -> None:
        super().__init__(*args, **kwds)
        self.id              = 0
        self.vencimento      = ''
        self.pagamento       = ''
        self.compra          = ''
        self.documento       = ''
        self.fornecedor      = 0
        self.historico       = ''
        self.valor           = 0.0
        self.juros           = 0.0
        self.total           = 0.0
        self.categoria       = 0
        self.nomefornecedor  = ''
        self.nomecategoria   = ''
        self.conta           = 0
        self.vencido         = False
        self.pago            = False
        self.nomeconta       = ''

def getContasPagar():
    SQL = dbmsqls()
    SQL.cur.execute(
       f"""
        UPDATE ContasPagar
        SET Vencido = CASE
            WHEN Pago = 1 THEN 0
            WHEN Pago = 0 AND CONVERT(DATE, Vencimento) < CONVERT(DATE, GETDATE()) THEN 1
            ELSE Vencido
        END
       """ 
    )    
    SQL.con.commit()
    
    SQL.cur.execute(
        """
        SELECT 
            ca.Id,
            ca.Vencimento, 
            ca.Pagamento, 
            ca.Compra, 
            ca.Documento, 
            ca.Fornecedor, 
            ca.Historico, 
            ca.Valor, 
            ca.Juros, 
            ca.Valor + (ca.Valor * ca.Juros * (DATEDIFF(day, ca.Vencimento, GETDATE())) / 100) AS Total,  
            ca.Categoria,
            f.nome as nomefornecedor,
            c.nome as nomecategoria,
            ca.conta,
            ca.vencido,
            ca.pago,
            ct.nome as nomeconta
        FROM ContasPagar as ca
        LEFT JOIN Fornecedores as f ON ca.Fornecedor = f.id
        LEFT JOIN Categoria as c ON ca.Categoria = c.id
        LEFT JOIN Contas as ct ON ca.Conta = ct.Id
        """
    )

    records = SQL.cur.fetchall()
    ContasPagar_list = []

    for r in records:
        conta_pagar                  = ContasPagar()
        conta_pagar.id               = r[0]
        conta_pagar.vencimento       = r[1]
        conta_pagar.pagamento        = r[2]
        conta_pagar.compra           = r[3]
        conta_pagar.documento        = r[4]
        conta_pagar.fornecedor       = r[5]
        conta_pagar.historico        = r[6]
        conta_pagar.valor            = r[7]
        conta_pagar.juros            = r[8]
        conta_pagar.total            = r[9]
        conta_pagar.categoria        = r[10]
        conta_pagar.nomefornecedor   = r[11]
        conta_pagar.nomecategoria    = r[12]
        conta_pagar.conta            = r[13]
        conta_pagar.vencido          = r[14]
        conta_pagar.pago             = r[15]
        conta_pagar.nomeconta        = r[16]
        ContasPagar_list.append(conta_pagar.__dict__)

    SQL.cur.close()

    return ContasPagar_list

def getContaPagar(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
       f"""
        UPDATE ContasPagar
        SET Vencido = CASE
            WHEN Pago = 1 THEN 0
            WHEN Pago = 0 AND CONVERT(DATE, Vencimento) < CONVERT(DATE, GETDATE()) THEN 1
            ELSE Vencido
        END
       """ 
    )    
    SQL.con.commit()
    
    SQL.cur.execute(
        f"""
        SELECT 
            ca.Id,
            ca.Vencimento, 
            ca.Pagamento, 
            ca.Compra, 
            ca.Documento, 
            ca.Fornecedor, 
            ca.Historico, 
            ca.Valor, 
            ca.Juros, 
            ca.Valor + (ca.Valor * ca.Juros * (DATEDIFF(day, ca.Vencimento, GETDATE())) / 100) AS Total,  
            ca.Categoria,
            f.nome as nomefornecedor,
            c.nome as nomecategoria,
            ca.conta,
            ca.vencido,
            ca.pago,
            ct.nome as nomeconta
        FROM ContasPagar as ca
        LEFT JOIN Fornecedores as f ON ca.Fornecedor = f.id
        LEFT JOIN Categoria as c ON ca.Categoria = c.id
        LEFT JOIN Contas as ct ON ca.Conta = ct.Id
        WHERE ca.Id = {id}
        """
    )

    records = SQL.cur.fetchall()
    conta_pagar_list = []

    for r in records:
        conta_pagar                  = ContasPagar()
        conta_pagar.id               = r[0]
        conta_pagar.vencimento       = r[1]
        conta_pagar.pagamento        = r[2]
        conta_pagar.compra           = r[3]
        conta_pagar.documento        = r[4]
        conta_pagar.fornecedor       = r[5]
        conta_pagar.historico        = r[6]
        conta_pagar.valor            = r[7]
        conta_pagar.juros            = r[8]
        conta_pagar.total            = r[9]
        conta_pagar.categoria        = r[10]
        conta_pagar.nomefornecedor   = r[11]
        conta_pagar.nomecategoria    = r[12]
        conta_pagar.conta            = r[13]
        conta_pagar.vencido          = r[14]
        conta_pagar.pago             = r[15]
        conta_pagar.nomeconta        = r[16]
        conta_pagar_list.append(conta_pagar.__dict__)

    SQL.cur.close()

    return conta_pagar_list

def postContaPagar(conta_pagar: ContasPagar):
    vencimento      = conta_pagar.vencimento
    pagamento       = conta_pagar.pagamento
    compra          = conta_pagar.compra
    documento       = conta_pagar.documento
    fornecedor      = conta_pagar.fornecedor
    historico       = conta_pagar.historico
    valor           = conta_pagar.valor
    juros           = conta_pagar.juros
    total           = conta_pagar.total
    categoria       = conta_pagar.categoria
    conta           = conta_pagar.conta    
    vencido         = conta_pagar.vencido  
    pago            = conta_pagar.pago     
    nomeconta       = conta_pagar.nomeconta

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO ContasPagar (Vencimento, Pagamento, Compra, Documento, Fornecedor, Historico, Valor, Juros, Total, Categoria, Conta, Vencido, Pago, NomeConta)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            vencimento, pagamento, compra, documento, fornecedor, historico, valor, juros, total, categoria, conta, vencido, pago, nomeconta
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return conta_pagar

def updateContaPagar(id: int, conta_pagar: ContasPagar):
    vencimento      = conta_pagar.vencimento
    pagamento       = conta_pagar.pagamento
    compra          = conta_pagar.compra
    documento       = conta_pagar.documento
    fornecedor      = conta_pagar.fornecedor
    historico       = conta_pagar.historico
    valor           = conta_pagar.valor
    juros           = conta_pagar.juros
    total           = conta_pagar.total
    categoria       = conta_pagar.categoria
    conta           = conta_pagar.conta    
    vencido         = conta_pagar.vencido  
    pago            = conta_pagar.pago     
    nomeconta       = conta_pagar.nomeconta

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE ContasPagar
        SET Vencimento = ?,
            Pagamento = ?,
            Compra = ?,
            Documento = ?,
            Fornecedor = ?,
            Historico = ?,
            Valor = ?,
            Juros = ?,
            Total = ?,
            Categoria = ?,
            Conta = ?, 
            Vencido = ?, 
            Pago = ?, 
            NomeConta = ?
        WHERE Id = ?;
        """,
        (
            vencimento, pagamento, compra, documento, fornecedor, historico, valor, juros, total, categoria, conta, vencido, pago, nomeconta, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return conta_pagar

def deleteContaPagar(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM ContasPagar WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
