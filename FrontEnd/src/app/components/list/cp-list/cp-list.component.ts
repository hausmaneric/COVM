import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Cp } from 'src/app/models/cp';
import { CpService } from 'src/app/services/cp.service';
import { DialogService } from 'src/app/services/dialog.service';
import { IdserviceService } from 'src/app/services/idservice.service';

@Component({
  selector: 'app-cp-list',
  templateUrl: './cp-list.component.html',
  styleUrls: ['./cp-list.component.css']
})
export class CpListComponent implements OnInit {
  allCp: Cp[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;

  constructor(private idService: IdserviceService,private cpService: CpService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getCp();
  }

  async getCp(){
    this.isLoading = true;

    const data      = await this.cpService.getCps().toPromise();
    this.isLoading  = false;
    this.allCp = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.cpService.deleteCp(id).subscribe(res=>{
          this.getCp();
        })
      }
    })
  }

  onPagar(id: number) {
    this.idService.setId(id);
    this.dialogService.openPayDialog().afterClosed().subscribe(res => {
      if (res) {
        this.getCp();
      }
    });
  }
}
