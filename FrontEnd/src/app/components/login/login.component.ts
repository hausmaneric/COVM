import { Component, OnInit } from '@angular/core';
import {FormGroup} from '@angular/forms'
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario';
import { UsuarioService } from 'src/app/services/usuario.service';
import { EmailService } from './../../services/email.service';
import { Email } from './../../models/email';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  emailForm: Email ={
    body: '',
    to: '',
    assunto: ''
  }

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

  mostrarMenu: boolean = false;
  codigo1!: any;
  text!:any;
  cod_rec!:any;
  email!:string;
  isLoading: boolean = false;

  public loginForm: Usuario[] = []

  constructor( private route: ActivatedRoute,private emailService: EmailService,public dialog: MatDialog, private router: Router, private usuarioService: UsuarioService) {  }

  ngOnInit(): void {
    let element = document.querySelector('.cad') as HTMLLIElement;
    this.usuarioService.getUsuario().subscribe((data) =>{
      if(data.length == 0){
        element.style.display = 'block';
      }else{
        element.style.display = 'none';
      }
    })
  }

  openDialog() {
    this.dialog.open(DialogElementsExampleDialog);
  }

  openDialogLogin() {
    this.dialog.open(DialogElementsLoginDialog);
  }

  openDialogLoginEmailNC() {
    this.dialog.open(DialogElementsEmailNCDialog);
  }

  openDialogLoginSenha() {
    this.dialog.open(DialogElementsSenhaDialog);
  }

  openDialogLoginCodigo() {
    this.dialog.open(DialogElementsCodigoDialog);
  }

  openDisplay(){
    let element = document.querySelector('.card_rec') as HTMLLIElement;
    element.style.display = 'none';

    let element_1 = document.querySelector('.card_rec_cod') as HTMLLIElement;
    element_1.style.display = 'block';
  }

  openDisplayPsw(){
    let element = document.querySelector('.card_rec_psw') as HTMLLIElement;
    element.style.display = 'block';

    let element_1 = document.querySelector('.card_rec_cod') as HTMLLIElement;
    element_1.style.display = 'none';

    this.usuarioService.getEmail(this.email).subscribe((data) =>{
      this.usuarioService.getByIdUsuario(Object.values(data)[0].id).subscribe((data) => {
        this.usuarioForm = Object.values(data)[0];
      })
    })

    this.usuarioForm.senha = '';
    this.usuarioForm.confirmacao = '';
  }

  login(){
    this.isLoading = true;
    this.usuarioForm.senha = btoa(this.usuarioForm.senha)
    this.usuarioService.getUsuario().subscribe(res=>{
      const user = res.find((a: any) =>{
          return a.login === this.usuarioForm.login && a.senha === this.usuarioForm.senha
      });
      if(this.usuarioForm.login =='' || this.usuarioForm.senha == ''){
        this.openDialogLogin()
      }
      else if(user){
        this.isLoading = false;
        this.usuarioService.Autenticado = true;
        this.usuarioService.mostrarMenuEmitter.emit(true);
        this.usuarioService.mostrarMenuEmitterFalse.emit(false);
        this.usuarioService.nome = user.login;
        this.usuarioService.mostrarNome.emit(this.usuarioService.nome);
        // this.mostrarImg.emit(user.image)
        // alert(this.nome)
        this.router.navigate(['home']);
      }else{
        this.openDialog()
        this.usuarioService.mostrarMenuEmitter.emit(false);
      }
    },error=>{
      alert("Somethin went wrong");
    })
  };


  recDisplay(){
    let element = document.querySelector('.card_rec') as HTMLLIElement;
    element.style.display = 'block';
  }

  enviarEmail(){
    this.codigo1 = Math.floor(1000 + Math.random() * 9000);
    this.isLoading = true;
    this.usuarioService.getUsuario().subscribe((data)=>{
      for (let index = 0; index < Object.values(data).length; index++) {
        const element = Object.values(data)[index];
        if(this.emailForm.to == element.email){
          this.emailForm.assunto = 'Código de Recuperação'
          this.emailForm.body  = 'Olá, o seu código de recuperação é: ' + this.codigo1;

          this.text = this.codigo1;

          this.email = this.emailForm.to;

          if(this.emailForm.to == ''){
            console.log('Vazio')
          }else if(this.emailForm.to != element.login){
            this.isLoading = false;
            this.openDialogLoginEmailNC();
          }
          else{
            this.emailService.sendEmail(this.emailForm).subscribe((data) =>{
              this.openDisplay();
            })
          }
        }
      }
    })
  }

  Recuperar(){
    if(this.text == this.cod_rec){
      this.openDisplayPsw();
    }else{
      this.openDialogLoginCodigo();
    }
  }

  RecuperarPsw(){
    if(this.usuarioForm.senha != this.usuarioForm.confirmacao){
      this.openDialogLoginSenha();
    }else{
      this.usuarioForm.senha = btoa(this.usuarioForm.senha)
      this.usuarioService.updateUsuario(this.usuarioForm).subscribe({
        next:(data) => {
          location.reload()
        },error:(error)=>{
          console.log(error);
        }
      })
    }
  }

}

@Component({
  selector: 'login.component.component',
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
  selector: 'login.component.component',
  templateUrl: 'dialog-elements-login.html',
})
export class DialogElementsLoginDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}

@Component({
  selector: 'login.component.component',
  templateUrl: 'dialog-elements-example-email-nc.html',
})
export class DialogElementsEmailNCDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}

@Component({
  selector: 'login.component.component',
  templateUrl: 'dialog-elements-example-senha.html',
})
export class DialogElementsSenhaDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}

@Component({
  selector: 'login.component.component',
  templateUrl: 'dialog-elements-codigo.html',
})
export class DialogElementsCodigoDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}


