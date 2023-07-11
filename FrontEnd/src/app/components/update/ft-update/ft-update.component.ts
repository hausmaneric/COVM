import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Ft } from 'src/app/models/ft';
import { FtService } from 'src/app/services/ft.service';

@Component({
  selector: 'app-ft-update',
  templateUrl: './ft-update.component.html',
  styleUrls: ['./ft-update.component.css']
})
export class FtUpdateComponent implements OnInit {
  ftForm: Ft = {
    id: 0,
    nome: '',
  }

  isLoading: boolean = false;

  constructor(public dialog: MatDialog, private router: ActivatedRoute, private ftService: FtService, private route: Router) { }

  ngOnInit(): void {
    this.router.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdFt(id);
    })
  }

  getByIdFt(id:number){
    this.ftService.getByIdFt(id).subscribe((data) => {
      this.ftForm = Object.values(data)[0];
    })
  }

  updateFt(){
    this.isLoading = true;
    setTimeout(() => {
      this.ftService.updateFt(this.ftForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.route.navigate(['/ft']);
  }

}
