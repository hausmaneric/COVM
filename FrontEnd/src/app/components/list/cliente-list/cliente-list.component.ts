import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Cliente } from 'src/app/models/cliente';
import { ClienteService } from 'src/app/services/cliente.service';
import { DialogService } from 'src/app/services/dialog.service';

@Component({
  selector: 'app-cliente-list',
  templateUrl: './cliente-list.component.html',
  styleUrls: ['./cliente-list.component.css']
})
export class ClienteListComponent implements OnInit {
  allCliente: Cliente[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private clienteService: ClienteService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getCliente();
  }

  async getCliente(){
    this.isLoading = true;

    const data      = await this.clienteService.getClientes().toPromise();
    this.isLoading  = false;
    this.allCliente = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.clienteService.deleteCliente(id).subscribe(res=>{
          this.getCliente();
        })
      }
    })
  }

}
