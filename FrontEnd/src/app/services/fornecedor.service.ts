import { Injectable } from '@angular/core';
import { Fornecedor } from '../models/fornecedor';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class FornecedorService {

  constructor(private http:HttpClient, private router: Router) { }

  getFornecedors(){
    return this.http.get<Fornecedor[]>("http://16.16.77.152/api1/fornecedor/");
  }

  createFornecedor(payLoad:Fornecedor){
    return this.http.post<Fornecedor>(`http://16.16.77.152/api1/fornecedor/`, payLoad);
  }

  getByIdFornecedor(id:number){
    return this.http.get<Fornecedor>(`http://16.16.77.152/api1/fornecedor/${id}`);
  }

  updateFornecedor(payLoad:Fornecedor){
    return this.http.put(`http://16.16.77.152/api1/fornecedor/${payLoad.id}`,payLoad);
  }

  deleteFornecedor(id:number){
    return this.http.delete<Fornecedor>(`http://16.16.77.152/api1/fornecedor/${id}`);
  }
}
