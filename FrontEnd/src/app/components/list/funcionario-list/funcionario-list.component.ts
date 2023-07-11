import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Funcionario } from 'src/app/models/funcionario';
import { DialogService } from 'src/app/services/dialog.service';
import { FuncionarioService } from 'src/app/services/funcionario.service';

@Component({
  selector: 'app-funcionario-list',
  templateUrl: './funcionario-list.component.html',
  styleUrls: ['./funcionario-list.component.css']
})
export class FuncionarioListComponent implements OnInit {
  allFuncionario: Funcionario[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private funcionarioService: FuncionarioService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getFuncionario();
  }

  async getFuncionario(){
    this.isLoading = true;

    const data = await this.funcionarioService.getFuncionarios().toPromise();
    this.isLoading = false;
    this.allFuncionario = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.funcionarioService.deleteFuncionario(id).subscribe(res=>{
          this.getFuncionario();
        })
      }
    })
  }
}
