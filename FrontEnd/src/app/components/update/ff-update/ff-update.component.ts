import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Ff } from 'src/app/models/ff';
import { FfService } from 'src/app/services/ff.service';

@Component({
  selector: 'app-ff-update',
  templateUrl: './ff-update.component.html',
  styleUrls: ['./ff-update.component.css']
})
export class FfUpdateComponent implements OnInit {
  ffForm: Ff = {
    id: 0,
    nome: '',
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog, private router: ActivatedRoute, private ffService: FfService, private route: Router) { }

  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdFf(id);
    })
  }

  getByIdFf(id:number){
    this.ffService.getByIdFf(id).subscribe((data) => {
      this.ffForm = Object.values(data)[0];
    })
  }

  updateFf(){
    this.isLoading = true;
    setTimeout(() => {
      this.ffService.updateFf(this.ffForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/ff']);
  }

}
