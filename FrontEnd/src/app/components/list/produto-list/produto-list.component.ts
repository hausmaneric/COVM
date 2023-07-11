import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Produto } from 'src/app/models/produto';
import { DialogService } from 'src/app/services/dialog.service';
import { ProdutoService } from 'src/app/services/produto.service';

@Component({
  selector: 'app-produto-list',
  templateUrl: './produto-list.component.html',
  styleUrls: ['./produto-list.component.css']
})
export class ProdutoListComponent implements OnInit {
  allProduto: Produto[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private produtoService: ProdutoService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getProduto();
  }

  async getProduto(){
    this.isLoading = true;

    const data = await this.produtoService.getProdutos().toPromise();
    this.isLoading = false;
    this.allProduto = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.produtoService.deleteProduto(id).subscribe(res=>{
          this.getProduto();
        })
      }
    })
  }

}
