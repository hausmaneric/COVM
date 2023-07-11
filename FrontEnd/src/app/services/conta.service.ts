import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Conta } from '../models/conta';

@Injectable({
  providedIn: 'root'
})
export class ContaService {

  constructor(private http:HttpClient, private router: Router) { }

  getContas(){
    return this.http.get<Conta[]>("http://16.16.77.152/api1/conta/");
  }

  createConta(payLoad:Conta){
    return this.http.post<Conta>(`http://16.16.77.152/api1/conta/`, payLoad);
  }

  getByIdConta(id:number){
    return this.http.get<Conta>(`http://16.16.77.152/api1/conta/${id}`);
  }

  updateConta(payLoad:Conta){
    return this.http.put(`http://16.16.77.152/api1/conta/${payLoad.id}`,payLoad);
  }

  deleteConta(id:number){
    return this.http.delete<Conta>(`http://16.16.77.152/api1/conta/${id}`);
  }
}
