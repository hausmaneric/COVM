import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Vt } from 'src/app/models/vt';
import { VtService } from 'src/app/services/vt.service';

@Component({
  selector: 'app-vt-create',
  templateUrl: './vt-create.component.html',
  styleUrls: ['./vt-create.component.css']
})
export class VtCreateComponent implements OnInit {
  vtForm: Vt = {
    id: 0,
    nome: '',
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog,private vtService: VtService, private route: Router) { }

  ngOnInit(): void {
  }

  createVt(){
    this.isLoading = true;
    setTimeout(() => {
      this.vtService.createVt(this.vtForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/vt']);
  }

}
