import { Categoria } from 'src/app/models/categoria';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { CategoriaService } from 'src/app/services/categoria.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-categoria-create',
  templateUrl: './categoria-create.component.html',
  styleUrls: ['./categoria-create.component.css']
})
export class CategoriaCreateComponent implements OnInit {
  categoriaForm: Categoria = {
    id: 0,
    codigo: '',
    nome: '',
    tipo: 0,
    nometipo: ''
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog,private categoriaService: CategoriaService, private route: Router) { }

  ngOnInit(): void {
    this.categoriaService.getLastCategoria().subscribe((lastCategoria: Categoria) => {
      if (lastCategoria) {
        const lastCode = parseInt(Object.values(lastCategoria)[0].codigo);
        const nextCode = (isNaN(lastCode) ? 0 : lastCode) + 1;
        this.categoriaForm.codigo = nextCode.toString().padStart(4, '0');
      } else {
        this.categoriaForm.codigo = '0001';
      }
    });
  }

  getTipo(){
    setTimeout(() => {
      if(this.categoriaForm.tipo == 0){
        this.categoriaForm.nometipo = 'A Pagar';
      }else{
        this.categoriaForm.nometipo = 'A Receber';
      }
    }, 100);
  }

  createCategoria(){
    this.isLoading = true;
    setTimeout(() => {
      this.categoriaService.createCategoria(this.categoriaForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/categoria']);
  }

}
