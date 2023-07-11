import { Component, OnInit } from '@angular/core';
import { Route, Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario';
import { UsuarioService } from 'src/app/services/usuario.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  allUsuario: Usuario[] = [];

  mostrarMenu: boolean = false;

  mostrarSubMenuFuncionarios: boolean = false;
  mostrarSubMenuVeiculos: boolean = false;
  ok: boolean = false;

  nomeUsuario!: string;

  constructor(private route: Router, private loginService: UsuarioService) { }

  ngOnInit(): void {
    window.addEventListener('popstate', this.preventBackNavigation, false);
    if (this.mostrarMenu == true) {
      this.ok = false
    }else{
      this.loginService.mostrarMenuEmitter.subscribe( (mostrar) => {
        this.mostrarMenu = mostrar
        this.ok = true
      })
    }
    this.loginService.mostrarMenuEmitter.subscribe( (mostrar) => {
      this.mostrarMenu = mostrar
      this.ok = true
    });
    this.loginService.mostrarNome.subscribe( mostrar => this.nomeUsuario = mostrar);

    this.getUsuario();
  }

  atualizarSubMenuFuncionarios(): void {
    this.mostrarSubMenuFuncionarios = !this.mostrarSubMenuFuncionarios;
  }

  atualizarSubMenuVeiculos(): void {
    this.mostrarSubMenuVeiculos = !this.mostrarSubMenuVeiculos;
  }

  preventBackNavigation(event:any) {
    // Verifique se o botão "voltar" foi pressionado
    if (event.type === 'popstate') {
      // Restaure a rota atual
      location.reload()
      // Ou você pode redirecionar para uma rota específica
      // this.router.navigate(['block-page']);
    }
  }

  ngOnDestroy() {
    window.removeEventListener('popstate', this.preventBackNavigation, false);
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
