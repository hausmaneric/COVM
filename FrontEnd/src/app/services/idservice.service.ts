import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class IdserviceService {
  private id!: number;
  private idRec!: number;

  constructor() { }

  setId(id: number) {
    this.id = id;
  }

  getId() {
    return this.id;
  }

  setIdRec(id: number) {
    this.idRec = id;
  }

  getIdRec() {
    return this.idRec;
  }
}
