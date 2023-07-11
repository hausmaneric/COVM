from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Models.categorias import *
from Models.clientes import *
from Models.contas import *
from Models.contaspagar import *
from Models.contasreceber import *
from Models.contasvalores import *
from Models.email import *
from Models.fornecedores import *
from Models.funcionarios import *
from Models.funcionarios_funcoes import *
from Models.funcionarios_tipo import *
from Models.obras import *
from Models.obrasimage import *
from Models.obrasopg import *
from Models.obrasprodutos import *
from Models.obrasservicos import *
from Models.opcoespagamento import *
from Models.produtos import *
from Models.usuarios import *
from Models.veiculos import *
from Models.veiculos_tipo import *
from Models.vendas import *
from Models.vendasopg import *
from Models.vendasproduto import *

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*", "methods": "GET, POST, PUT, DELETE", "headers":"Origin, Content-Type, X-Auth-Token"}})
app.config['JSON_AS_ASCII'] = False

@app.route('/') 
def main():
    return 'API OK 0.0.1'

#region Categoria 
@app.route('/api/categoria/',     methods = ['GET', 'POST'])
@app.route('/api/categoria/<id>', methods = ['GET', 'PUT', 'DELETE'])
def categoria(id=0):
    categoria  = Categoria()
    if request.method == 'GET':
        if id != 0:
            return getCategoria(id)
        else:
            return getCategorias()
    elif request.method == 'POST': 
        if request.is_json:
            categoria.__dict__.update(request.get_json())          
            return postCategoria(categoria).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            categoria.__dict__.update(request.get_json()) 
            return updateCategoria(id, categoria).__dict__   
    elif request.method == 'DELETE': 
        return deleteCategoria(id)
    
@app.route('/api/categorialast/', methods = ['GET'])   
def categoriaLast():
    if request.method == 'GET':
        return getCategoriaLast()
#endregion
  
#region Cliente 
@app.route('/api/cliente/',     methods = ['GET', 'POST'])
@app.route('/api/cliente/<id>', methods = ['GET', 'PUT', 'DELETE'])
def cliente(id=0):
    cliente  = Clientes()
    if request.method == 'GET':
        if id != 0:
            return getCliente(id)
        else:
            return getClientes()
    elif request.method == 'POST': 
        if request.is_json:
            cliente.__dict__.update(request.get_json())          
            return postCliente(cliente).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            cliente.__dict__.update(request.get_json()) 
            return updateCliente(id, cliente).__dict__   
    elif request.method == 'DELETE': 
        return deleteCliente(id)
#endregion

#region Conta 
@app.route('/api/conta/',     methods = ['GET', 'POST'])
@app.route('/api/conta/<id>', methods = ['GET', 'PUT', 'DELETE'])
def conta(id=0):
    conta  = Contas()
    if request.method == 'GET':
        if id != 0:
            return getConta(id)
        else:
            return getContas()
    elif request.method == 'POST': 
        if request.is_json:
            conta.__dict__.update(request.get_json())          
            return postConta(conta).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            conta.__dict__.update(request.get_json()) 
            return updateConta(id, conta).__dict__   
    elif request.method == 'DELETE': 
        return deleteConta(id)
#endregion

#region Conta a Pagar 
@app.route('/api/cp/',     methods = ['GET', 'POST'])
@app.route('/api/cp/<id>', methods = ['GET', 'PUT', 'DELETE'])
def cp(id=0):
    cp  = ContasPagar()
    if request.method == 'GET':
        if id != 0:
            return getContaPagar(id)
        else:
            return getContasPagar()
    elif request.method == 'POST': 
        if request.is_json:
            cp.__dict__.update(request.get_json())          
            return postContaPagar(cp).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            cp.__dict__.update(request.get_json()) 
            return updateContaPagar(id, cp).__dict__   
    elif request.method == 'DELETE': 
        return deleteContaPagar(id)
#endregion

#region Conta a Receber 
@app.route('/api/cr/',     methods = ['GET', 'POST'])
@app.route('/api/cr/<id>', methods = ['GET', 'PUT', 'DELETE'])
def cr(id=0):
    cr  = ContasReceber()
    if request.method == 'GET':
        if id != 0:
            return getContaReceber(id)
        else:
            return getContasReceber()
    elif request.method == 'POST': 
        if request.is_json:
            cr.__dict__.update(request.get_json())          
            return postContaReceber(cr).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            cr.__dict__.update(request.get_json()) 
            return updateContaReceber(id, cr).__dict__   
    elif request.method == 'DELETE': 
        return deleteContaReceber(id)
