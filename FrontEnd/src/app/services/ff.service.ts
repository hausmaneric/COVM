import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Ff } from '../models/ff';

@Injectable({
  providedIn: 'root'
})
export class FfService {
  constructor(private http:HttpClient, private router: Router) { }

  getFfs(){
    return this.http.get<Ff[]>("http://16.16.77.152/api1/ff/");
  }

  createFf(payLoad:Ff){
    return this.http.post<Ff>(`http://16.16.77.152/api1/ff/`, payLoad);
  }

  getByIdFf(id:number){
    return this.http.get<Ff>(`http://16.16.77.152/api1/ff/${id}`);
  }

  updateFf(payLoad:Ff){
    return this.http.put(`http://16.16.77.152/api1/ff/${payLoad.id}`,payLoad);
  }

  deleteFf(id:number){
    return this.http.delete<Ff>(`http://16.16.77.152/api1/ff/${id}`);
  }
}
