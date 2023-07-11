import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Ft } from '../models/ft';

@Injectable({
  providedIn: 'root'
})
export class FtService {
  constructor(private http:HttpClient, private router: Router) { }

  getFts(){
    return this.http.get<Ft[]>("http://16.16.77.152/api1/ft/");
  }

  createFt(payLoad:Ft){
    return this.http.post<Ft>(`http://16.16.77.152/api1/ft/`, payLoad);
  }

  getByIdFt(id:number){
    return this.http.get<Ft>(`http://16.16.77.152/api1/ft/${id}`);
  }

  updateFt(payLoad:Ft){
    return this.http.put(`http://16.16.77.152/api1/ft/${payLoad.id}`,payLoad);
  }

  deleteFt(id:number){
    return this.http.delete<Ft>(`http://16.16.77.152/api1/ft/${id}`);
  }
}
