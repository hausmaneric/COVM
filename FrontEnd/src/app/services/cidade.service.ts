import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Cidade } from '../models/cidade';

@Injectable({
  providedIn: 'root'
})
export class CidadeService {

  constructor(private http:HttpClient) { }

  getCidade(UF:number){
    return this.http.get<Cidade[]>(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${UF}/distritos`);
  }
}
