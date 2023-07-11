from typing import Any, overload
from flask import jsonify
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Produtos(BaseClass):
    id                     = 0
    nome                   = ''
    descricao              = ''
    CodigoDeBarras         = ''
    unidade                = ''
    desconto               = 0
    desconto_maximo        = 0
    peso                   = 0
    tamanho                = 0
    quantidade             = 0
    entrega                = 0
    quantidade_minima      = 0
    preco_compra           = 0
    margem                 = 0
    preco_venda            = 0
    margem_1               = 0
    preco_venda_1          = 0
    promocao               = False
    margem_promocao        = 0
    preco_venda_promocao   = 0
    atacado                = False
    minimo_atacado         = 0
    margem_atacado         = 0
    preco_venda_atacado    = 0
    ultima_venda           = date.today()
    ultima_compra          = date.today()
    imagem                 = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        
        self.id                     = 0
        self.nome                   = ''
        self.descricao              = ''
        self.CodigoDeBarras         = ''
        self.unidade                = ''
        self.desconto               = 0
        self.desconto_maximo        = 0
        self.peso                   = 0
        self.tamanho                = 0
        self.quantidade             = 0
        self.entrega                = 0
        self.quantidade_minima      = 0
        self.preco_compra           = 0
        self.margem                 = 0
        self.preco_venda            = 0
        self.margem_1               = 0
        self.preco_venda_1          = 0
        self.promocao               = False
        self.margem_promocao        = 0
        self.preco_venda_promocao   = 0
        self.atacado                = False
        self.minimo_atacado         = 0
        self.margem_atacado         = 0
        self.preco_venda_atacado    = 0
        self.ultima_venda           = date.today()
        self.ultima_compra          = date.today()
        self.imagem                 = ''
    
def getProdutos():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
            SELECT Id, Nome, Descricao, CodigoDeBarras, Unidade, Desconto, DescontoMaximo, Peso, Tamanho,
                Quantidade, Entrega, Quantidade_Minima, Preco_Compra, Margem, Preco_Venda, Margem_1,
                Preco_Venda_1, Promocao, Margem_Promocao, Preco_Venda_Promocao, Atacado, Minimo_Atacado,
                Margem_Atacado, Preco_Venda_Atacado, Ultima_Venda, Ultima_Compra, Imagem
            FROM Produtos
        """
    )
    
    records = SQL.cur.fetchall()    
    _list = []
    
    for r in records:
        _produto                        = Produtos()
        _produto.id                     = r[0]
        _produto.nome                   = r[1]
        _produto.descricao              = r[2]
        _produto.CodigoDeBarras         = r[3]
        _produto.unidade                = r[4]
        _produto.desconto               = r[5]
        _produto.desconto_maximo        = r[6]
        _produto.peso                   = r[7]
        _produto.tamanho                = r[8]
        _produto.quantidade             = r[9]
        _produto.entrega                = r[10]
        _produto.quantidade_minima      = r[11]
        _produto.preco_compra           = r[12]
        _produto.margem                 = r[13]
        _produto.preco_venda            = r[14]
        _produto.margem_1               = r[15]
        _produto.preco_venda_1          = r[16]
        _produto.promocao               = r[17]
        _produto.margem_promocao        = r[18]
        _produto.preco_venda_promocao   = r[19]
        _produto.atacado                = r[20]
        _produto.minimo_atacado         = r[21]
        _produto.margem_atacado         = r[22]
        _produto.preco_venda_atacado    = r[23]
        _produto.ultima_venda           = r[24]
        _produto.ultima_compra          = r[25]
        _produto.imagem                 = r[26]
        _list.append(_produto.__dict__)          

    SQL.cur.close() 

    return _list 

def getProduto(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
            SELECT Id, Nome, Descricao, CodigoDeBarras, Unidade, Desconto, DescontoMaximo, Peso, Tamanho,
                Quantidade, Entrega, Quantidade_Minima, Preco_Compra, Margem, Preco_Venda, Margem_1,
                Preco_Venda_1, Promocao, Margem_Promocao, Preco_Venda_Promocao, Atacado, Minimo_Atacado,
                Margem_Atacado, Preco_Venda_Atacado, Ultima_Venda, Ultima_Compra, Imagem
            FROM Produtos
            WHERE id = {id}
        """
    )
    
    records = SQL.cur.fetchall()    
    _list = []
    
    for r in records:
        _produto                        = Produtos()
        _produto.id                     = r[0]
        _produto.nome                   = r[1]
        _produto.descricao              = r[2]
        _produto.CodigoDeBarras         = r[3]
        _produto.unidade                = r[4]
        _produto.desconto               = r[5]
        _produto.desconto_maximo        = r[6]
        _produto.peso                   = r[7]
        _produto.tamanho                = r[8]
        _produto.quantidade             = r[9]
        _produto.entrega                = r[10]
        _produto.quantidade_minima      = r[11]
        _produto.preco_compra           = r[12]
        _produto.margem                 = r[13]
        _produto.preco_venda            = r[14]
        _produto.margem_1               = r[15]
        _produto.preco_venda_1          = r[16]
        _produto.promocao               = r[17]
        _produto.margem_promocao        = r[18]
        _produto.preco_venda_promocao   = r[19]
        _produto.atacado                = r[20]
        _produto.minimo_atacado         = r[21]
        _produto.margem_atacado         = r[22]
        _produto.preco_venda_atacado    = r[23]
        _produto.ultima_venda           = r[24]
        _produto.ultima_compra          = r[25]
        _produto.imagem                 = r[26]
        _list.append(_produto.__dict__)          

    SQL.cur.close() 

    return _list

