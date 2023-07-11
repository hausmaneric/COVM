import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Produto } from '../models/produto';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {
  constructor(private http:HttpClient, private router: Router) { }

  getProdutos(){
    return this.http.get<Produto[]>("http://16.16.77.152/api1/produto/");
  }

  createProduto(payLoad:Produto){
    return this.http.post<Produto>(`http://16.16.77.152/api1/produto/`, payLoad);
  }

  getByIdProduto(id:number){
    return this.http.get<Produto>(`http://16.16.77.152/api1/produto/${id}`);
  }

  updateProduto(payLoad:Produto){
    return this.http.put(`http://16.16.77.152/api1/produto/${payLoad.id}`,payLoad);
  }

  deleteProduto(id:number){
    return this.http.delete<Produto>(`http://16.16.77.152/api1/produto/${id}`);
  }
}