#endregion

#region Conta Valor
@app.route('/api/cv/',     methods = ['GET', 'POST'])
@app.route('/api/cv/<id>', methods = ['GET', 'PUT', 'DELETE'])
def cv(id=0):
    cv  = Contas_Valores()
    if request.method == 'GET':
        if id != 0:
            return getContas_Valor(id)
        else:
            return getContas_Valores()
    elif request.method == 'POST': 
        if request.is_json:
            cv.__dict__.update(request.get_json())          
            return postContas_Valor(cv).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            cv.__dict__.update(request.get_json()) 
            return updateContas_Valor(id, cv).__dict__   
    elif request.method == 'DELETE': 
        return deleteContas_Valor(id)
#endregion

#region Fornecedor
@app.route('/api/fornecedor/',     methods = ['GET', 'POST'])
@app.route('/api/fornecedor/<id>', methods = ['GET', 'PUT', 'DELETE'])
def fornecedor(id=0):
    fornecedor  = Fornecedores()
    if request.method == 'GET':
        if id != 0:
            return getFornecedor(id)
        else:
            return getFornecedores()
    elif request.method == 'POST': 
        if request.is_json:
            fornecedor.__dict__.update(request.get_json())          
            return postFornecedor(fornecedor).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            fornecedor.__dict__.update(request.get_json()) 
            return updateFornecedor(id, fornecedor).__dict__   
    elif request.method == 'DELETE': 
        return deleteFornecedor(id)
#endregion

#region Funcionario Tipo
@app.route('/api/ft/',     methods = ['GET', 'POST'])
@app.route('/api/ft/<id>', methods = ['GET', 'PUT', 'DELETE'])
def ft(id=0):
    ft  = FuncionarioTipo()
    if request.method == 'GET':
        if id != 0:
            return getFuncionarioTipo(id)
        else:
            return getFuncionarioTipoList()
    elif request.method == 'POST': 
        if request.is_json:
            ft.__dict__.update(request.get_json())          
            return postFuncionarioTipo(ft).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            ft.__dict__.update(request.get_json()) 
            return updateFuncionarioTipo(id, ft).__dict__   
    elif request.method == 'DELETE': 
        return deleteFuncionarioTipo(id)
#endregion

#region Funcionario Funcao
@app.route('/api/ff/',     methods = ['GET', 'POST'])
@app.route('/api/ff/<id>', methods = ['GET', 'PUT', 'DELETE'])
def ff(id=0):
    ff  = FuncionarioFuncao()
    if request.method == 'GET':
        if id != 0:
            return getFuncionarioFuncao(id)
        else:
            return getFuncionarioFuncaoList()
    elif request.method == 'POST': 
        if request.is_json:
            ff.__dict__.update(request.get_json())          
            return postFuncionarioFuncao(ff).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            ff.__dict__.update(request.get_json()) 
            return updateFuncionarioFuncao(id, ff).__dict__   
    elif request.method == 'DELETE': 
        return deleteFuncionarioFuncao(id)
#endregion

#region Funcionario
@app.route('/api/funcionario/',     methods = ['GET', 'POST'])
@app.route('/api/funcionario/<id>', methods = ['GET', 'PUT', 'DELETE'])
def funcionario(id=0):
    funcionario  = Funcionarios()
    if request.method == 'GET':
        if id != 0:
            return getFuncionario(id)
        else:
            return getFuncionarios()
    elif request.method == 'POST': 
        if request.is_json:
            funcionario.__dict__.update(request.get_json())          
            return postFuncionario(funcionario).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            funcionario.__dict__.update(request.get_json()) 
            return updateFuncionario(id, funcionario).__dict__   
    elif request.method == 'DELETE': 
        return deleteFuncionario(id)
#endregion

#region Obra
@app.route('/api/obra/',     methods = ['GET', 'POST'])
@app.route('/api/obra/<id>', methods = ['GET', 'PUT', 'DELETE'])
def obra(id=0):
    obra  = Obras()
    if request.method == 'GET':
        if id != 0:
            return getObra(id)
        else:
            return getObras()
    elif request.method == 'POST': 
        if request.is_json:
            obra.__dict__.update(request.get_json())          
            return postObra(obra).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            obra.__dict__.update(request.get_json()) 
            return updateObra(id, obra).__dict__   
    elif request.method == 'DELETE': 
        return deleteObra(id)
