import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { jsPDF } from 'jspdf'
import { PDFDocument, StandardFonts, rgb } from 'pdf-lib';
import html2canvas from 'html2canvas';
import { Router } from '@angular/router';
import { Cr } from 'src/app/models/cr';
import { CrService } from 'src/app/services/cr.service';
import { DialogService } from 'src/app/services/dialog.service';
import { IdserviceService } from 'src/app/services/idservice.service';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-cr-list',
  templateUrl: './cr-list.component.html',
  styleUrls: ['./cr-list.component.css']
})
export class CrListComponent implements OnInit {
  allCr: Cr[] | undefined = [];

  @ViewChild('content', {static: false}) el!: ElementRef;
  isLoading: boolean = false;
  pdfUrl: string = '';
  chart: any;

  constructor(private idService: IdserviceService,private crService: CrService, private router: Router, private dialogService: DialogService, private elementRef: ElementRef) { }

  deleteModal: any;
  idToDelete: number = 0;

  ngOnInit(): void {
    this.getCr();
  }

  createChart() {
    if(this.allCr){
      const labels = this.allCr.map(cr => cr.nomecliente);
      const data = this.allCr.map(cr => cr.total);

      const canvas = document.getElementById('myChart') as HTMLCanvasElement; // Faz a assertiva de tipo para HTMLCanvasElement
      const ctx = canvas.getContext('2d');
      if (!ctx) {
        return;
      }

      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Total',
            data: data,
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    }
  }

  drawTable(page: any, table: string[][], settings: any): void {
    const { startX, startY, marginX, marginY, columnWidths } = settings;
    const rowHeight = 20;

    let x = startX;
    let y = startY;

    for (const row of table) {
      for (let i = 0; i < row.length; i++) {
        const text = row[i];
        const width = columnWidths[i];

        page.drawText(text, { x, y, size: 12 });

        x += width + marginX;
      }

      x = startX;
      y -= rowHeight + marginY;
    }
  }

  visualizarPDF(data: string, filename: string): void {
    const blob = new Blob([data], { type: 'application/pdf' });
    const url = URL.createObjectURL(blob);
    window.open(url, '_blank');
  }

  async gerarPDF() {
    const doc = await PDFDocument.create();
    const page = doc.addPage();
    const { width, height } = page.getSize();

    // Defina o conteúdo da tabela
    const table = [];

    // Obtenha a tabela pelo ID
    const tableElement = document.getElementById('report');

    // Obtenha o cabeçalho da tabela
    const headerRow = tableElement!.querySelector('thead tr');

    // Obtenha todas as células do cabeçalho
    const headerCells = headerRow!.querySelectorAll('td');

    // Extrair os valores das células do cabeçalho e adicioná-los à tabela
    const headerData: any = [];
    headerCells.forEach((cell) => {
      cell.style.backgroundColor = 'lightgray';
      headerData.push(cell.textContent);
    });
    table.push(headerData);

    // Obtenha todas as linhas de dados da tabela, excluindo o cabeçalho
    const dataRows = tableElement!.querySelectorAll('tbody tr');

    // Itere sobre as linhas de dados
    dataRows.forEach((row) => {
      const rowData: any = [];

      // Obtenha todas as células da linha
      const cells = row.querySelectorAll('th');

      // Itere sobre as células da linha e adicione os valores ao array rowData
      cells.forEach((cell) => {
        rowData.push(cell.textContent);
      });

      // Adicione a linha ao array table
      table.push(rowData);
    });


    // Defina as configurações da tabela
    const tableSettings = {
      startX: 10,
      startY: height - 50,
      marginX: 60,
      marginY: 5,
      columnWidths: [18, 15, 70, 50, 50, 50],
    };

    // Desenhe a tabela no documento
    this.drawTable(page, table, tableSettings);

    // Salve o arquivo PDF
    const pdfBytes = await doc.save();

    // Faça o download do arquivo PDF
    this.visualizarPDF('relatorio.pdf', 'relatorio.pdf');
  }

  async getCr(){
    this.isLoading = true;

    const data      = await this.crService.getCrs().toPromise();
    this.isLoading  = false;
    this.allCr = data;
  }

  onDelete(id:number){
    this.dialogService.openConfirmDialog().afterClosed().subscribe(res => {
      if(res){
        this.crService.deleteCr(id).subscribe(res=>{
          this.getCr();
        })
      }
    })
  }

  onReceber(id: number) {
    this.idService.setIdRec(id);
    this.dialogService.openRecDialog().afterClosed().subscribe(res => {
      if (res) {
        this.getCr();
      }
    });
  }
}
