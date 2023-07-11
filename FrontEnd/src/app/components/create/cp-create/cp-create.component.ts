import { Component, OnInit } from '@angular/core';
import { DateAdapter } from '@angular/material/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Categoria } from 'src/app/models/categoria';
import { Conta } from 'src/app/models/conta';
import { Cp } from 'src/app/models/cp';
import { Fornecedor } from 'src/app/models/fornecedor';
import { CategoriaService } from 'src/app/services/categoria.service';
import { ContaService } from 'src/app/services/conta.service';
import { CpService } from 'src/app/services/cp.service';
import { FornecedorService } from 'src/app/services/fornecedor.service';

@Component({
  selector: 'app-cp-create',
  templateUrl: './cp-create.component.html',
  styleUrls: ['./cp-create.component.css']
})
export class CpCreateComponent implements OnInit {
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

  isLoading: boolean = false;
  allFornecedor: Fornecedor[] | undefined  = [];
  allCategoria: Categoria[] | undefined = [];
  allConta: Conta[] | undefined = [];

  constructor(public dialog: MatDialog,private cpService: CpService,private categoriaService: CategoriaService, private contaService: ContaService, private fornecedorService: FornecedorService,private route: Router, private dateAdapter: DateAdapter<Date>) {
    this.dateAdapter.setLocale('en-GB');
  }

  updateTotal() {
    const valor = (this.cpForm.valor);
    const juros = (this.cpForm.juros);
    const total = valor;

    this.cpForm.total = total;
  }

  ngOnInit(): void {
    this.getCategoria();
    this.getFornecedor();
    this.getConta();
  }

  async getCategoria(){
    const data      = await this.categoriaService.getCategoria().toPromise();
    this.allCategoria = data;
  }

  async getConta(){
    const data      = await this.contaService.getContas().toPromise();
    this.allConta = data;
  }

  async getFornecedor(){
    const data      = await this.fornecedorService.getFornecedors().toPromise();
    this.allFornecedor = data;
  }

  onFornecedorSelecionada() {
    const fornecedorSelecionado = this.cpForm.fornecedor;

    const fornecedor = this.allFornecedor!.find(fornecedor => fornecedor.id === fornecedorSelecionado);

    if (fornecedor) {
      this.cpForm.nomefornecedor = fornecedor.nome;
    }
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

  createCp(){
    this.isLoading = true;
    setTimeout(() => {
      this.cpService.createCp(this.cpForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/cp']);
  }

}
