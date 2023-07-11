import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Email } from '../models/email';

@Injectable({
  providedIn: 'root'
})
export class EmailService {


  constructor(private http:HttpClient) { }

  sendEmail(payLoad:Email){
    return this.http.post<Email>("http://16.16.77.152/api1/email/", payLoad);
  }
}
