import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Opg } from 'src/app/models/opg';
import { DialogService } from 'src/app/services/dialog.service';
import { OpgService } from 'src/app/services/opg.service';

@Component({
  selector: 'app-opg-list',
  templateUrl: './opg-list.component.html',
  styleUrls: ['./opg-list.component.css']
})
export class OpgListComponent implements OnInit {
  allOpg: Opg[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private opgService: OpgService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getOpg();
  }

  async getOpg(){
    this.isLoading = true;

    const data = await this.opgService.getOpgs().toPromise();
    this.isLoading = false;
    this.allOpg = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.opgService.deleteOpg(id).subscribe(res=>{
          this.getOpg();
        })
      }
    })
  }
}
