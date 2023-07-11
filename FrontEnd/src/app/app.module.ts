import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { HomeComponent } from './components/home/home.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import { NgxMaskModule } from 'ngx-mask';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavComponent } from './components/shared/nav/nav.component';
import { HeaderComponent } from './components/shared/header/header.component';
import { FooterComponent } from './components/shared/footer/footer.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatDialogModule} from '@angular/material/dialog';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatListModule} from '@angular/material/list';
import {MatMenuModule} from '@angular/material/menu';
import {MatSelectModule} from '@angular/material/select';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatTableModule} from '@angular/material/table';
import {MatNativeDateModule} from '@angular/material/core';
import {MatPaginatorModule} from '@angular/material/paginator';
import {MatSortModule} from '@angular/material/sort';
import { UsuarioCreateComponent } from './components/create/usuario-create/usuario-create.component';
import { UsuarioUpdateComponent } from './components/update/usuario-update/usuario-update.component';
import { UsuarioListComponent } from './components/list/usuario-list/usuario-list.component';
import { AuthGuard } from './guards/auth-guard';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatStepperModule} from '@angular/material/stepper';
import {MatExpansionModule} from '@angular/material/expansion';
import { MatConfirmDialogComponent } from './components/shared/mat-confirm-dialog/mat-confirm-dialog.component';
import { RichTextEditorModule,ToolbarService, LinkService, ImageService, HtmlEditorService } from "@syncfusion/ej2-angular-richtexteditor";
import { LoadingComponent } from './components/loading/loading.component';
import { CategoriaListComponent } from './components/list/categoria-list/categoria-list.component';
import { CategoriaCreateComponent } from './components/create/categoria-create/categoria-create.component';
import { CategoriaUpdateComponent } from './components/update/categoria-update/categoria-update.component';
import { ClienteListComponent } from './components/list/cliente-list/cliente-list.component';
import { ClienteCreateComponent } from './components/create/cliente-create/cliente-create.component';
import { ClienteUpdateComponent } from './components/update/cliente-update/cliente-update.component';
import {MatTabsModule} from '@angular/material/tabs';
import { ContaListComponent } from './components/list/conta-list/conta-list.component';
import { ContaUpdateComponent } from './components/update/conta-update/conta-update.component';
import { ContaCreateComponent } from './components/create/conta-create/conta-create.component';
import { CpListComponent } from './components/list/cp-list/cp-list.component';
import { CpCreateComponent } from './components/create/cp-create/cp-create.component';
import { CpUpdateComponent } from './components/update/cp-update/cp-update.component';
import { NgxCurrencyModule } from '@sumond25/ngx-currency';
import { MatPagarDialogComponent } from './components/shared/mat-pagar-dialog/mat-pagar-dialog.component';
import { CrListComponent } from './components/list/cr-list/cr-list.component';
import { CrCreateComponent } from './components/create/cr-create/cr-create.component';
import { CrUpdateComponent } from './components/update/cr-update/cr-update.component';
import { MatRecDialogComponent } from './components/shared/mat-rec-dialog/mat-rec-dialog.component';
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
import { FfUpdateComponent } from './components/update/ff-update/ff-update.component';
import { FfCreateComponent } from './components/create/ff-create/ff-create.component';
import { VtListComponent } from './components/list/vt-list/vt-list.component';
import { VtCreateComponent } from './components/create/vt-create/vt-create.component';
import { VtUpdateComponent } from './components/update/vt-update/vt-update.component';
import { VeiculoListComponent } from './components/list/veiculo-list/veiculo-list.component';
import { VeiculoCreateComponent } from './components/create/veiculo-create/veiculo-create.component';
import { VeiculoUpdateComponent } from './components/update/veiculo-update/veiculo-update.component';
import { OpgListComponent } from './components/list/opg-list/opg-list.component';
import { OpgUpdateComponent } from './components/update/opg-update/opg-update.component';
import { OpgCreateComponent } from './components/create/opg-create/opg-create.component';
import { NgxExtendedPdfViewerModule } from 'ngx-extended-pdf-viewer';
import { ProdutoListComponent } from './components/list/produto-list/produto-list.component';
import { ProdutoCreateComponent } from './components/create/produto-create/produto-create.component';
import { ProdutoUpdateComponent } from './components/update/produto-update/produto-update.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    HomeComponent,
    NavComponent,
    HeaderComponent,
    FooterComponent,
    UsuarioCreateComponent,
    UsuarioUpdateComponent,
    UsuarioListComponent,
    MatConfirmDialogComponent,
    MatRecDialogComponent,
    LoadingComponent,
    CategoriaListComponent,
    CategoriaCreateComponent,
    CategoriaUpdateComponent,
    ClienteListComponent,
    ClienteCreateComponent,
    ClienteUpdateComponent,
    ContaListComponent,
    ContaUpdateComponent,
    ContaCreateComponent,
    CpListComponent,
    CpCreateComponent,
    CpUpdateComponent,
    MatPagarDialogComponent,
    CrListComponent,
    CrCreateComponent,
    CrUpdateComponent,
    FornecedorListComponent,
    FornecedorCreateComponent,
    FornecedorUpdateComponent,
    FtListComponent,
    FtCreateComponent,
    FtUpdateComponent,
    FuncionarioListComponent,
    FuncionarioCreateComponent,
    FuncionarioUpdateComponent,
    FfListComponent,
    FfUpdateComponent,
    FfCreateComponent,
    VtListComponent,
    VtCreateComponent,
    VtUpdateComponent,
    VeiculoListComponent,
    VeiculoCreateComponent,
    VeiculoUpdateComponent,
    OpgListComponent,
    OpgUpdateComponent,
    OpgCreateComponent,
    ProdutoListComponent,
    ProdutoCreateComponent,
    ProdutoUpdateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    NgxMaskModule.forRoot({
      dropSpecialCharacters: false
    }),
    BrowserAnimationsModule,
    MatToolbarModule,
    MatCardModule,
    MatButtonModule,
    MatCheckboxModule,
    MatDatepickerModule,
    MatDialogModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatListModule,
    MatMenuModule,
    MatSelectModule,
    MatSidenavModule,
    MatTableModule,
    FormsModule,
    MatNativeDateModule,
    MatPaginatorModule,
    MatSortModule,
    MatSnackBarModule,
    MatStepperModule,
    MatExpansionModule,
    RichTextEditorModule,
    MatTabsModule,
    NgxCurrencyModule,
    NgxExtendedPdfViewerModule
  ],
  providers: [AuthGuard,ToolbarService, LinkService, ImageService, HtmlEditorService],
  bootstrap: [AppComponent],
  entryComponents:[MatConfirmDialogComponent,MatPagarDialogComponent, MatRecDialogComponent]
})
export class AppModule { }
