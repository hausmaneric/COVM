import { MatConfirmDialogComponent } from './../components/shared/mat-confirm-dialog/mat-confirm-dialog.component';
import { MatDialog } from '@angular/material/dialog';
import { Injectable } from '@angular/core';
import { MatPagarDialogComponent } from '../components/shared/mat-pagar-dialog/mat-pagar-dialog.component';
import { MatRecDialogComponent } from '../components/shared/mat-rec-dialog/mat-rec-dialog.component';


@Injectable({
  providedIn: 'root'
})
export class DialogService {

  constructor(private dialog: MatDialog) { }

  openConfirmDialog(){
    return this.dialog.open(MatConfirmDialogComponent,{
       width: '390px',
       panelClass: 'confirm-dialog-container',
       disableClose: true,
       position: { top: '10%' },
     });
   }

  openPayDialog() {
    return this.dialog.open(MatPagarDialogComponent, {
      width: '450px',
      panelClass: 'confirm-dialog-container',
      disableClose: true,
      position: { top: '10%' },
    });
  }

  openRecDialog() {
    return this.dialog.open(MatRecDialogComponent, {
      width: '450px',
      panelClass: 'confirm-dialog-container',
      disableClose: true,
      position: { top: '10%' },
    });
  }
}
