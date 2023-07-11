import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Fornecedor } from 'src/app/models/fornecedor';
import { DialogService } from 'src/app/services/dialog.service';
import { FornecedorService } from 'src/app/services/fornecedor.service';

@Component({
  selector: 'app-fornecedor-list',
  templateUrl: './fornecedor-list.component.html',
  styleUrls: ['./fornecedor-list.component.css']
})
export class FornecedorListComponent implements OnInit {
  allFornecedor: Fornecedor[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private fornecedorService: FornecedorService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getFornecedor();
  }

  async getFornecedor(){
    this.isLoading = true;

    const data      = await this.fornecedorService.getFornecedors().toPromise();
    this.isLoading  = false;
    this.allFornecedor = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.fornecedorService.deleteFornecedor(id).subscribe(res=>{
          this.getFornecedor();
        })
      }
    })
  }

}
