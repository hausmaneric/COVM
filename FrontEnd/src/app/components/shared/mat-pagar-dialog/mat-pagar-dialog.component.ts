
import { Component, OnInit, Inject } from '@angular/core';
import {  } from '@angular/material';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Categoria } from 'src/app/models/categoria';
import { Conta } from 'src/app/models/conta';
import { Cp } from 'src/app/models/cp';
import { CategoriaService } from 'src/app/services/categoria.service';
import { ContaService } from 'src/app/services/conta.service';
import { CpService } from 'src/app/services/cp.service';
import { IdserviceService } from 'src/app/services/idservice.service';

@Component({
  selector: 'app-mat-pagar-dialog',
  templateUrl: './mat-pagar-dialog.component.html',
  styleUrls: ['./mat-pagar-dialog.component.css']
})
export class MatPagarDialogComponent implements OnInit {
  cpForm: Cp = {
    id: 0,
    vencimento: '',
    pagamento: '',
    compra: '',
    documento: '',
    fornecedor: 0,
    historico: '',
    valor: 0.0,
    juros: 0.0,
    total: 0.0,
    categoria: 0,
    nomefornecedor: '',
    nomecategoria: '',
    conta: 0,
    vencido: 0,
    pago: 0,
    nomeconta: ''
  }

  allCategoria: Categoria[] | undefined = [];
  allConta: Conta[] | undefined = [];

  constructor(
    private route: Router,public dialogRef: MatDialogRef<MatPagarDialogComponent>,private router: ActivatedRoute, private cpService: CpService,private idService: IdserviceService, private contaService: ContaService, private categoriaService: CategoriaService) { }

  ngOnInit() {
    const id = this.idService.getId();
    this.getByIdCp(id);
    this.getCategoria();
    this.getConta();
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }

  updateTotal() {
    const valor = (this.cpForm.valor);
    const juros = (this.cpForm.juros);
    const total = valor;

    this.cpForm.total = total;
  }

  async getCategoria(){
    const data      = await this.categoriaService.getCategoria().toPromise();
    this.allCategoria = data;
  }

  async getConta(){
    const data      = await this.contaService.getContas().toPromise();
    this.allConta = data;
  }

  onContaSelecionada() {
    const contaSelecionado = this.cpForm.conta;

    const conta = this.allConta!.find(conta => conta.id === contaSelecionado);

    if (conta) {
      this.cpForm.nomeconta = conta.nome;
    }
  }

  onCategoriaSelecionada() {
    const categoriaSelecionada = this.cpForm.categoria;

    const categoria = this.allCategoria!.find(categoria => categoria.id === categoriaSelecionada);

    if (categoria) {
      this.cpForm.nomecategoria = categoria.nome;
    }
  }

  getByIdCp(id:number){
    this.cpService.getByIdCp(id).subscribe((data) => {
      this.cpForm = Object.values(data)[0];
    })
  }

  updateCp(){
    this.cpForm.pago = 1;
    this.cpService.updateCp(this.cpForm).subscribe((data) => {
      this.route.navigate(['/cp']);
    })
  }

  closeDialog() {
    this.dialogRef.close(false);
  }

}
