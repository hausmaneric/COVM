from typing import Any
from Models.codigo import GeradorIDSequencial
from dataaccess.db import *
from Models.baseClass import *

class Usuarios(BaseClass):
    id              = 0
    login           = ''
    email           = ''
    funcionario     = 0
    nivel           = 0
    senha           = ''
    nomefuncionario = ''

    def __init__(self, *args: Any, **kwds: Any) -> Any:
        super().__init__(*args, **kwds) 
        self.id              = 0
        self.login           = ''
        self.email           = ''
        self.funcionario     = 0
        self.nivel           = 0
        self.senha           = ''
        self.nomefuncionario = ''
        
def getUsuarios():
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        SELECT 
            u.Id, 
            u.Login,             
            u.Funcionario, 
            u.Nivel, 
            u.Senha,
            f.nome as nomefuncionario,
            u.Email
        FROM Usuarios as u
        LEFT JOIN Funcionarios as f ON u.Funcionario = f.id
        """
    )
    
    records = SQL.cur.fetchall()
    usuario_list = []
    
    for r in records:
        usuario                 = Usuarios()
        usuario.id              = r[0]
        usuario.login           = r[1]
        usuario.funcionario     = r[2]
        usuario.nivel           = r[3]
        usuario.senha           = r[4]
        usuario.nomefuncionario = r[5]
        usuario.email           = r[6]
        usuario_list.append(usuario.__dict__)
    
    SQL.cur.close()
    
    return usuario_list

def getUsuario(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        f"""
        SELECT 
            u.Id, 
            u.Login, 
            u.Funcionario, 
            u.Nivel, 
            u.Senha,
            f.nome as nomefuncionario,
            u.Email
        FROM Usuarios as u
        LEFT JOIN Funcionarios as f ON u.Funcionario = f.id
        WHERE u.Id = {id}
        """
    )
    
    records = SQL.cur.fetchall()
    usuario_list = []
    
    for r in records:
        usuario                 = Usuarios()
        usuario.id              = r[0]
        usuario.login           = r[1]
        usuario.funcionario     = r[2]
        usuario.nivel           = r[3]
        usuario.senha           = r[4]
        usuario.nomefuncionario = r[5]
        usuario.email           = r[6]
        usuario_list.append(usuario.__dict__)
    
    SQL.cur.close()
    
    return usuario_list

def postUsuario(usuario: Usuarios):
    login         = usuario.login
    email         = usuario.email
    funcionario   = usuario.funcionario
    nivel         = usuario.nivel
    senha         = usuario.senha

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        INSERT INTO Usuarios ( Login, Email, Funcionario, Nivel, Senha)
        VALUES (?, ?, ?, ?, ?)
        """,
        ( login, email, funcionario, nivel, senha)
    )

    SQL.con.commit()
    SQL.con.close()

    return usuario

def updateUsuario(id: int, usuario: Usuarios):
    login         = usuario.login
    email         = usuario.email
    funcionario   = usuario.funcionario
    nivel         = usuario.nivel
    senha         = usuario.senha

    SQL = dbmsqls()
    SQL.cur.execute(
        """
        UPDATE Usuarios
        SET 
            Login = ?,
            Email = ?,
            Funcionario = ?,
            Nivel = ?,
            Senha = ?
        WHERE Id = ?;
        """,
        (login, email, funcionario, nivel, senha, id)
    )

    SQL.con.commit()
    SQL.con.close()

    return usuario

def deleteUsuario(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(
        """
        DELETE FROM Usuarios WHERE Id = ?
        """,
        (id,)
    )
    SQL.con.commit()
    SQL.cur.close()
    
    return {"msg": "Deletado"}