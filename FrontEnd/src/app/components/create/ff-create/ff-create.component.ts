import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Ff } from 'src/app/models/ff';
import { FfService } from 'src/app/services/ff.service';

@Component({
  selector: 'app-ff-create',
  templateUrl: './ff-create.component.html',
  styleUrls: ['./ff-create.component.css']
})
export class FfCreateComponent implements OnInit {
  ffForm: Ff = {
    id: 0,
    nome: '',
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog,private ffService: FfService, private route: Router) { }

  ngOnInit(): void {
  }

  createFf(){
    this.isLoading = true;
    setTimeout(() => {
      this.ffService.createFf(this.ffForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/ff']);
  }

}
