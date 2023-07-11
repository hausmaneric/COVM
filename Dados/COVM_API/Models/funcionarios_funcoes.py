from typing import Any, overload
from flask import jsonify
from Models.codigo import *
from dataaccess.db import *
from Models.baseClass import *
from datetime import date

class FuncionarioFuncao:
    id              = 0
    nome            = ""
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds) 
        self.id                 = 0
        self.nome               = ""

def getFuncionarioFuncaoList():
    funcionario_Funcao_list = []

    SQL = dbmsqls()
    SQL.cur.execute("""
                    SELECT 
                    ff.Id, 
                    ff.Nome
                    FROM Funcionario_Funcao as ff
                    """)
    rows = SQL.cur.fetchall()

    for r in rows:
        funcionario_Funcao                    = FuncionarioFuncao()
        funcionario_Funcao.id                 = r[0]
        funcionario_Funcao.nome               = r[1]
        funcionario_Funcao_list.append(funcionario_Funcao.__dict__)

    SQL.cur.close()

    return funcionario_Funcao_list

def getFuncionarioFuncao(id: int):
    funcionario_Funcao_list = []

    SQL = dbmsqls()
    SQL.cur.execute(f"""
                        SELECT 
                        ff.Id, 
                        ff.Nome
                        FROM Funcionario_Funcao as ff
                        WHERE ff.Id = {id}
                    """)
    rows = SQL.cur.fetchall()

    for r in rows:
        funcionario_Funcao                    = FuncionarioFuncao()
        funcionario_Funcao.id                 = r[0]
        funcionario_Funcao.nome               = r[1]
        funcionario_Funcao_list.append(funcionario_Funcao.__dict__)

    SQL.cur.close()

    return funcionario_Funcao_list

def postFuncionarioFuncao(funcionarios_Funcao: FuncionarioFuncao):
    nome            = funcionarios_Funcao.nome

    SQL = dbmsqls()
    SQL.cur.execute(
        "INSERT INTO Funcionario_Funcao (Nome) VALUES (?)",
        (nome)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return funcionarios_Funcao


def updateFuncionarioFuncao(id: int, funcionarios_Funcao: FuncionarioFuncao):
    nome            = funcionarios_Funcao.nome

    SQL = dbmsqls()
    SQL.cur.execute(
        "UPDATE Funcionario_Funcao SET Nome = ?  WHERE Id = ?",
        (nome, id)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return funcionarios_Funcao


def deleteFuncionarioFuncao(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        "DELETE FROM Funcionario_Funcao WHERE Id = ?",
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}
