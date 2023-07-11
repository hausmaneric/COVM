export interface Cliente {
  id: number;
  nome: string;
  fantasia: string;
  pessoa: number;
  endereco: string;
  numero: string;
  complemento: string;
  bairro: string;
  uf: number;
  cidade: number;
  cep: string;
  telefone_1: string;
  telefone_2: string;
  email: string;
  cnpj: string;
  cpf: string;
  rg: string;
  data_nascimento: Date | string;
  sexo: number;
  cadastro: Date | string ;
  ultima_compra: Date | string;
  nomeuf: string;
  nomecidade: string;
}
