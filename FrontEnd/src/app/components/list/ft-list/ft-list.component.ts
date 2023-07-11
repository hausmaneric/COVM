import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Ft } from 'src/app/models/ft';
import { DialogService } from 'src/app/services/dialog.service';
import { FtService } from 'src/app/services/ft.service';

@Component({
  selector: 'app-ft-list',
  templateUrl: './ft-list.component.html',
  styleUrls: ['./ft-list.component.css']
})
export class FtListComponent implements OnInit {
  allFt: Ft[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private ftService: FtService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getFt();
  }

  async getFt(){
    this.isLoading = true;

    const data = await this.ftService.getFts().toPromise();
    this.isLoading = false;
    this.allFt = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.ftService.deleteFt(id).subscribe(res=>{
          this.getFt();
        })
      }
    })
  }
}
