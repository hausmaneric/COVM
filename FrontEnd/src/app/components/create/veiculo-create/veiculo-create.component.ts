import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Veiculo } from 'src/app/models/veiculo';
import { Vt } from 'src/app/models/vt';
import { VeiculoService } from 'src/app/services/veiculo.service';
import { VtService } from 'src/app/services/vt.service';

@Component({
  selector: 'app-veiculo-create',
  templateUrl: './veiculo-create.component.html',
  styleUrls: ['./veiculo-create.component.css']
})
export class VeiculoCreateComponent implements OnInit {
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

  constructor(public dialog: MatDialog, private vtService: VtService,private veiculoService: VeiculoService, private route: Router) { }

  ngOnInit(): void {
    this.getVt();
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

  createVeiculo(){
    this.isLoading = true;
    setTimeout(() => {
      this.veiculoService.createVeiculo(this.veiculoForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/veiculo']);
  }

}
