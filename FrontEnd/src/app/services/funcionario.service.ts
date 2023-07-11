import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Funcionario } from '../models/funcionario';

@Injectable({
  providedIn: 'root'
})
export class FuncionarioService {
  constructor(private http:HttpClient, private router: Router) { }

  getFuncionarios(){
    return this.http.get<Funcionario[]>("http://16.16.77.152/api1/funcionario/");
  }

  createFuncionario(payLoad:Funcionario){
    return this.http.post<Funcionario>(`http://16.16.77.152/api1/funcionario/`, payLoad);
  }

  getByIdFuncionario(id:number){
    return this.http.get<Funcionario>(`http://16.16.77.152/api1/funcionario/${id}`);
  }

  updateFuncionario(payLoad:Funcionario){
    return this.http.put(`http://16.16.77.152/api1/funcionario/${payLoad.id}`,payLoad);
  }

  deleteFuncionario(id:number){
    return this.http.delete<Funcionario>(`http://16.16.77.152/api1/funcionario/${id}`);
  }
}
