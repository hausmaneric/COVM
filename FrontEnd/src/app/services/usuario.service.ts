import { Router } from '@angular/router';
import { LoginComponent } from '../components/login/login.component';
import { HttpClient } from '@angular/common/http';
import { Component, EventEmitter, Injectable } from '@angular/core';
import { Usuario } from '../models/usuario';
import { MatDialog } from '@angular/material/dialog';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http:HttpClient, private router: Router) { }

  public Autenticado: boolean = false;

  usuario!: Usuario;

  mostrarMenuEmitter = new EventEmitter<boolean>();
  mostrarMenuEmitterFalse = new EventEmitter<boolean>();
  mostrarNome = new EventEmitter<string>();
  mostrarImg = new EventEmitter<string>();
  nome!: string;

  getUsuario(){
    return this.http.get<Usuario[]>("http://16.16.77.152/api1/usuario/");
  }

  getEmail(login:string){
    return this.http.get<Usuario[]>(`http://16.16.77.152/api1/clienteemail/${login}`);
  }

  createUsuario(payLoad:Usuario){
    return this.http.post<Usuario>(`http://16.16.77.152/api1/usuario/`, payLoad);
  }

  getByIdUsuario(id:number){
    return this.http.get<Usuario>(`http://16.16.77.152/api1/usuario/${id}`);
  }

  updateUsuario(payLoad:Usuario){
    return this.http.put(`http://16.16.77.152/api1/usuario/${payLoad.id}`,payLoad);
  }

  deleteUsuario(id:number){
    return this.http.delete<Usuario>(`http://16.16.77.152/api1/usuario/${id}`);
  }

  logar(login: string, senha: string, func:any){

    this.getUsuario().subscribe(res=>{
      const user = res.find((a: any) =>{
          return a.login === login && a.senha === senha
      });
      if(user?.login =='' || user?.senha == ''){
        return func
      }
      else if(user){
        this.Autenticado = true;
        this.mostrarMenuEmitter.emit(true);
        this.mostrarMenuEmitterFalse.emit(false);
        this.nome = user.login;
        this.mostrarNome.emit(this.nome);
        // this.mostrarImg.emit(user.image)
        // alert(this.nome)
        this.router.navigate(['home']);
      }else{
        // func1
        this.mostrarMenuEmitter.emit(false);
      }
    },error=>{
      alert("Somethin went wrong");
    })
  }

  usuarioAutenticado(){
    return this.Autenticado;
  }
}
