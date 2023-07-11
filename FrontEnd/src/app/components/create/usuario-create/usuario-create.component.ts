import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario';
import { UsuarioService } from 'src/app/services/usuario.service';
import * as CryptoJS from 'crypto-js';

@Component({
  selector: 'app-usuario-create',
  templateUrl: './usuario-create.component.html',
  styleUrls: ['./usuario-create.component.css']
})
export class UsuarioCreateComponent implements OnInit {

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
  isLoading: boolean = false;
  elemento!: Usuario;

  constructor(public dialog: MatDialog,private usuarioService: UsuarioService, private route: Router,) {  }

  ngOnInit(): void {
    this.usuarioForm.login = '';
    this.usuarioForm.senha = '';
    this.usuarioForm.nivel = 0;
  }

  openDialog(){
    this.dialog.open(DialogElementsExampleDialog);
  }

  openDialogEmail(){
    this.dialog.open(DialogElementsExampleEmailDialog);
  }

  createUsuario(){
    this.usuarioForm.senha = btoa(this.usuarioForm.senha);
    this.isLoading = true;
    this.usuarioService.getUsuario().subscribe((data) => {
      for (let index = 0; index < Object.values(data).length; index++) {
        const element = Object.values(data)[index];
        this.elemento = element;
      }
      if(this.usuarioForm.email != this.elemento.email){
        if(this.usuarioForm.login != '' && this.usuarioForm.nivel != 0 && this.usuarioForm.senha){
          this.isLoading = false;
          this.usuarioService.createUsuario(this.usuarioForm).subscribe({
            next:(data) => {
              this.route.navigate(['/usuario'])
            },error: (error) =>{
              console.log(error);
            }
          })
        }else{
          this.openDialog();
        }
      }else{
        this.openDialogEmail();
      }
    })

  }

  gotoList() {
    this.route.navigate(['/usuario']);
  }
}

@Component({
  selector: 'usuario-create.component.component',
  templateUrl: 'dialog-elements-example.html',
})
export class DialogElementsExampleDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}

@Component({
  selector: 'usuario-create.component.component',
  templateUrl: 'dialog-elements-exampleEmail.html',
})
export class DialogElementsExampleEmailDialog {
  constructor(public dialog: MatDialog){

  }
  fecharDialog(){
    this.dialog.closeAll();
  }
}