#endregion

#region Obra Imagem
@app.route('/api/oi/',     methods = ['GET', 'POST'])
@app.route('/api/oi/<id>', methods = ['GET', 'PUT', 'DELETE'])
def oi(id=0):
    oi  = Obras_Imagem()
    if request.method == 'GET':
        if id != 0:
            return getObra_Imagem(id)
        else:
            return getObras_Imagem()
    elif request.method == 'POST': 
        if request.is_json:
            oi.__dict__.update(request.get_json())          
            return postObra_Imagem(oi).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            oi.__dict__.update(request.get_json()) 
            return updateObra_Imagem(id, oi).__dict__   
    elif request.method == 'DELETE': 
        return deleteObra_Imagem(id)
#endregion

#region Obra Produto
@app.route('/api/op/',     methods = ['GET', 'POST'])
@app.route('/api/op/<id>', methods = ['GET', 'PUT', 'DELETE'])
def op(id=0):
    op  = Obras_Produtos()
    if request.method == 'GET':
        if id != 0:
            return getObraProduto(id)
        else:
            return getObrasProdutos()
    elif request.method == 'POST': 
        if request.is_json:
            op.__dict__.update(request.get_json())          
            return postObraProduto(op).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            op.__dict__.update(request.get_json()) 
            return updateObraProduto(id, op).__dict__   
    elif request.method == 'DELETE': 
        return deleteObraProduto(id)
#endregion

#region Obra Servico
@app.route('/api/os/',     methods = ['GET', 'POST'])
@app.route('/api/os/<id>', methods = ['GET', 'PUT', 'DELETE'])
def os(id=0):
    os  = Obras_Servicos()
    if request.method == 'GET':
        if id != 0:
            return getObraServicos(id)
        else:
            return getObrasServicos()
    elif request.method == 'POST': 
        if request.is_json:
            os.__dict__.update(request.get_json())          
            return postObraServicos(os).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            os.__dict__.update(request.get_json()) 
            return updateObraServicos(id, os).__dict__   
    elif request.method == 'DELETE': 
        return deleteObraServicos(id)
#endregion

#region Obra OPG
@app.route('/api/oopg/',     methods = ['GET', 'POST'])
@app.route('/api/oopg/<id>', methods = ['GET', 'PUT', 'DELETE'])
def oopg(id=0):
    oopg  = Obras_Opg()
    if request.method == 'GET':
        if id != 0:
            return getObra_Opg(id)
        else:
            return getObras_Opg()
    elif request.method == 'POST': 
        if request.is_json:
            oopg.__dict__.update(request.get_json())          
            return postObra_Opg(oopg).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            oopg.__dict__.update(request.get_json()) 
            return updateObra_Opg(id, oopg).__dict__   
    elif request.method == 'DELETE': 
        return deleteObra_Opg(id)
#endregion

#region Opção de Pagamento
@app.route('/api/opg/',     methods = ['GET', 'POST'])
@app.route('/api/opg/<id>', methods = ['GET', 'PUT', 'DELETE'])
def opg(id=0):
    opg  = OpcaoPagamento()
    if request.method == 'GET':
        if id != 0:
            return getOpcaoPagamento(id)
        else:
            return getOpcoesPagamento()
    elif request.method == 'POST': 
        if request.is_json:
            opg.__dict__.update(request.get_json())          
            return postOpcaoPagamento(opg).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            opg.__dict__.update(request.get_json()) 
            return updateOpcaoPagamento(id, opg).__dict__   
    elif request.method == 'DELETE': 
        return deleteOpcaoPagamento(id)
#endregion

#region Produto
@app.route('/api/produto/',     methods = ['GET', 'POST'])
@app.route('/api/produto/<id>', methods = ['GET', 'PUT', 'DELETE'])
def produto(id=0):
    produto  = Produtos()
    if request.method == 'GET':
        if id != 0:
            return getProduto(id)
        else:
            return getProdutos()
    elif request.method == 'POST': 
        if request.is_json:
            produto.__dict__.update(request.get_json())          
            return postProduto(produto).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            produto.__dict__.update(request.get_json()) 
            return updateProduto(id, produto).__dict__   
    elif request.method == 'DELETE': 
        return deleteProduto(id)
#endregion

