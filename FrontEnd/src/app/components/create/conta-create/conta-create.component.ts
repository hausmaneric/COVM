import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Conta } from 'src/app/models/conta';
import { ContaService } from 'src/app/services/conta.service';

@Component({
  selector: 'app-conta-create',
  templateUrl: './conta-create.component.html',
  styleUrls: ['./conta-create.component.css']
})
export class ContaCreateComponent implements OnInit {
  contaForm: Conta = {
    id: 0,
    nome: '',
    agencia:'',
    conta:'',
    banco:'',
    extrato:0
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog,private contaService: ContaService, private route: Router) { }

  ngOnInit(): void {
  }

  createConta(){
    this.isLoading = true;
    setTimeout(() => {
      this.contaService.createConta(this.contaForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/conta']);
  }

}
