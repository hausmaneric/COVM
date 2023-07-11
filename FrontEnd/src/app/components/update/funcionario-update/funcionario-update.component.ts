import { Component, OnInit } from '@angular/core';
import { DateAdapter } from '@angular/material/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Cidade } from 'src/app/models/cidade';
import { Ff } from 'src/app/models/ff';
import { Ft } from 'src/app/models/ft';
import { Funcionario } from 'src/app/models/funcionario';
import { Uf } from 'src/app/models/uf';
import { CidadeService } from 'src/app/services/cidade.service';
import { FfService } from 'src/app/services/ff.service';
import { FtService } from 'src/app/services/ft.service';
import { FuncionarioService } from 'src/app/services/funcionario.service';
import { UfService } from 'src/app/services/uf.service';

@Component({
  selector: 'app-funcionario-update',
  templateUrl: './funcionario-update.component.html',
  styleUrls: ['./funcionario-update.component.css']
})
export class FuncionarioUpdateComponent implements OnInit {
  funcionarioForm: Funcionario = {
    id                  : 0,
    nome                : '',
    identificacao       : '',
    cnpj                : '',
    cpf                 : '',
    rg                  : '',
    endereco            : '',
    numero              : '',
    complemento         : '',
    bairro              : '',
    uf                  : 0,
    cidade              : 0,
    cep                 : '',
    telefone_1          : '',
    telefone_2          : '',
    email               : '',
    salario             : 0,
    m_quadrado          : 0.0,
    diaria              : 0.0,
    mensal              : 0.0,
    data_nascimento     : new Date(),
    admissao            : new Date(),
    funcao              : 0,
    senha               : '',
    comissao_calculo    : 0,
    comissao_produto    : 0.0,
    comissao_servico    : 0.0,
    desconto            : 0.0,
    tipo                : 0,
    nometipo            : '',
    nomefuncao          : '',
    nomeuf              : '',
    nomecidade          : ''
  }

  uf: Uf[] = [];
  cidade: Cidade[] = [];
  allFuncao: Ff[] | undefined = [];
  allTipo: Ft[] | undefined = []

  isLoading: boolean = false;
  nomeCidadeSelecionada!: string;
  nomeUFSelecionada!: string;

  constructor(public dialog: MatDialog, private router: ActivatedRoute, private ffService: FfService, private ftService: FtService,private funcionarioService: FuncionarioService, private route: Router, private dateAdapter: DateAdapter<Date>, private ufService: UfService, private cidadeService: CidadeService) {
    this.dateAdapter.setLocale('en-GB');
  }

  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdFuncionario(id);
    })
    this.getUf();
    this.getFt();
    this.getFf();
    this.getCidade();
  }

  getByIdFuncionario(id:number){
    this.funcionarioService.getByIdFuncionario(id).subscribe((data) => {
      this.funcionarioForm = Object.values(data)[0];
    })
  }

  async getFt(){
    const data = await this.ftService.getFts().toPromise();
    this.allTipo = data
  }

  async getFf(){
    const data = await this.ffService.getFfs().toPromise();
    this.allFuncao = data
  }

  onCidadeSelecionada() {
    const cidadeSelecionada = this.funcionarioForm.cidade;

    const cidade = this.cidade.find(cidade => cidade.id === cidadeSelecionada);

    if (cidade) {
      this.funcionarioForm.nomecidade = cidade.nome;
    }
  }

  onUFSelecionada() {
    const nomeUFSelecionada = this.funcionarioForm.uf;

    const uf = this.uf.find(uf => uf.id === nomeUFSelecionada);

    if (uf) {
      this.funcionarioForm.nomeuf = uf.nome;
    }
  }

  onTipoSelecionada() {
    const nomeTipoSelecionada = this.funcionarioForm.tipo;

    const tipo = this.allTipo!.find(tipo => tipo.id === nomeTipoSelecionada);

    if (tipo) {
      this.funcionarioForm.nometipo = tipo.nome;
    }
  }

  onFuncaoSelecionada() {
    const nomeFuncaoSelecionada = this.funcionarioForm.funcao;

    const funcao = this.allFuncao!.find(funcao => funcao.id === nomeFuncaoSelecionada);

    if (funcao) {
      this.funcionarioForm.nomefuncao = funcao.nome;
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
      this.cidadeService.getCidade(this.funcionarioForm.uf).subscribe((data) => {
        this.cidade = data;
      })
    }, 150);
  }

  updateFuncionario(){
    this.isLoading = true;
    setTimeout(() => {
      this.funcionarioService.updateFuncionario(this.funcionarioForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/funcionario']);
  }

}
