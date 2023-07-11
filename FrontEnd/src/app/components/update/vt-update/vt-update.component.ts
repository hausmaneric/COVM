import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Vt } from 'src/app/models/vt';
import { VtService } from 'src/app/services/vt.service';

@Component({
  selector: 'app-vt-update',
  templateUrl: './vt-update.component.html',
  styleUrls: ['./vt-update.component.css']
})
export class VtUpdateComponent implements OnInit {
  vtForm: Vt = {
    id: 0,
    nome: '',
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog, private router: ActivatedRoute, private vtService: VtService, private route: Router) { }

  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdVt(id);
    })
  }

  getByIdVt(id:number){
    this.vtService.getByIdVt(id).subscribe((data) => {
      this.vtForm = Object.values(data)[0];
    })
  }

  updateVt(){
    this.isLoading = true;
    setTimeout(() => {
      this.vtService.updateVt(this.vtForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/vt']);
  }

}