def postProduto(produto: Produtos):
    nome                   = produto.nome                
    descricao              = produto.descricao           
    CodigoDeBarras         = produto.CodigoDeBarras       
    unidade                = produto.unidade             
    desconto               = produto.desconto            
    desconto_maximo        = produto.desconto_maximo     
    peso                   = produto.peso                
    tamanho                = produto.tamanho             
    quantidade             = produto.quantidade          
    entrega                = produto.entrega             
    quantidade_minima      = produto.quantidade_minima   
    preco_compra           = produto.preco_compra        
    margem                 = produto.margem              
    preco_venda            = produto.preco_venda         
    margem_1               = produto.margem_1            
    preco_venda_1          = produto.preco_venda_1       
    promocao               = produto.promocao            
    margem_promocao        = produto.margem_promocao     
    preco_venda_promocao   = produto.preco_venda_promocao
    atacado                = produto.atacado             
    minimo_atacado         = produto.minimo_atacado      
    margem_atacado         = produto.margem_atacado      
    preco_venda_atacado    = produto.preco_venda_atacado 
    ultima_venda           = produto.ultima_venda        
    ultima_compra          = produto.ultima_compra       
    imagem                 = produto.imagem  
                
    SQL = dbmsqls() 
    SQL.cur.execute(
        """
            INSERT INTO Produtos ( Nome, Descricao, CodigoDeBarras, Unidade, Desconto, DescontoMaximo, Peso, Tamanho,
                      Quantidade, Entrega, Quantidade_Minima, Preco_Compra, Margem, Preco_Venda, Margem_1,
                      Preco_Venda_1, Promocao, Margem_Promocao, Preco_Venda_Promocao, Atacado, Minimo_Atacado,
                      Margem_Atacado, Preco_Venda_Atacado, Ultima_Venda, Ultima_Compra, Imagem)
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,( nome, descricao, CodigoDeBarras, unidade, desconto, desconto_maximo, peso, tamanho,
            quantidade, entrega, quantidade_minima, preco_compra, margem, preco_venda, margem_1,
            preco_venda_1, promocao, margem_promocao, preco_venda_promocao, atacado, minimo_atacado,
            margem_atacado, preco_venda_atacado, ultima_venda, ultima_compra, imagem)
    ) 
    
    SQL.con.commit()
    SQL.con.close()
    
    return produto

def updateProduto(id: int,produto: Produtos):
    nome                   = produto.nome                
    descricao              = produto.descricao           
    CodigoDeBarras         = produto.CodigoDeBarras       
    unidade                = produto.unidade             
    desconto               = produto.desconto            
    desconto_maximo        = produto.desconto_maximo     
    peso                   = produto.peso                
    tamanho                = produto.tamanho             
    quantidade             = produto.quantidade          
    entrega                = produto.entrega             
    quantidade_minima      = produto.quantidade_minima   
    preco_compra           = produto.preco_compra        
    margem                 = produto.margem              
    preco_venda            = produto.preco_venda         
    margem_1               = produto.margem_1            
    preco_venda_1          = produto.preco_venda_1       
    promocao               = produto.promocao            
    margem_promocao        = produto.margem_promocao     
    preco_venda_promocao   = produto.preco_venda_promocao
    atacado                = produto.atacado             
    minimo_atacado         = produto.minimo_atacado      
    margem_atacado         = produto.margem_atacado      
    preco_venda_atacado    = produto.preco_venda_atacado 
    ultima_venda           = produto.ultima_venda        
    ultima_compra          = produto.ultima_compra       
    imagem                 = produto.imagem  
                
    SQL = dbmsqls() 
    SQL.cur.execute(
        """
            UPDATE Produtos
            SET Nome = ?,
                Descricao = ?,
                CodigoDeBarras = ?,
                Unidade = ?,
                Desconto = ?,
                DescontoMaximo = ?,
                Peso = ?,
                Tamanho = ?,
                Quantidade = ?,
                Entrega = ?,
                Quantidade_Minima = ?,
                Preco_Compra = ?,
                Margem = ?,
                Preco_Venda = ?,
                Margem_1 = ?,
                Preco_Venda_1 = ?,
                Promocao = ?,
                Margem_Promocao = ?,
                Preco_Venda_Promocao = ?,
                Atacado = ?,
                Minimo_Atacado = ?,
                Margem_Atacado = ?,
                Preco_Venda_Atacado = ?,
                Ultima_Venda = ?,
                Ultima_Compra = ?,
                Imagem = ?
            WHERE Id = ?;""",
            (nome, descricao, CodigoDeBarras, unidade, desconto, desconto_maximo, peso, tamanho,
            quantidade, entrega, quantidade_minima, preco_compra, margem, preco_venda, margem_1,
            preco_venda_1, promocao, margem_promocao, preco_venda_promocao, atacado, minimo_atacado,
            margem_atacado, preco_venda_atacado, ultima_venda, ultima_compra, imagem, id)
    ) 
    
    SQL.con.commit()
    SQL.con.close()
    
    return produto

def deleteProduto(id: int):
    SQL = dbmsqls()
    SQL.cur.execute('DELETE FROM Produtos WHERE id = ?', [id])
    
    SQL.con.commit()
    SQL.con.close()
    
    return {"msg": "Deletado"}

