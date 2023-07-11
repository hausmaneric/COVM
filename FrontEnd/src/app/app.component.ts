import { UsuarioService } from './services/usuario.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Project_Prizes';

  mostrarMenu: boolean = false;

  constructor(private loginService: UsuarioService){ }

  ngOnInit(){
   this.loginService.mostrarMenuEmitter.subscribe( mostrar => this.mostrarMenu = mostrar);
  }
}
