import { DateAdapter } from '@angular/material/core';
import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Produto } from 'src/app/models/produto';
import { ProdutoService } from 'src/app/services/produto.service';

@Component({
  selector: 'app-produto-update',
  templateUrl: './produto-update.component.html',
  styleUrls: ['./produto-update.component.css']
})
export class ProdutoUpdateComponent implements OnInit {
  produtoForm: Produto = {
    id                   : 0,
    nome                 : '',
    descricao            : '',
    CodigoDeBarras       : '',
    unidade              : '',
    desconto             : 0,
    desconto_maximo      : 0,
    peso                 : 0,
    tamanho              : 0,
    quantidade           : 0,
    entrega              : 0,
    quantidade_minima    : 0,
    preco_compra         : 0,
    margem               : 0,
    preco_venda          : 0,
    margem_1             : 0,
    preco_venda_1        : 0,
    promocao             : 0,
    margem_promocao      : 0,
    preco_venda_promocao : 0,
    atacado              : 0,
    minimo_atacado       : 0,
    margem_atacado       : 0,
    preco_venda_atacado  : 0,
    ultima_venda         : '',
    ultima_compra        : '',
    imagem               : ''
  }

  isLoading: boolean = false;
  valorFinal: number = 0

  constructor(public dialog: MatDialog,private route: ActivatedRoute,private produtoService: ProdutoService, private router: Router, private dateAdapter: DateAdapter<Date>) {
    this.dateAdapter.setLocale('en-GB');
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe((param) => {
      var id = Number(param.get('id'));
      this.getByIdProduto(id);
    })
  }

  compareFn(optionValue: any, selectionValue: any): boolean {
    return optionValue == selectionValue;
  }

  getByIdProduto(id:number){
    this.produtoService.getByIdProduto(id).subscribe((data) => {
      this.produtoForm = Object.values(data)[0];
    })
  }

  getMinimo(event: any){
    this.valorFinal = event.target.value;
  }

  updatePrecoVenda() {
    const precoCompra = this.produtoForm.preco_compra;
    const margem = this.produtoForm.margem;

    // Check if both values are valid numbers
    if (!isNaN(precoCompra) && !isNaN(margem)) {
      const precoVenda = (precoCompra) * (1 + (margem) / 100);
      this.produtoForm.preco_venda = precoVenda;
    } else {
      this.produtoForm.preco_venda = 0;
    }
  }

  updatePrecoVenda1() {
    const precoCompra = this.produtoForm.preco_compra;
    const margem = this.produtoForm.margem_1;

    // Check if both values are valid numbers
    if (!isNaN(precoCompra) && !isNaN(margem)) {
      const precoVenda = (precoCompra) * (1 + (margem) / 100);
      this.produtoForm.preco_venda_1 = precoVenda;
    } else {
      this.produtoForm.preco_venda_1 = 0;
    }
  }

  updatePrecoVendaPromocao() {
    const precoCompra = this.produtoForm.preco_compra;
    const margem = this.produtoForm.margem_promocao;

    // Check if both values are valid numbers
    if (!isNaN(precoCompra) && !isNaN(margem)) {
      const precoVenda = (precoCompra) * (1 + (margem) / 100);
      this.produtoForm.preco_venda_promocao = precoVenda;
    } else {
      this.produtoForm.preco_venda_promocao = 0;
    }
  }

  updatePrecoVendaAtacado() {
    const precoCompra = this.produtoForm.preco_compra;
    const margem = this.produtoForm.margem_atacado;

    // Check if both values are valid numbers
    if (!isNaN(precoCompra) && !isNaN(margem)) {
      const precoVenda = (precoCompra) * (1 + (margem) / 100);
      this.produtoForm.preco_venda_atacado = precoVenda;
    } else {
      this.produtoForm.preco_venda_atacado = 0;
    }
  }

  updateMargem() {
    const precoCompra = this.produtoForm.preco_compra;
    const precoVenda = this.produtoForm.preco_venda;

    // Check if both values are valid numbers
    if (!isNaN(precoCompra) && !isNaN(precoVenda)) {
      const margem = ((precoVenda - precoCompra) / precoCompra) * 100;
      this.produtoForm.margem = margem;
    } else {
      this.produtoForm.margem = 0;
    }
  }

  updateMargem1() {
    const precoCompra = this.produtoForm.preco_compra;
    const precoVenda = this.produtoForm.preco_venda_1;

    // Check if both values are valid numbers
    if (!isNaN(precoCompra) && !isNaN(precoVenda)) {
      const margem = ((precoVenda - precoCompra) / precoCompra) * 100;
      this.produtoForm.margem_1 = margem;
    } else {
      this.produtoForm.margem_1 = 0;
    }
  }

  updateMargemPromocao() {
    const precoCompra = this.produtoForm.preco_compra;
    const precoVenda = this.produtoForm.preco_venda_promocao;

    // Check if both values are valid numbers
    if (!isNaN(precoCompra) && !isNaN(precoVenda)) {
      const margem = ((precoVenda - precoCompra) / precoCompra) * 100;
      this.produtoForm.margem_promocao = margem;
    } else {
      this.produtoForm.margem_promocao = 0;
    }
  }

  updateMargemAtacado() {
    const precoCompra = this.produtoForm.preco_compra;
    const precoVenda = this.produtoForm.preco_venda_atacado;

    if (!isNaN(precoCompra) && !isNaN(precoVenda)) {
      const margem = ((precoVenda - precoCompra) / precoCompra) * 100;
      this.produtoForm.margem_atacado = margem;
    } else {
      this.produtoForm.margem_atacado = 0;
    }
  }

  onInputChange(newValue: number) {
    setTimeout(() => {
      if (newValue > this.produtoForm.quantidade) {
        this.produtoForm.quantidade_minima = this.produtoForm.quantidade - 1; // Define o valor limite no campo de entrada
      }
    }, 100);
  }

  onInputChanges(newValue: number) {
    setTimeout(() => {
      if (newValue > this.produtoForm.quantidade) {
        this.produtoForm.entrega = this.produtoForm.quantidade - 1; // Define o valor limite no campo de entrada
      }
    }, 100);
  }

  updateProduto(){
    this.isLoading = true;
    setTimeout(() => {
      this.produtoService.updateProduto(this.produtoForm).subscribe((data) => {
        this.isLoading = false;
        this.gotoList();
      })
    }, 150);
  }

  gotoList() {
    this.router.navigate(['/produto']);
  }

}
