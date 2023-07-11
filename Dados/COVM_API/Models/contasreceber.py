from typing import Any
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class ContasReceber(BaseClass):
    id              = 0
    cliente         = 0
    venda           = 0
    documento       = ""
    vencimento      = ''
    pagamento       = ''
    historico       = ""
    recebido        = False
    negativado      = False
    conta           = 0
    categoria       = 0
    tipo            = 0
    nomeconta       = ''
    nomecliente     = ''
    nomecategoria   = ''
    nometipo        = ''
    vencido         = 0
    pago            = 0
    valor           = 0
    juros           = 0
    total           = 0

    def __init__(self, *args: Any, **kwds: Any) -> None:
        super().__init__(*args, **kwds)
        self.id              = 0
        self.cliente         = 0
        self.venda           = 0
        self.documento       = ""
        self.vencimento      = ''
        self.pagamento       = ''
        self.historico       = ""
        self.recebido        = False
        self.negativado      = False
        self.conta           = 0
        self.categoria       = 0
        self.tipo            = 0
        self.nomeconta       = ''
        self.nomecliente     = ''
        self.nomecategoria   = ''
        self.nometipo        = ''
        self.vencido         = 0
        self.pago            = 0
        self.valor           = 0
        self.juros           = 0
        self.total           = 0

def getContasReceber():
    SQL = dbmsqls()
    SQL.cur.execute(
       f"""
        UPDATE ContasReceber
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
        cr.Id, 
        cr.Cliente, 
        cr.Venda, 
        cr.Documento, 
        cr.Vencimento, 
        cr.Pagamento, 
        cr.Historico, 
        cr.Recebido, 
        cr.Negativado, 
        cr.Conta, 
        cr.Categoria, 
        cr.Tipo,
        c.nome as nomecliente,
        ct.nome as nomeconta,
        cg.nome as nomecategoria,
        cr.NomeTipo,
        cr.Vencido,
        cr.Pago,
        cr.Valor,
        cr.Juros,
        cr.Valor + (cr.Valor * cr.Juros * (DATEDIFF(day, cr.Vencimento, GETDATE())) / 100) AS Total
        FROM ContasReceber as cr
            LEFT JOIN Clientes as c ON cr.Cliente = c.id
            LEFT JOIN Contas as ct ON cr.Conta = ct.id
            LEFT JOIN Categoria as cg ON cr.Categoria = cg.id
        """
    )

    records = SQL.cur.fetchall()
    ContasReceber_list = []

    for r in records:
        conta_receber               = ContasReceber()
        conta_receber.id            = r[0]
        conta_receber.cliente       = r[1]
        conta_receber.venda         = r[2]
        conta_receber.documento     = r[3]
        conta_receber.vencimento    = r[4]
        conta_receber.pagamento     = r[5]
        conta_receber.historico     = r[6]
        conta_receber.recebido      = r[7]
        conta_receber.negativado    = r[8]
        conta_receber.conta         = r[9]
        conta_receber.categoria     = r[10]
        conta_receber.tipo          = r[11]
        conta_receber.nomecliente   = r[12]
        conta_receber.nomeconta     = r[13]        
        conta_receber.nomecategoria = r[14]
        conta_receber.nometipo      = r[15]
        conta_receber.vencido       = r[16]        
        conta_receber.pago          = r[17]
        conta_receber.valor         = r[18]
        conta_receber.juros         = r[19]
        conta_receber.total         = r[20]
        ContasReceber_list.append(conta_receber.__dict__)

    SQL.cur.close()

    return ContasReceber_list

