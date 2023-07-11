from typing import Any
from Models.codigo import GeradorIDSequencial
from dataaccess.db import dbmsqls
from Models.baseClass import *

class Obras_Imagem(BaseClass):
    id     = 0
    imagem = ''
    obra   = 0

    def __init__(self, *args: Any, **kwds: Any) -> None:
        super().__init__(*args, **kwds)
        self.id     = 0
        self.imagem = ''
        self.obra   = 0

def getObras_Imagem():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT Id, Imagem, Obra
        FROM Obras_Imagem
        """
    )
    
    records = SQL.cur.fetchall()
    obras_imagem_list = []
    
    for r in records:
        obras_imagem       = Obras_Imagem()
        obras_imagem.id    = r[0]
        obras_imagem.imagem = r[1]
        obras_imagem.obra   = r[2]
        obras_imagem_list.append(obras_imagem.__dict__)
    
    SQL.cur.close()
    
    return obras_imagem_list

def getObra_Imagem(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT Id, Imagem, Obra
        FROM Obras_Imagem
        WHERE Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    obras_imagem_list = []
    
    for r in records:
        obras_imagem       = Obras_Imagem()
        obras_imagem.id    = r[0]
        obras_imagem.imagem = r[1]
        obras_imagem.obra   = r[2]
        obras_imagem_list.append(obras_imagem.__dict__)
    
    SQL.cur.close()
    
    return obras_imagem_list

def postObra_Imagem(obras_imagem: Obras_Imagem):
    imagem = obras_imagem.imagem
    obra   = obras_imagem.obra

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Obras_Imagem ( Imagem, Obra)
        VALUES ( ?, ?)
        """,
        ( imagem, obra)
    )

    SQL.con.commit()
    SQL.con.close()

    return obras_imagem

def updateObra_Imagem(id: int, obras_imagem: Obras_Imagem):
    imagem = obras_imagem.imagem
    obra   = obras_imagem.obra

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Obras_Imagem
        SET Imagem = ?,
            Obra = ?
        WHERE Id = ?;
        """,
        (imagem, obra, id)
    )

    SQL.con.commit()
    SQL.con.close()

    return obras_imagem

def deleteObra_Imagem(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Obras_Imagem WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
