import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Categoria } from 'src/app/models/categoria';
import { CategoriaService } from 'src/app/services/categoria.service';

@Component({
  selector: 'app-categoria-update',
  templateUrl: './categoria-update.component.html',
  styleUrls: ['./categoria-update.component.css']
})
export class CategoriaUpdateComponent implements OnInit {
  categoriaForm: Categoria = {
    id: 0,
    codigo: '',
    nome: '',
    tipo: 0,
    nometipo: ''
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog,private route: ActivatedRoute,private categoriaService: CategoriaService, private router: Router) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdCategoria(id);
    })
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }

  getByIdCategoria(id:number){
    this.categoriaService.getByIdCategoria(id).subscribe((data) => {
      this.categoriaForm = Object.values(data)[0];
    })
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

  updateCategoria(){
    this.isLoading = true;
    setTimeout(() => {
      this.categoriaService.updateCategoria(this.categoriaForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.router.navigate(['/categoria']);
  }

}
