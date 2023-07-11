import { Component, OnInit } from '@angular/core';
import { DateAdapter } from '@angular/material/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario';
import { UsuarioService } from 'src/app/services/usuario.service';

@Component({
  selector: 'app-usuario-update',
  templateUrl: './usuario-update.component.html',
  styleUrls: ['./usuario-update.component.css']
})
export class UsuarioUpdateComponent implements OnInit {
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
  constructor(private usuarioService: UsuarioService, private router: Router, private route: ActivatedRoute,private dateAdapter: DateAdapter<Date>) {
    this.dateAdapter.setLocale('en-GB');
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdusuario(id);
    })
  }

  getByIdusuario(id:number){
    this.usuarioService.getByIdUsuario(id).subscribe((data) => {
      this.usuarioForm = Object.values(data)[0];
    })
  }

  async updateUsuario(){
    this.isLoading = true;
    this.usuarioForm.senha = btoa(this.usuarioForm.senha);
    const data = await this.usuarioService.updateUsuario(this.usuarioForm).toPromise();
    if(data){
      this.isLoading = false;
      this.router.navigate(['/usuario']);
    }
  }

  gotoList() {
    this.router.navigate(['/usuario']);
  }
}
