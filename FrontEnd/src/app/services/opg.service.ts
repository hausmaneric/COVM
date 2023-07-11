import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Opg } from '../models/opg';

@Injectable({
  providedIn: 'root'
})
export class OpgService {
  constructor(private http:HttpClient, private router: Router) { }

  getOpgs(){
    return this.http.get<Opg[]>("http://16.16.77.152/api1/opg/");
  }

  createOpg(payLoad:Opg){
    return this.http.post<Opg>(`http://16.16.77.152/api1/opg/`, payLoad);
  }

  getByIdOpg(id:number){
    return this.http.get<Opg>(`http://16.16.77.152/api1/opg/${id}`);
  }

  updateOpg(payLoad:Opg){
    return this.http.put(`http://16.16.77.152/api1/opg/${payLoad.id}`,payLoad);
  }

  deleteOpg(id:number){
    return this.http.delete<Opg>(`http://16.16.77.152/api1/opg/${id}`);
  }
}
