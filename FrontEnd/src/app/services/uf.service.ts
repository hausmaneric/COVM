import { Uf } from '../models//uf';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UfService {

  constructor(private http:HttpClient) { }

  getUF(){
    return this.http.get<Uf[]>("https://servicodados.ibge.gov.br/api/v1/localidades/estados");
  }
}
