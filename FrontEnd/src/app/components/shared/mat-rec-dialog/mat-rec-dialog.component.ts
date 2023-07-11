
import { Component, OnInit, Inject } from '@angular/core';
import {  } from '@angular/material';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Categoria } from 'src/app/models/categoria';
import { Conta } from 'src/app/models/conta';
import { Cr } from 'src/app/models/cr';
import { CategoriaService } from 'src/app/services/categoria.service';
import { ContaService } from 'src/app/services/conta.service';
import { CrService } from 'src/app/services/cr.service';
import { IdserviceService } from 'src/app/services/idservice.service';

@Component({
  selector: 'app-mat-rec-dialog',
  templateUrl: './mat-rec-dialog.component.html',
  styleUrls: ['./mat-rec-dialog.component.css']
})
export class MatRecDialogComponent implements OnInit {
  crForm: Cr = {
    id: 0,
    tipo: 0,
    nometipo: '',
    cliente: 0,
    venda: 0,
    documento: '',
    vencimento: '',
    pagamento: '',
    historico: '',
    recebido: false,
    negativado: false,
    conta: 0,
    categoria: 0,
    nomeconta: '',
    nomecliente: '',
    nomecategoria: '',
    vencido: 0,
    pago: 0,
    valor: 0,
    juros: 0,
    total: 0
  }

  allCategoria: Categoria[] | undefined = [];
  allConta: Conta[] | undefined = [];

  constructor(
    private route: Router,public dialogRef: MatDialogRef<MatRecDialogComponent>,private router: ActivatedRoute, private crService: CrService,private idService: IdserviceService, private contaService: ContaService, private categoriaService: CategoriaService) { }

  ngOnInit() {
    const id = this.idService.getIdRec();
    this.getByIdCr(id);
    this.getCategoria();
    this.getConta();
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }

  updateTotal() {
    const valor = (this.crForm.valor);
    const juros = (this.crForm.juros);
    const total = valor;

    this.crForm.total = total;
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
    const contaSelecionado = this.crForm.conta;

    const conta = this.allConta!.find(conta => conta.id === contaSelecionado);

    if (conta) {
      this.crForm.nomeconta = conta.nome;
    }
  }

  onCategoriaSelecionada() {
    const categoriaSelecionada = this.crForm.categoria;

    const categoria = this.allCategoria!.find(categoria => categoria.id === categoriaSelecionada);

    if (categoria) {
      this.crForm.nomecategoria = categoria.nome;
    }
  }

  getByIdCr(id:number){
    this.crService.getByIdCr(id).subscribe((data) => {
      this.crForm = Object.values(data)[0];
    })
  }

  updateCr(){
    this.crForm.pago = 1;
    this.crService.updateCr(this.crForm).subscribe((data) => {
      this.route.navigate(['/cr']);
    })
  }

  closeDialog() {
    this.dialogRef.close(false);
  }

}
