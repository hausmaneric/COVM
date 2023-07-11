import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Categoria } from 'src/app/models/categoria';
import { CategoriaService } from 'src/app/services/categoria.service';
import { DialogService } from 'src/app/services/dialog.service';

@Component({
  selector: 'app-categoria-list',
  templateUrl: './categoria-list.component.html',
  styleUrls: ['./categoria-list.component.css']
})
export class CategoriaListComponent implements OnInit {
  allCategoria: Categoria[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private categoriaService: CategoriaService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getCategoria();
  }

  async getCategoria(){
    this.isLoading = true;

    const data = await this.categoriaService.getCategoria().toPromise();
    this.isLoading = false;
    this.allCategoria = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.categoriaService.deleteCategoria(id).subscribe(res=>{
          this.getCategoria();
        })
      }
    })
  }

}
