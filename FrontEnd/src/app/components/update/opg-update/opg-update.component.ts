import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Opg } from 'src/app/models/opg';
import { OpgService } from 'src/app/services/opg.service';

@Component({
  selector: 'app-opg-update',
  templateUrl: './opg-update.component.html',
  styleUrls: ['./opg-update.component.css']
})
export class OpgUpdateComponent implements OnInit {
  opgForm: Opg = {
    id: 0,
    nome: '',
    tipo: 0,
    brinde: 0,
    taxa: 0.0,
    desconto: 0.0,
    parcelas: 0,
    entrada: 0.0,
    com_entrada: false,
    av_entrada: false,
    av_parcelas: false,
    carne: false,
    e_boleto: false,
    v_dinheiro: false,
    v_cheque: false,
    v_debito: false,
    v_credito: false,
    v_financeira: false,
    v_pix: false,
    a_cartao: false,
    a_crediario: false,
    a_boleto: false,
    a_duplicata: false
  }

  isLoading: boolean = false;

  mostrarPrazo: Boolean = false;

  constructor(public dialog: MatDialog, private router: ActivatedRoute,private opgService: OpgService, private route: Router) { }

  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdOpg(id);
    })
  }

  getByIdOpg(id:number){
    this.opgService.getByIdOpg(id).subscribe((data) => {
      this.opgForm = Object.values(data)[0];
    })
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }

  updateOpg(){
    this.isLoading = true;
    setTimeout(() => {
      this.opgService.updateOpg(this.opgForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/opg']);
  }

}
