import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Vt } from '../models/vt';

@Injectable({
  providedIn: 'root'
})
export class VtService {
  constructor(private http:HttpClient, private router: Router) { }

  getVts(){
    return this.http.get<Vt[]>("http://16.16.77.152/api1/vt/");
  }

  createVt(payLoad:Vt){
    return this.http.post<Vt>(`http://16.16.77.152/api1/vt/`, payLoad);
  }

  getByIdVt(id:number){
    return this.http.get<Vt>(`http://16.16.77.152/api1/vt/${id}`);
  }

  updateVt(payLoad:Vt){
    return this.http.put(`http://16.16.77.152/api1/vt/${payLoad.id}`,payLoad);
  }

  deleteVt(id:number){
    return this.http.delete<Vt>(`http://16.16.77.152/api1/vt/${id}`);
  }
}
