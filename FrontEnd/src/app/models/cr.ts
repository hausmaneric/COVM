export interface Cr {
  id: number;
  cliente: number;
  tipo: number,
  venda: number;
  documento: string;
  vencimento: string;
  pagamento: string;
  historico: string;
  recebido: boolean;
  negativado: boolean;
  conta: number;
  categoria: number;
  nomeconta: string;
  nomecliente: string;
  nomecategoria: string;
  nometipo: string;
  vencido: number;
  pago: number;
  valor: number;
  juros: number;
  total:number;
}

