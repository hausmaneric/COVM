import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { Ff } from 'src/app/models/ff';
import { DialogService } from 'src/app/services/dialog.service';
import { FfService } from 'src/app/services/ff.service';

@Component({
  selector: 'app-ff-list',
  templateUrl: './ff-list.component.html',
  styleUrls: ['./ff-list.component.css']
})
export class FfListComponent implements OnInit {
  allFf: Ff[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  constructor(private ffService: FfService, private router: Router, private dialogService: DialogService) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getFf();
  }

  async getFf(){
    this.isLoading = true;

    const data = await this.ffService.getFfs().toPromise();
    this.isLoading = false;
    this.allFf = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.ffService.deleteFf(id).subscribe(res=>{
          this.getFf();
        })
      }
    })
  }

}
