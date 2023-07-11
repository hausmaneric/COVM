import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Cliente } from '../models/cliente';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {

  constructor(private http:HttpClient, private router: Router) { }

  getClientes(){
    return this.http.get<Cliente[]>("http://16.16.77.152/api1/cliente/");
  }

  createCliente(payLoad:Cliente){
    return this.http.post<Cliente>(`http://16.16.77.152/api1/cliente/`, payLoad);
  }

  getByIdCliente(id:number){
    return this.http.get<Cliente>(`http://16.16.77.152/api1/cliente/${id}`);
  }

  updateCliente(payLoad:Cliente){
    return this.http.put(`http://16.16.77.152/api1/cliente/${payLoad.id}`,payLoad);
  }

  deleteCliente(id:number){
    return this.http.delete<Cliente>(`http://16.16.77.152/api1/cliente/${id}`);
  }
}
