import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Conta } from 'src/app/models/conta';
import { ContaService } from 'src/app/services/conta.service';
import { DialogService } from 'src/app/services/dialog.service';

@Component({
  selector: 'app-conta-list',
  templateUrl: './conta-list.component.html',
  styleUrls: ['./conta-list.component.css']
})
export class ContaListComponent implements OnInit {
  allConta: Conta[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private contaService: ContaService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getConta();
  }

  async getConta(){
    this.isLoading = true;

    const data      = await this.contaService.getContas().toPromise();
    this.isLoading  = false;
    this.allConta = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.contaService.deleteConta(id).subscribe(res=>{
          this.getConta();
        })
      }
    })
  }

}
