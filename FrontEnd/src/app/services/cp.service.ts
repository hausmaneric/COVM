import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Cp } from '../models/cp';

@Injectable({
  providedIn: 'root'
})
export class CpService {

  constructor(private http:HttpClient, private router: Router) { }

  getCps(){
    return this.http.get<Cp[]>("http://16.16.77.152/api1/cp/");
  }

  createCp(payLoad:Cp){
    return this.http.post<Cp>(`http://16.16.77.152/api1/cp/`, payLoad);
  }

  getByIdCp(id:number){
    return this.http.get<Cp>(`http://16.16.77.152/api1/cp/${id}`);
  }

  updateCp(payLoad:Cp){
    return this.http.put(`http://16.16.77.152/api1/cp/${payLoad.id}`,payLoad);
  }

  deleteCp(id:number){
    return this.http.delete<Cp>(`http://16.16.77.152/api1/cp/${id}`);
  }
}

