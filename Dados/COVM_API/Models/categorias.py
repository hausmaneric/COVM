from typing import Any
from flask import jsonify
from Models.codigo import *
from dataaccess.db import *
from Models.baseClass import *

class Categoria(BaseClass):
    id       = 0
    codigo   = ''
    nome     = ''
    tipo     = 0
    nometipo = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id       = 0
        self.codigo   = ''
        self.nome     = ''
        self.tipo     = 0
        self.nometipo = ''
        
def getCategorias():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT Id, Codigo, Nome, Tipo, NomeTipo
        FROM Categoria
        """
    )
    
    records = SQL.cur.fetchall()
    categorias_list = []
    
    for r in records:
        categoria          = Categoria()
        categoria.id       = r[0]
        categoria.codigo   = r[1]
        categoria.nome     = r[2]
        categoria.tipo     = r[3]
        categoria.nometipo = r[4]
        categorias_list.append(categoria.__dict__)
    
    SQL.cur.close()
    
    return categorias_list

def getCategoria(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT Id, Codigo, Nome, Tipo, NomeTipo
        FROM Categoria
        WHERE Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    categorias_list = []
    
    for r in records:
        categoria          = Categoria()
        categoria.id       = r[0]
        categoria.codigo   = r[1]
        categoria.nome     = r[2]
        categoria.tipo     = r[3]
        categoria.nometipo = r[4]
        categorias_list.append(categoria.__dict__)
    
    SQL.cur.close()
    
    return categorias_list

def getCategoriaLast():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT TOP 1 Id, Codigo, Nome, Tipo, NomeTipo
        FROM Categoria ORDER BY id DESC
        """
    )
    
    records = SQL.cur.fetchall()
    categorias_list = []
    
    for r in records:
        categoria          = Categoria()
        categoria.id       = r[0]
        categoria.codigo   = r[1]
        categoria.nome     = r[2]
        categoria.tipo     = r[3]
        categoria.nometipo = r[4]
        categorias_list.append(categoria.__dict__)
    
    SQL.cur.close()
    
    return categorias_list


def postCategoria(categoria: Categoria):
    codigo   = categoria.codigo
    nome     = categoria.nome
    tipo     = categoria.tipo
    nometipo = categoria.nometipo

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Categoria (Codigo, Nome, Tipo, NomeTipo)
        VALUES (?, ?, ?, ?)
        """,
        (
            codigo, nome, tipo, nometipo
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return categoria

def updateCategoria(id: int, categoria: Categoria):
    codigo   = categoria.codigo
    nome     = categoria.nome
    tipo     = categoria.tipo
    nometipo = categoria.nometipo

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Categoria
        SET Codigo = ?,
            Nome = ?,
            Tipo = ?,
            NomeTipo = ?
        WHERE Id = ?;
        """,
        (
            codigo, nome, tipo, nometipo, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return categoria

def deleteCategoria(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Categoria WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.con.close()
    
    return {"msg": "Deletado"}
