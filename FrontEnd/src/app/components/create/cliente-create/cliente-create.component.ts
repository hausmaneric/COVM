import { Component, OnInit } from '@angular/core';
import { DateAdapter } from '@angular/material/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Cidade } from 'src/app/models/cidade';
import { Cliente } from 'src/app/models/cliente';
import { Uf } from 'src/app/models/uf';
import { CidadeService } from 'src/app/services/cidade.service';
import { ClienteService } from 'src/app/services/cliente.service';
import { UfService } from 'src/app/services/uf.service';

@Component({
  selector: 'app-cliente-create',
  templateUrl: './cliente-create.component.html',
  styleUrls: ['./cliente-create.component.css']
})
export class ClienteCreateComponent implements OnInit {
  clienteForm: Cliente = {
    id: 0,
    nome: '',
    fantasia: '',
    pessoa: 0,
    endereco: '',
    numero: '',
    complemento: '',
    bairro: '',
    uf: 0,
    cidade: 0,
    cep: '',
    telefone_1: '',
    telefone_2: '',
    email: '',
    cnpj: '',
    cpf: '',
    rg: '',
    data_nascimento: new Date(),
    sexo: 0,
    cadastro: new Date(),
    ultima_compra: new Date(),
    nomeuf: '',
    nomecidade: '',
  }

  uf: Uf[] = [];
  cidade: Cidade[] = [];

  isLoading: boolean = false;
  nomeCidadeSelecionada!: string;
  nomeUFSelecionada!: string;

  constructor(public dialog: MatDialog,private clienteService: ClienteService, private route: Router, private dateAdapter: DateAdapter<Date>, private ufService: UfService, private cidadeService: CidadeService) {
    this.dateAdapter.setLocale('en-GB');
  }

  ngOnInit(): void {
    this.getUf();
  }

  onCidadeSelecionada() {
    const cidadeSelecionada = this.clienteForm.cidade;

    const cidade = this.cidade.find(cidade => cidade.id === cidadeSelecionada);

    if (cidade) {
      this.clienteForm.nomecidade = cidade.nome;
    }
  }

  onUFSelecionada() {
    const nomeUFSelecionada = this.clienteForm.uf;

    const uf = this.uf.find(uf => uf.id === nomeUFSelecionada);

    if (uf) {
      this.clienteForm.nomeuf = uf.nome;
    }
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }

  getUf(){
    this.ufService.getUF().subscribe((data) => {
      this.uf = data;
    })
  }

  getCidade(){
    setTimeout(() => {
      this.cidadeService.getCidade(this.clienteForm.uf).subscribe((data) => {
        this.cidade = data;
      })
    }, 150);
  }

  createCliente(){
    this.isLoading = true;
    setTimeout(() => {
      this.clienteService.createCliente(this.clienteForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/cliente']);
  }
}