#region Usuario
@app.route('/api/usuario/',     methods = ['GET', 'POST'])
@app.route('/api/usuario/<id>', methods = ['GET', 'PUT', 'DELETE'])
def usuario(id=0):
    usuario  = Usuarios()
    if request.method == 'GET':
        if id != 0:
            return getUsuario(id)
        else:
            return getUsuarios()
    elif request.method == 'POST': 
        if request.is_json:
            usuario.__dict__.update(request.get_json())          
            return postUsuario(usuario).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            usuario.__dict__.update(request.get_json()) 
            return updateUsuario(id, usuario).__dict__   
    elif request.method == 'DELETE': 
        return deleteUsuario(id)
#endregion

#region Veiculo Tipo
@app.route('/api/vt/',     methods = ['GET', 'POST'])
@app.route('/api/vt/<id>', methods = ['GET', 'PUT', 'DELETE'])
def vt(id=0):
    vt  = VeiculosTipo()
    if request.method == 'GET':
        if id != 0:
            return getVeiculosTipo(id)
        else:
            return getVeiculosTipoList()
    elif request.method == 'POST': 
        if request.is_json:
            vt.__dict__.update(request.get_json())          
            return postVeiculoTipo(vt).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            vt.__dict__.update(request.get_json()) 
            return updateVeiculoTipo(id, vt).__dict__   
    elif request.method == 'DELETE': 
        return deleteVeiculoTipo(id)
#endregion

#region Veiculo
@app.route('/api/veiculo/',     methods = ['GET', 'POST'])
@app.route('/api/veiculo/<id>', methods = ['GET', 'PUT', 'DELETE'])
def veiculo(id=0):
    veiculo  = Veiculos()
    if request.method == 'GET':
        if id != 0:
            return getVeiculo(id)
        else:
            return getVeiculosList()
    elif request.method == 'POST': 
        if request.is_json:
            veiculo.__dict__.update(request.get_json())          
            return postVeiculo(veiculo).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            veiculo.__dict__.update(request.get_json()) 
            return updateVeiculo(id, veiculo).__dict__   
    elif request.method == 'DELETE': 
        return deleteVeiculo(id)
#endregion

#region Venda
@app.route('/api/venda/',     methods = ['GET', 'POST'])
@app.route('/api/venda/<id>', methods = ['GET', 'PUT', 'DELETE'])
def venda(id=0):
    venda  = Vendas()
    if request.method == 'GET':
        if id != 0:
            return getVenda(id)
        else:
            return getVendas()
    elif request.method == 'POST': 
        if request.is_json:
            venda.__dict__.update(request.get_json())          
            return postVenda(venda).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            venda.__dict__.update(request.get_json()) 
            return updateVenda(id, venda).__dict__   
    elif request.method == 'DELETE': 
        return deleteVenda(id)
#endregion

#region Venda Opg
@app.route('/api/vopg/',     methods = ['GET', 'POST'])
@app.route('/api/vopg/<id>', methods = ['GET', 'PUT', 'DELETE'])
def vopg(id=0):
    vopg  = Vendas_Opg()
    if request.method == 'GET':
        if id != 0:
            return getVendaOpg(id)
        else:
            return getVendasOpg()
    elif request.method == 'POST': 
        if request.is_json:
            vopg.__dict__.update(request.get_json())          
            return postVendaOpg(vopg).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            vopg.__dict__.update(request.get_json()) 
            return updateVendaOpg(id, vopg).__dict__   
    elif request.method == 'DELETE': 
        return deleteVendaOpg(id)
#endregion

#region Venda Produto
@app.route('/api/vp/',     methods = ['GET', 'POST'])
@app.route('/api/vp/<id>', methods = ['GET', 'PUT', 'DELETE'])
def vp(id=0):
    vp  = Vendas_Produtos()
    if request.method == 'GET':
        if id != 0:
            return getVendaProduto(id)
        else:
            return getVendasProdutos()
    elif request.method == 'POST': 
        if request.is_json:
            vp.__dict__.update(request.get_json())          
            return postVendaProduto(vp).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            vp.__dict__.update(request.get_json()) 
            return updateVendaProduto(id, vp).__dict__   
    elif request.method == 'DELETE': 
        return deleteVendaProduto(id)
#endregion

#region Email
@app.route('/api/email/', methods = ['GET', 'POST'])
def email():
    email = Email()
    email.__dict__.update(request.get_json())    
    return sendEmail(email)
#endregion

if __name__ == '__main__':
  app.run(host="0.0.0.0")