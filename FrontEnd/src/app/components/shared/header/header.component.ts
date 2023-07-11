import { Route, Router } from '@angular/router';
import { LoginComponent } from '../../login/login.component';
import { Usuario } from 'src/app/models/usuario';
import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/services/usuario.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  allUsuario: Usuario[] = [];

  mostrarMenu: boolean = false;
  ok: boolean = false;

  login!: Usuario;

  constructor(private loginService: UsuarioService, private router:Router ) { }

  nomeUsuario!: string;

  ngOnInit(): void {
    this.loginService.mostrarMenuEmitter.subscribe( (mostrar) => {
      this.mostrarMenu = mostrar
      this.ok = true
    });
    this.loginService.mostrarNome.subscribe( mostrar => this.nomeUsuario = mostrar);

    this.getUsuario();
  }

  getUsuario(){
    this.loginService.getUsuario().subscribe((data) =>{
      this.allUsuario = data;
    })
  }

  deslogar(){
    location.reload()

  }
}
