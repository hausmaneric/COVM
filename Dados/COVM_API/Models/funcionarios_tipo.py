from typing import Any, overload
from flask import jsonify
from Models.codigo import *
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class FuncionarioTipo:
    id              = 0
    nome            = ""
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id                 = 0
        self.nome               = ""

def getFuncionarioTipoList():
    funcionario_tipo_list = []

    SQL = dbmsqls()
    SQL.cur.execute("""
                    SELECT 
                    ft.Id, 
                    ft.Nome
                    FROM Funcionario_Tipo as ft
                    """)
    rows = SQL.cur.fetchall()

    for r in rows:
        funcionario_tipo                    = FuncionarioTipo()
        funcionario_tipo.id                 = r[0]
        funcionario_tipo.nome               = r[1]
        funcionario_tipo_list.append(funcionario_tipo.__dict__)

    SQL.cur.close()

    return funcionario_tipo_list

def getFuncionarioTipo(id: int):
    funcionario_tipo_list = []

    SQL = dbmsqls()
    SQL.cur.execute(f"""
                        SELECT 
                        ft.Id, 
                        ft.Nome
                        FROM Funcionario_Tipo as ft
                        WHERE ft.Id = {id}
                    """)
    rows = SQL.cur.fetchall()

    for r in rows:
        funcionario_tipo                    = FuncionarioTipo()
        funcionario_tipo.id                 = r[0]
        funcionario_tipo.nome               = r[1]
        funcionario_tipo_list.append(funcionario_tipo.__dict__)

    SQL.cur.close()

    return funcionario_tipo_list

def postFuncionarioTipo(funcionarios_tipo: FuncionarioTipo):
    nome            = funcionarios_tipo.nome

    SQL = dbmsqls()
    SQL.cur.execute(
        "INSERT INTO Funcionario_Tipo (Nome) VALUES (?)",
        (nome)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return funcionarios_tipo


def updateFuncionarioTipo(id: int, funcionarios_tipo: FuncionarioTipo):
    nome            = funcionarios_tipo.nome

    SQL = dbmsqls()
    SQL.cur.execute(
        "UPDATE Funcionario_Tipo SET Nome = ?  WHERE Id = ?",
        (nome, id)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return funcionarios_tipo


def deleteFuncionarioTipo(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Funcionario_Tipo WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
