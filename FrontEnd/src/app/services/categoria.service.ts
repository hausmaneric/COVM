import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Categoria } from '../models/categoria';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {

  constructor(private http:HttpClient, private router: Router) { }

  getLastCategoria(): Observable<Categoria> {
    // Fazer uma requisição GET para a API para obter o último registro
    return this.http.get<Categoria>(`http://16.16.77.152/api1/categorialast?_sort=id&_order=desc&_limit=1`);
  }

  getCategoria(){
    return this.http.get<Categoria[]>("http://16.16.77.152/api1/categoria/");
  }

  createCategoria(payLoad:Categoria){
    return this.http.post<Categoria>(`http://16.16.77.152/api1/categoria/`, payLoad);
  }

  getByIdCategoria(id:number){
    return this.http.get<Categoria>(`http://16.16.77.152/api1/categoria/${id}`);
  }

  updateCategoria(payLoad:Categoria){
    return this.http.put(`http://16.16.77.152/api1/categoria/${payLoad.id}`,payLoad);
  }

  deleteCategoria(id:number){
    return this.http.delete<Categoria>(`http://16.16.77.152/api1/categoria/${id}`);
  }
}
