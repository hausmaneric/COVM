from typing import Any
from datetime import date
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *

class OpcaoPagamento(BaseClass):
    id             = 0
    tipo           = 0
    brinde         = 0
    nome           = ""
    taxa           = 0.0
    desconto       = 0.0
    parcelas       = 0
    entrada        = 0.0
    com_entrada    = False
    av_entrada     = False
    av_parcelas    = False
    carne          = False
    e_boleto       = False
    v_dinheiro     = False
    v_cheque       = False
    v_debito       = False
    v_credito      = False
    v_financeira   = False
    v_pix          = False
    a_cartao       = False
    a_crediario    = False
    a_boleto       = False
    a_duplicata    = False

    def __init__(self, *args: Any, **kwds: Any) -> None:
        super().__init__(*args, **kwds)
        self.id             = 0
        self.tipo           = 0
        self.brinde         = 0
        self.nome           = ""
        self.taxa           = 0.0
        self.desconto       = 0.0
        self.parcelas       = 0
        self.entrada        = 0.0
        self.com_entrada    = False
        self.av_entrada     = False
        self.av_parcelas    = False
        self.carne          = False
        self.e_boleto       = False
        self.v_dinheiro     = False
        self.v_cheque       = False
        self.v_debito       = False
        self.v_credito      = False
        self.v_financeira   = False
        self.v_pix          = False
        self.a_cartao       = False
        self.a_crediario    = False
        self.a_boleto       = False
        self.a_duplicata    = False

def getOpcoesPagamento():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT Id, Tipo, Brinde, Nome, Taxa, Desconto, Parcelas, Entrada, ComEntrada, AVEntrada, AVParcelas,
               Carnê, EBoleto, VDinheiro, VCheque, VCDebito, VCCredito, VFinanceira, VPix, ACartao, ACrediario,
               ABoleto, ADuplicata
        FROM OpcaoPagamento
        """
    )

    records = SQL.cur.fetchall()
    opcao_pagamento_list = []

    for r in records:
        opcao_pagamento                 = OpcaoPagamento()
        opcao_pagamento.id              = r[0]
        opcao_pagamento.tipo            = r[1]
        opcao_pagamento.brinde          = r[2]
        opcao_pagamento.nome            = r[3]
        opcao_pagamento.taxa            = r[4]
        opcao_pagamento.desconto        = r[5]
        opcao_pagamento.parcelas        = r[6]
        opcao_pagamento.entrada         = r[7]
        opcao_pagamento.com_entrada     = (r[8])
        opcao_pagamento.av_entrada      = (r[9])
        opcao_pagamento.av_parcelas     = (r[10])
        opcao_pagamento.carne           = (r[11])
        opcao_pagamento.e_boleto        = (r[12])
        opcao_pagamento.v_dinheiro      = (r[13])
        opcao_pagamento.v_cheque        = (r[14])
        opcao_pagamento.v_debito        = (r[15])
        opcao_pagamento.v_credito       = (r[16])
        opcao_pagamento.v_financeira    = (r[17])
        opcao_pagamento.v_pix           = (r[18])
        opcao_pagamento.a_cartao        = (r[19])
        opcao_pagamento.a_crediario     = (r[20])
        opcao_pagamento.a_boleto        = (r[21])
        opcao_pagamento.a_duplicata     = (r[22])
        opcao_pagamento_list.append(opcao_pagamento.__dict__)

    SQL.cur.close()

    return opcao_pagamento_list

def getOpcaoPagamento(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT Id, Tipo, Brinde, Nome, Taxa, Desconto, Parcelas, Entrada, ComEntrada, AVEntrada, AVParcelas,
               Carnê, EBoleto, VDinheiro, VCheque, VCDebito, VCCredito, VFinanceira, VPix, ACartao, ACrediario,
               ABoleto, ADuplicata
        FROM OpcaoPagamento
        WHERE Id = {id}
        """
    )

    records = SQL.cur.fetchall()
    opcao_pagamento_list = []

    for r in records:
        opcao_pagamento                 = OpcaoPagamento()
        opcao_pagamento.id              = r[0]
        opcao_pagamento.tipo            = r[1]
        opcao_pagamento.brinde          = r[2]
        opcao_pagamento.nome            = r[3]
        opcao_pagamento.taxa            = r[4]
        opcao_pagamento.desconto        = r[5]
        opcao_pagamento.parcelas        = r[6]
        opcao_pagamento.entrada         = r[7]
        opcao_pagamento.com_entrada     = (r[8])
        opcao_pagamento.av_entrada      = (r[9])
        opcao_pagamento.av_parcelas     = (r[10])
        opcao_pagamento.carne           = (r[11])
        opcao_pagamento.e_boleto        = (r[12])
        opcao_pagamento.v_dinheiro      = (r[13])
        opcao_pagamento.v_cheque        = (r[14])
        opcao_pagamento.v_debito        = (r[15])
        opcao_pagamento.v_credito       = (r[16])
        opcao_pagamento.v_financeira    = (r[17])
        opcao_pagamento.v_pix           = (r[18])
        opcao_pagamento.a_cartao        = (r[19])
        opcao_pagamento.a_crediario     = (r[20])
        opcao_pagamento.a_boleto        = (r[21])
        opcao_pagamento.a_duplicata     = (r[22])
        opcao_pagamento_list.append(opcao_pagamento.__dict__)

    SQL.cur.close()

    return opcao_pagamento_list

