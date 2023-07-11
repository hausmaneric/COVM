import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Cr } from '../models/cr';

@Injectable({
  providedIn: 'root'
})
export class CrService {

  constructor(private http:HttpClient, private router: Router) { }

  getCrs(){
    return this.http.get<Cr[]>("http://16.16.77.152/api1/cr/");
  }

  createCr(payLoad:Cr){
    return this.http.post<Cr>(`http://16.16.77.152/api1/cr/`, payLoad);
  }

  getByIdCr(id:number){
    return this.http.get<Cr>(`http://16.16.77.152/api1/cr/${id}`);
  }

  updateCr(payLoad:Cr){
    return this.http.put(`http://16.16.77.152/api1/cr/${payLoad.id}`,payLoad);
  }

  deleteCr(id:number){
    return this.http.delete<Cr>(`http://16.16.77.152/api1/cr/${id}`);
  }
}
