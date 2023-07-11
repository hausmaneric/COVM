from typing import Any
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class Obras(BaseClass):
    id                  = 0
    cliente             = 0
    data_inicial        = date.today()
    data_final          = date.today()
    desconto_valorfinal = 0.0
    desconto_diaria     = 0.0
    tipo                = 0
    metragem            = 0.0
    opg                 = 0
    nomecliente         = ''
    nomeopg             = ''

    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id                  = 0
        self.cliente             = 0
        self.data_inicial        = date.today()
        self.data_final          = date.today()
        self.desconto_valorfinal = 0.0
        self.desconto_diaria     = 0.0
        self.tipo                = 0
        self.metragem            = 0.0
        self.opg                 = 0
        self.nomecliente         = ''
        self.nomeopg             = ''
        
def getObras():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
        o.Id, 
        o.Cliente, 
        o.DataInicial, 
        o.DataFinal, 
        o.Desconto_ValorFinal, 
        o.Desconto_Diaria, 
        o.Tipo, 
        o.Metragem, 
        o.Opg,
        c.nome as nomecliente,
        op.nome as nomeopg
        FROM Obras as o
        LEFT JOIN Clientes as c ON o.Cliente = c.id
        LEFT JOIN Opcao_Pagamento as op ON o.Opg = op.id
        """
    )
    
    records = SQL.cur.fetchall()
    obra_list = []
    
    for r in records:
        obra                        = Obras()
        obra.id                     = r[0]
        obra.cliente                = r[1]
        obra.data_inicial           = r[2]
        obra.data_final             = r[3]
        obra.desconto_valorfinal    = r[4]
        obra.desconto_diaria        = r[5]
        obra.tipo                   = r[6]
        obra.metragem               = r[7]
        obra.opg                    = r[8]
        obra.nomecliente            = r[9]
        obra.nomeopg                = r[10]
        obra_list.append(obra.__dict__)
    
    SQL.cur.close()
    
    return obra_list

def getObra(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
            SELECT 
            o.Id, 
            o.Cliente, 
            o.DataInicial, 
            o.DataFinal, 
            o.Desconto_ValorFinal, 
            o.Desconto_Diaria, 
            o.Tipo, 
            o.Metragem, 
            o.Opg,
            c.nome as nomecliente,
            op.nome as nomeopg
            FROM Obras as o
            LEFT JOIN Clientes as c ON o.cliente = c.id
            LEFT JOIN Opcao_Pagamento as op ON o.opg = op.id
            WHERE o.Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    obra_list = []
    
    for r in records:
        obra                        = Obras()
        obra.id                     = r[0]
        obra.cliente                = r[1]
        obra.data_inicial           = r[2]
        obra.data_final             = r[3]
        obra.desconto_valorfinal    = r[4]
        obra.desconto_diaria        = r[5]
        obra.tipo                   = r[6]
        obra.metragem               = r[7]
        obra.opg                    = r[8]
        obra.nomecliente            = r[9]
        obra.nomeopg                = r[10]
        obra_list.append(obra.__dict__)
    
    SQL.cur.close()
    
    return obra_list

def postObra(obra: Obras):
    cliente             = obra.cliente
    data_inicial        = obra.data_inicial
    data_final          = obra.data_final
    desconto_valorfinal = obra.desconto_valorfinal
    desconto_diaria     = obra.desconto_diaria
    tipo                = obra.tipo
    metragem            = obra.metragem
    opg                 = obra.opg

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Obras ( Cliente, DataInicial, DataFinal, Desconto_ValorFinal, Desconto_Diaria, Tipo, Metragem, Opg)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            cliente, data_inicial, data_final, desconto_valorfinal, desconto_diaria, tipo, metragem, opg
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return obra

def updateObra(id: int, obra: Obras):
    cliente             = obra.cliente
    data_inicial        = obra.data_inicial
    data_final          = obra.data_final
    desconto_valorfinal = obra.desconto_valorfinal
    desconto_diaria     = obra.desconto_diaria
    tipo                = obra.tipo
    metragem            = obra.metragem
    opg                 = obra.opg

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Obras
        SET Cliente = ?,
            DataInicial = ?,
            DataFinal = ?,
            Desconto_ValorFinal = ?,
            Desconto_Diaria = ?,
            Tipo = ?,
            Metragem = ?,
            Opg = ?
        WHERE Id = ?;
        """,
        (
            cliente, data_inicial, data_final, desconto_valorfinal, desconto_diaria, tipo, metragem, opg, id
        )
    )

    SQL.con.commit()
    SQL.con.close()

    return obra

def deleteObra(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Obras WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