def getContaReceber(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
       f"""
        UPDATE ContasReceber
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
            cr.Id, 
            cr.Cliente, 
            cr.Venda, 
            cr.Documento, 
            cr.Vencimento, 
            cr.Pagamento, 
            cr.Historico, 
            cr.Recebido, 
            cr.Negativado, 
            cr.Conta, 
            cr.Categoria, 
            cr.Tipo,
            c.nome as nomecliente,
            ct.nome as nomeconta,
            cg.nome as nomecategoria,
            cr.NomeTipo,
            cr.Vencido,
            cr.Pago,
            cr.Valor,
            cr.Juros,
            cr.Valor + (cr.Valor * cr.Juros * (DATEDIFF(day, cr.Vencimento, GETDATE())) / 100) AS Total
            FROM ContasReceber as cr
            LEFT JOIN Clientes as c ON cr.Cliente = c.id
            LEFT JOIN Contas as ct ON cr.Conta = ct.id
            LEFT JOIN Categoria as cg ON cr.Categoria = cg.id
            WHERE cr.Id = {id}
        """
    )

    records = SQL.cur.fetchall()
    conta_receber_list = []

    for r in records:
        conta_receber               = ContasReceber()
        conta_receber.id            = r[0]
        conta_receber.cliente       = r[1]
        conta_receber.venda         = r[2]
        conta_receber.documento     = r[3]
        conta_receber.vencimento    = r[4]
        conta_receber.pagamento     = r[5]
        conta_receber.historico     = r[6]
        conta_receber.recebido      = r[7]
        conta_receber.negativado    = r[8]
        conta_receber.conta         = r[9]
        conta_receber.categoria     = r[10]
        conta_receber.tipo          = r[11]
        conta_receber.nomecliente   = r[12]
        conta_receber.nomeconta     = r[13]        
        conta_receber.nomecategoria = r[14]
        conta_receber.nometipo      = r[15]
        conta_receber.vencido       = r[16]        
        conta_receber.pago          = r[17]
        conta_receber.valor         = r[18]
        conta_receber.juros         = r[19]
        conta_receber.total         = r[20]
        conta_receber_list.append(conta_receber.__dict__)

    SQL.cur.close()

    return conta_receber_list

def postContaReceber(conta_receber: ContasReceber):
    cliente         = conta_receber.cliente
    venda           = conta_receber.venda
    documento       = conta_receber.documento
    vencimento      = conta_receber.vencimento
    pagamento       = conta_receber.pagamento
    historico       = conta_receber.historico
    recebido        = conta_receber.recebido
    negativado      = conta_receber.negativado
    conta           = conta_receber.conta
    categoria       = conta_receber.categoria
    tipo            = conta_receber.tipo
    nometipo        = conta_receber.nometipo
    vencido         = conta_receber.vencido  
    pago            = conta_receber.pago   
    valor           = conta_receber.valor
    juros           = conta_receber.juros
    total           = conta_receber.total     

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO ContasReceber (Cliente, Venda, Documento, Vencimento, Pagamento, Historico, Recebido, Negativado, Conta, Categoria, Tipo, NomeTipo, Vencido, Pago, Valor, Juros, Total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            cliente, venda, documento, vencimento, pagamento, historico, recebido, negativado, conta, categoria, tipo, nometipo, vencido, pago, valor, juros, total
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return conta_receber

def updateContaReceber(id: int, conta_receber: ContasReceber):
    cliente         = conta_receber.cliente
    venda           = conta_receber.venda
    documento       = conta_receber.documento
    vencimento      = conta_receber.vencimento
    pagamento       = conta_receber.pagamento
    historico       = conta_receber.historico
    recebido        = conta_receber.recebido
    negativado      = conta_receber.negativado
    conta           = conta_receber.conta
    categoria       = conta_receber.categoria
    tipo            = conta_receber.tipo
    nometipo        = conta_receber.nometipo
    vencido         = conta_receber.vencido  
    pago            = conta_receber.pago  
    valor           = conta_receber.valor
    juros           = conta_receber.juros
    total           = conta_receber.total 
    
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE ContasReceber
        SET Cliente = ?,
            Venda = ?,
            Documento = ?,
            Vencimento = ?,
            Pagamento = ?,
            Historico = ?,
            Recebido = ?,
            Negativado = ?,
            Conta = ?,
            Categoria = ?,
            Tipo = ?,
            NomeTipo = ?, 
            Vencido = ?, 
            Pago = ?,
            Valor = ?, 
            Juros = ?, 
            Total = ?
        WHERE Id = ?;
        """,
        (
            cliente, venda, documento, vencimento, pagamento, historico, recebido, negativado, conta, categoria, tipo, nometipo, vencido, pago, valor, juros, total, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return conta_receber

def deleteContaReceber(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM ContasReceber WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
