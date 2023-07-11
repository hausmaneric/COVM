import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Vt } from 'src/app/models/vt';
import { DialogService } from 'src/app/services/dialog.service';
import { VtService } from 'src/app/services/vt.service';

@Component({
  selector: 'app-vt-list',
  templateUrl: './vt-list.component.html',
  styleUrls: ['./vt-list.component.css']
})
export class VtListComponent implements OnInit {
  allVt: Vt[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private vtService: VtService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getvt();
  }

  async getvt(){
    this.isLoading = true;

    const data = await this.vtService.getVts().toPromise();
    this.isLoading = false;
    this.allVt = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.vtService.deleteVt(id).subscribe(res=>{
          this.getvt();
        })
      }
    })
  }

}
