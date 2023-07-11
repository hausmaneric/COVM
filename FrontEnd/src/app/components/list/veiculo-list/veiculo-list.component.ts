import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Veiculo } from 'src/app/models/veiculo';
import { DialogService } from 'src/app/services/dialog.service';
import { VeiculoService } from 'src/app/services/veiculo.service';

@Component({
  selector: 'app-veiculo-list',
  templateUrl: './veiculo-list.component.html',
  styleUrls: ['./veiculo-list.component.css']
})
export class VeiculoListComponent implements OnInit {
  allVeiculo: Veiculo[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private veiculoService: VeiculoService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getVeiculo();
  }

  async getVeiculo(){
    this.isLoading = true;

    const data = await this.veiculoService.getVeiculos().toPromise();
    this.isLoading = false;
    this.allVeiculo = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.veiculoService.deleteVeiculo(id).subscribe(res=>{
          this.getVeiculo();
        })
      }
    })
  }

}
