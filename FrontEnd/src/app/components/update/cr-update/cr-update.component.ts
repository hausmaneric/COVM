import { Component, OnInit } from '@angular/core';
import { DateAdapter } from '@angular/material/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Categoria } from 'src/app/models/categoria';
import { Cliente } from 'src/app/models/cliente';
import { Conta } from 'src/app/models/conta';
import { Cr } from 'src/app/models/cr';
import { CategoriaService } from 'src/app/services/categoria.service';
import { ClienteService } from 'src/app/services/cliente.service';
import { ContaService } from 'src/app/services/conta.service';
import { CrService } from 'src/app/services/cr.service';

@Component({
  selector: 'app-cr-update',
  templateUrl: './cr-update.component.html',
  styleUrls: ['./cr-update.component.css']
})
export class CrUpdateComponent implements OnInit {
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

  isLoading: boolean = false;
  allCliente: Cliente[] | undefined  = [];
  allCategoria: Categoria[] | undefined = [];
  allConta: Conta[] | undefined = [];

  constructor(public dialog: MatDialog, private router: ActivatedRoute,private crService: CrService,private categoriaService: CategoriaService, private contaService: ContaService, private clienteService: ClienteService,private route: Router, private dateAdapter: DateAdapter<Date>) {
    this.dateAdapter.setLocale('en-GB');
  }

  updateTotal() {
    const valor = (this.crForm.valor);
    const juros = (this.crForm.juros);
    const total = valor;

    this.crForm.total = total;
  }

  getTipo(){
    setTimeout(() => {
      if(this.crForm.tipo == 0){
        this.crForm.nometipo = 'Cartão';
      }else{
        this.crForm.nometipo = 'Crediário';
      }
    }, 100);
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }


  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdCr(id);
    })
    this.getCliente();
    this.getTipo();
  }

  getByIdCr(id:number){
    this.crService.getByIdCr(id).subscribe((data) => {
      this.crForm = Object.values(data)[0];
    })
  }

  async getCategoria(){
    const data      = await this.categoriaService.getCategoria().toPromise();
    this.allCategoria = data;
  }

  async getConta(){
    const data      = await this.contaService.getContas().toPromise();
    this.allConta = data;
  }

  async getCliente(){
    const data      = await this.clienteService.getClientes().toPromise();
    this.allCliente = data;
  }

  onClienteSelecionada() {
    const ClienteSelecionado = this.crForm.cliente;

    const Cliente = this.allCliente!.find(Cliente => Cliente.id === ClienteSelecionado);

    if (Cliente) {
      this.crForm.nomecliente = Cliente.nome;
    }
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

  updateCr(){
    this.isLoading = true;
    setTimeout(() => {
      this.crService.updateCr(this.crForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/cr']);
  }

}
