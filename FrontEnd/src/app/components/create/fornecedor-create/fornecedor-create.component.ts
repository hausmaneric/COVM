import { Component, OnInit } from '@angular/core';
import { DateAdapter } from '@angular/material/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Cidade } from 'src/app/models/cidade';
import { Fornecedor } from 'src/app/models/fornecedor';
import { Uf } from 'src/app/models/uf';
import { CidadeService } from 'src/app/services/cidade.service';
import { FornecedorService } from 'src/app/services/fornecedor.service';
import { UfService } from 'src/app/services/uf.service';

@Component({
  selector: 'app-fornecedor-create',
  templateUrl: './fornecedor-create.component.html',
  styleUrls: ['./fornecedor-create.component.css']
})
export class FornecedorCreateComponent implements OnInit {
  fornecedorForm: Fornecedor = {
    id: 0,
    nome: '',
    fantasia: '',
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
    nomeuf: '',
    nomecidade: '',
  }

  uf: Uf[] = [];
  cidade: Cidade[] = [];

  isLoading: boolean = false;
  nomeCidadeSelecionada!: string;
  nomeUFSelecionada!: string;

  constructor(public dialog: MatDialog,private fornecedorService: FornecedorService, private route: Router, private dateAdapter: DateAdapter<Date>, private ufService: UfService, private cidadeService: CidadeService) {
    this.dateAdapter.setLocale('en-GB');
  }

  ngOnInit(): void {
    this.getUf();
  }

  onCidadeSelecionada() {
    const cidadeSelecionada = this.fornecedorForm.cidade;

    const cidade = this.cidade.find(cidade => cidade.id === cidadeSelecionada);

    if (cidade) {
      this.fornecedorForm.nomecidade = cidade.nome;
    }
  }

  onUFSelecionada() {
    const nomeUFSelecionada = this.fornecedorForm.uf;

    const uf = this.uf.find(uf => uf.id === nomeUFSelecionada);

    if (uf) {
      this.fornecedorForm.nomeuf = uf.nome;
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
      this.cidadeService.getCidade(this.fornecedorForm.uf).subscribe((data) => {
        this.cidade = data;
      })
    }, 150);
  }

  createfornecedor(){
    this.isLoading = true;
    setTimeout(() => {
      this.fornecedorService.createFornecedor(this.fornecedorForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/fornecedor']);
  }

}
