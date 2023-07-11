import { EmailService } from './../../services/email.service';
import { Email } from './../../models/email';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder} from '@angular/forms'
import { Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario';
import { UsuarioService } from 'src/app/services/usuario.service';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  usuarioForm: Usuario ={
    id: 0,
    login:'',
    email: '',
    senha:'',
    nivel:0,
    confirmacao: '',
    funcionario: 0,
    nomefuncionario: ''
  }

  emailForm: Email ={
    body: '',
    to: '',
    assunto: ''
  }

  codigo1!: any;
  text!:any;
  text1!:any;

  constructor(public dialog: MatDialog,private emailService: EmailService,private formBuilder: FormBuilder, private http: HttpClient, private router: Router, private usuarioService: UsuarioService) { }

  ngOnInit(): void { }

  openDialog() {
    this.dialog.open(DialogElementsExampleDialog);
  }

  openDialogSignup() {
    this.dialog.open(DialogElementsSignupDialog);
  }

  openDisplay(){
    let element = document.querySelector('.card_ativacao') as HTMLLIElement;
    element.style.display = 'block';
  }

  createUsuario(){
    this.codigo1 = Math.floor(1000 + Math.random() * 9000) ;
    this.usuarioForm.senha = btoa(this.usuarioForm.senha);
    this.usuarioForm.confirmacao = btoa(this.usuarioForm.confirmacao);
    this.emailForm.to = this.usuarioForm.email;
    this.emailForm.assunto = 'Código de Ativação'
    this.emailForm.body  = 'Olá ' + this.usuarioForm.login +', o seu código de ativação é: ' + this.codigo1;

    this.text = this.codigo1;

    if(this.usuarioForm.confirmacao == this.usuarioForm.senha){
      this.emailService.sendEmail(this.emailForm).subscribe((data) =>{
        this.openDisplay();
      })
    }else{
      this.openDialogSignup();
    }
  }

  Confirmar(){
    if(this.text == this.text1){
      this.usuarioForm.nivel = 3;
      this.usuarioService.createUsuario(this.usuarioForm).subscribe({
        next:(data) => {
          this.router.navigate(["login"])
        },error: (error) =>{
          console.log(error);
        }
      })
    }else{
      this.openDialog();
    }
  }

  gotoLogin() {
    this.router.navigate(['/login']);
  }
}

@Component({
  selector: 'signup.component.component',
  templateUrl: 'dialog-elements-example-dialog.html',
})
export class DialogElementsExampleDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}

@Component({
  selector: 'signup.component.component',
  templateUrl: 'dialog-elements-signup.html',
})
export class DialogElementsSignupDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}
