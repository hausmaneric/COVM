import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Veiculo } from '../models/veiculo';

@Injectable({
  providedIn: 'root'
})
export class VeiculoService {
  constructor(private http:HttpClient, private router: Router) { }

  getVeiculos(){
    return this.http.get<Veiculo[]>("http://16.16.77.152/api1/veiculo/");
  }

  createVeiculo(payLoad:Veiculo){
    return this.http.post<Veiculo>(`http://16.16.77.152/api1/veiculo/`, payLoad);
  }

  getByIdVeiculo(id:number){
    return this.http.get<Veiculo>(`http://16.16.77.152/api1/veiculo/${id}`);
  }

  updateVeiculo(payLoad:Veiculo){
    return this.http.put(`http://16.16.77.152/api1/veiculo/${payLoad.id}`,payLoad);
  }

  deleteVeiculo(id:number){
    return this.http.delete<Veiculo>(`http://16.16.77.152/api1/veiculo/${id}`);
  }
}
