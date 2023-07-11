import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Conta } from 'src/app/models/conta';
import { ContaService } from 'src/app/services/conta.service';

@Component({
  selector: 'app-conta-update',
  templateUrl: './conta-update.component.html',
  styleUrls: ['./conta-update.component.css']
})
export class ContaUpdateComponent implements OnInit {
  contaForm: Conta = {
    id: 0,
    nome: '',
    agencia:'',
    conta:'',
    banco:'',
    extrato:0
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog,private router: ActivatedRoute,private contaService: ContaService, private route: Router) { }

  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdConta(id);
    })
  }

  getByIdConta(id:number){
    this.contaService.getByIdConta(id).subscribe((data) => {
      this.contaForm = Object.values(data)[0];
    })
  }

  createConta(){
    this.isLoading = true;
    setTimeout(() => {
      this.contaService.updateConta(this.contaForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/conta']);
  }
}
