import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UsuarioCreateComponent } from './components/create/usuario-create/usuario-create.component';
import { HomeComponent } from './components/home/home.component';
import { UsuarioListComponent } from './components/list/usuario-list/usuario-list.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { UsuarioUpdateComponent } from './components/update/usuario-update/usuario-update.component';
import { AuthGuard } from './guards/auth-guard';
import { CategoriaListComponent } from './components/list/categoria-list/categoria-list.component';
import { CategoriaCreateComponent } from './components/create/categoria-create/categoria-create.component';
import { CategoriaUpdateComponent } from './components/update/categoria-update/categoria-update.component';
import { ClienteListComponent } from './components/list/cliente-list/cliente-list.component';
import { ClienteCreateComponent } from './components/create/cliente-create/cliente-create.component';
import { ClienteUpdateComponent } from './components/update/cliente-update/cliente-update.component';
import { ContaListComponent } from './components/list/conta-list/conta-list.component';
import { ContaCreateComponent } from './components/create/conta-create/conta-create.component';
import { ContaUpdateComponent } from './components/update/conta-update/conta-update.component';
import { CpListComponent } from './components/list/cp-list/cp-list.component';
import { CpCreateComponent } from './components/create/cp-create/cp-create.component';
import { CpUpdateComponent } from './components/update/cp-update/cp-update.component';
import { CrListComponent } from './components/list/cr-list/cr-list.component';
import { CrCreateComponent } from './components/create/cr-create/cr-create.component';
import { CrUpdateComponent } from './components/update/cr-update/cr-update.component';
import { FornecedorListComponent } from './components/list/fornecedor-list/fornecedor-list.component';
import { FornecedorCreateComponent } from './components/create/fornecedor-create/fornecedor-create.component';
import { FornecedorUpdateComponent } from './components/update/fornecedor-update/fornecedor-update.component';
import { FtListComponent } from './components/list/ft-list/ft-list.component';
import { FtCreateComponent } from './components/create/ft-create/ft-create.component';
import { FtUpdateComponent } from './components/update/ft-update/ft-update.component';
import { FuncionarioListComponent } from './components/list/funcionario-list/funcionario-list.component';
import { FuncionarioCreateComponent } from './components/create/funcionario-create/funcionario-create.component';
import { FuncionarioUpdateComponent } from './components/update/funcionario-update/funcionario-update.component';
import { FfListComponent } from './components/list/ff-list/ff-list.component';
import { FfCreateComponent } from './components/create/ff-create/ff-create.component';
import { FfUpdateComponent } from './components/update/ff-update/ff-update.component';
import { VtListComponent } from './components/list/vt-list/vt-list.component';
import { VtCreateComponent } from './components/create/vt-create/vt-create.component';
import { VtUpdateComponent } from './components/update/vt-update/vt-update.component';
import { VeiculoListComponent } from './components/list/veiculo-list/veiculo-list.component';
import { VeiculoCreateComponent } from './components/create/veiculo-create/veiculo-create.component';
import { VeiculoUpdateComponent } from './components/update/veiculo-update/veiculo-update.component';
import { OpgListComponent } from './components/list/opg-list/opg-list.component';
import { OpgCreateComponent } from './components/create/opg-create/opg-create.component';
import { OpgUpdateComponent } from './components/update/opg-update/opg-update.component';
import { ProdutoListComponent } from './components/list/produto-list/produto-list.component';
import { ProdutoCreateComponent } from './components/create/produto-create/produto-create.component';
import { ProdutoUpdateComponent } from './components/update/produto-update/produto-update.component';

const routes: Routes = [
  {
    path:'',redirectTo:'login',pathMatch:'full'
  },
  {
    path: 'login', component: LoginComponent
  },
  {
    path: 'signup', component: SignupComponent
  },
  {
  path: 'home', component: HomeComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]
  },

  // Usuario
  { path:'usuario', component:UsuarioListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'usuarioCreate', component: UsuarioCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'usuarioUpdate/:id', component: UsuarioUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Categoria
  { path:'categoria', component:CategoriaListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'categoriaCreate', component: CategoriaCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'categoriaUpdate/:id', component: CategoriaUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Cliente
  { path:'cliente', component:ClienteListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'clienteCreate', component: ClienteCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'clienteUpdate/:id', component: ClienteUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Fornecedor
  { path:'fornecedor', component:FornecedorListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'fornecedorCreate', component: FornecedorCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'fornecedorUpdate/:id', component: FornecedorUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Funcionario Tipo
  { path:'ft', component:FtListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'ftCreate', component: FtCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'ftUpdate/:id', component: FtUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Funcionario Função
  { path:'ff', component:FfListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'ffCreate', component: FfCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'ffUpdate/:id', component: FfUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Funcionario
  { path:'funcionario', component:FuncionarioListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'funcionarioCreate', component: FuncionarioCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'funcionarioUpdate/:id', component: FuncionarioUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Veiculo Tipo
  { path:'vt', component:VtListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'vtCreate', component: VtCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'vtUpdate/:id', component: VtUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Veiculo
  { path:'veiculo', component:VeiculoListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'veiculoCreate', component: VeiculoCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'veiculoUpdate/:id', component: VeiculoUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Conta
  { path:'conta', component:ContaListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'contaCreate', component: ContaCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'contaUpdate/:id', component: FuncionarioUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Opg
  { path:'opg', component:OpgListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'opgCreate', component: OpgCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'opgUpdate/:id', component: OpgUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Conta a Pagar
  { path:'cp', component:CpListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'cpCreate', component: CpCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'cpUpdate/:id', component: CpUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Conta a Receber
  { path:'cr', component:CrListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'crCreate', component: CrCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'crUpdate/:id', component: CrUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},

  // Produto
  { path:'produto', component:ProdutoListComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'produtoCreate', component: ProdutoCreateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
  { path:'produtoUpdate/:id', component: ProdutoUpdateComponent, canActivate: [AuthGuard], canLoad: [AuthGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: []
})
export class AppRoutingModule { }
