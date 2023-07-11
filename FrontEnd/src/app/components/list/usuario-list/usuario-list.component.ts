import { ElementRef,ViewChild,Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario';
import { DialogService } from 'src/app/services/dialog.service';
import { UsuarioService } from 'src/app/services/usuario.service';
import { jsPDF } from 'jspdf';

declare var window: any;

@Component({
  selector: 'app-usuario-list',
  templateUrl: './usuario-list.component.html',
  styleUrls: ['./usuario-list.component.css']
})
export class UsuarioListComponent implements OnInit {
  allUsuario: Usuario[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private usuarioService: UsuarioService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getUsuario();
  }

  async getUsuario(){
    this.isLoading = true;

    const data = await this.usuarioService.getUsuario().toPromise();
    this.isLoading = false;
    this.allUsuario = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.usuarioService.deleteUsuario(id).subscribe(res=>{
          this.getUsuario();
        })
      }
    })
  }

  printSimplePDF(){
    let pdf = new jsPDF('p', 'pt', 'a4');
    pdf.html(this.el.nativeElement,{
      callback: (pdf) => {
        pdf.save("testPDFHTMl.pdf");
      }
    })
  }

}
