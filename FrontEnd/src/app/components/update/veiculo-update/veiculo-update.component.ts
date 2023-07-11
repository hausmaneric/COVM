import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Veiculo } from 'src/app/models/veiculo';
import { Vt } from 'src/app/models/vt';
import { VeiculoService } from 'src/app/services/veiculo.service';
import { VtService } from 'src/app/services/vt.service';

@Component({
  selector: 'app-veiculo-update',
  templateUrl: './veiculo-update.component.html',
  styleUrls: ['./veiculo-update.component.css']
})
export class VeiculoUpdateComponent implements OnInit {
  veiculoForm: Veiculo = {
    id         : 0,
    tipo       : 0,
    nome       : "",
    placa      : "",
    cor        : "",
    situacao   : 0,
    modelo     : "",
    nometipo   : '',
  }

  isLoading: boolean = false;
  allVt: Vt[] | undefined = [];

  constructor(public dialog: MatDialog, private router: ActivatedRoute, private vtService: VtService,private veiculoService: VeiculoService, private route: Router) { }

  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdveiculo(id);
    })
    this.getVt();
  }

  getByIdveiculo(id:number){
    this.veiculoService.getByIdVeiculo(id).subscribe((data) => {
      this.veiculoForm = Object.values(data)[0];
    })
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }

  converterParaMaiusculas(): void {
    this.veiculoForm.placa = this.veiculoForm.placa.toUpperCase();
  }

  onTipoSelecionada() {
    const tipoSelecionado = this.veiculoForm.tipo;

    const tipo = this.allVt!.find(tipo => tipo.id === tipoSelecionado);

    if (tipo) {
      this.veiculoForm.nometipo = tipo.nome;
    }
  }

  async getVt(){
    const data = await this.vtService.getVts().toPromise()
    this.allVt = data
  }

  updateVeiculo(){
    this.isLoading = true;
    setTimeout(() => {
      this.veiculoService.updateVeiculo(this.veiculoForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/veiculo']);
  }

}