def postOpcaoPagamento(opcao_pagamento: OpcaoPagamento):
    tipo            = opcao_pagamento.tipo
    brinde          = opcao_pagamento.brinde
    nome            = opcao_pagamento.nome
    taxa            = opcao_pagamento.taxa
    desconto        = opcao_pagamento.desconto
    parcelas        = opcao_pagamento.parcelas
    entrada         = opcao_pagamento.entrada
    com_entrada     = opcao_pagamento.com_entrada
    av_entrada      = opcao_pagamento.av_entrada
    av_parcelas     = opcao_pagamento.av_parcelas
    carne           = opcao_pagamento.carne
    e_boleto        = opcao_pagamento.e_boleto
    v_dinheiro      = opcao_pagamento.v_dinheiro
    v_cheque        = opcao_pagamento.v_cheque
    v_debito        = opcao_pagamento.v_debito
    v_credito       = opcao_pagamento.v_credito
    v_financeira    = opcao_pagamento.v_financeira
    v_pix           = opcao_pagamento.v_pix
    a_cartao        = opcao_pagamento.a_cartao
    a_crediario     = opcao_pagamento.a_crediario
    a_boleto        = opcao_pagamento.a_boleto
    a_duplicata     = opcao_pagamento.a_duplicata

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO OpcaoPagamento ( Tipo, Brinde, Nome, Taxa, Desconto, Parcelas, Entrada, ComEntrada, AVEntrada,
                                     AVParcelas, Carnê, EBoleto, VDinheiro, VCheque, VCDebito, VCCredito, VFinanceira,
                                     VPix, ACartao, ACrediario, ABoleto, ADuplicata)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            tipo, brinde, nome, taxa, desconto, parcelas, entrada, com_entrada, av_entrada, av_parcelas, carne,
            e_boleto, v_dinheiro, v_cheque, v_debito, v_credito, v_financeira, v_pix, a_cartao, a_crediario,
            a_boleto, a_duplicata
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return opcao_pagamento

def updateOpcaoPagamento(id: int, opcao_pagamento: OpcaoPagamento):
    tipo            = opcao_pagamento.tipo
    brinde          = opcao_pagamento.brinde
    nome            = opcao_pagamento.nome
    taxa            = opcao_pagamento.taxa
    desconto        = opcao_pagamento.desconto
    parcelas        = opcao_pagamento.parcelas
    entrada         = opcao_pagamento.entrada
    com_entrada     = opcao_pagamento.com_entrada
    av_entrada      = opcao_pagamento.av_entrada
    av_parcelas     = opcao_pagamento.av_parcelas
    carne           = opcao_pagamento.carne
    e_boleto        = opcao_pagamento.e_boleto
    v_dinheiro      = opcao_pagamento.v_dinheiro
    v_cheque        = opcao_pagamento.v_cheque
    v_debito        = opcao_pagamento.v_debito
    v_credito       = opcao_pagamento.v_credito
    v_financeira    = opcao_pagamento.v_financeira
    v_pix           = opcao_pagamento.v_pix
    a_cartao        = opcao_pagamento.a_cartao
    a_crediario     = opcao_pagamento.a_crediario
    a_boleto        = opcao_pagamento.a_boleto
    a_duplicata     = opcao_pagamento.a_duplicata

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE OpcaoPagamento
        SET Tipo = ?,
            Brinde = ?,
            Nome = ?,
            Taxa = ?,
            Desconto = ?,
            Parcelas = ?,
            Entrada = ?,
            ComEntrada = ?,
            AVEntrada = ?,
            AVParcelas = ?,
            Carnê = ?,
            EBoleto = ?,
            VDinheiro = ?,
            VCheque = ?,
            VCDebito = ?,
            VCCredito = ?,
            VFinanceira = ?,
            VPix = ?,
            ACartao = ?,
            ACrediario = ?,
            ABoleto = ?,
            ADuplicata = ?
        WHERE Id = ?
        """,
        (
            tipo, brinde, nome, taxa, desconto, parcelas, entrada, com_entrada, av_entrada, av_parcelas, carne,
            e_boleto, v_dinheiro, v_cheque, v_debito, v_credito, v_financeira, v_pix, a_cartao, a_crediario,
            a_boleto, a_duplicata, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return opcao_pagamento

def deleteOpcaoPagamento(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        DELETE FROM OpcaoPagamento
        WHERE Id = {id}
        """
    )

    SQL.con.commit()
    SQL.con.close()

    return jsonify({"message": "Opção de pagamento deletada com sucesso."})

