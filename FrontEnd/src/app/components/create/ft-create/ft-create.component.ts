import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Ft } from 'src/app/models/ft';
import { FtService } from 'src/app/services/ft.service';

@Component({
  selector: 'app-ft-create',
  templateUrl: './ft-create.component.html',
  styleUrls: ['./ft-create.component.css']
})
export class FtCreateComponent implements OnInit {
  ftForm: Ft = {
    id: 0,
    nome: '',
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog,private ftService: FtService, private route: Router) { }

  ngOnInit(): void {
  }

  createFt(){
    this.isLoading = true;
    setTimeout(() => {
      this.ftService.createFt(this.ftForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/ft']);
  }
}
