export interface Opg {
  id: number;
  nome: string;
  tipo: number;
  brinde: number;
  taxa: number;
  desconto: number;
  parcelas: number;
  entrada: number;
  com_entrada: boolean;
  av_entrada: boolean;
  av_parcelas: boolean;
  carne: boolean;
  e_boleto: boolean;
  v_dinheiro: boolean;
  v_cheque: boolean;
  v_debito: boolean;
  v_credito: boolean;
  v_financeira: boolean;
  v_pix: boolean;
  a_cartao: boolean;
  a_crediario: boolean;
  a_boleto: boolean;
  a_duplicata: boolean;
}
