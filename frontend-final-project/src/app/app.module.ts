import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './login/login.component';
import { SigninComponent } from './signin/signin.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { RecipeComponent } from './recipe/recipe.component';
import { RecipeBrowseComponent } from './recipe-browse/recipe-browse.component';
import { ProfileComponent } from './profile/profile.component';
import { AboutComponent } from './about/about.component';
import { CommentComponent } from './comment/comment.component';
import { RouterModule, Routes } from '@angular/router';
import { ContactComponent } from './contact/contact.component';
import { MatSelectModule } from '@angular/material/select';
import { AsianRecipesComponent } from './asian-recipes/asian-recipes.component';
import { MeditRecipesComponent } from './medit-recipes/medit-recipes.component';
import { ItalianRecipesComponent } from './italian-recipes/italian-recipes.component';
import { DessertsRecipesComponent } from './desserts-recipes/desserts-recipes.component';
import { OtherRecipesComponent } from './other-recipes/other-recipes.component';
import { AllRecipesComponent } from './all-recipes/all-recipes.component';
import { HomePageComponent } from './home-page/home-page.component';
import { HttpClientModule } from '@angular/common/http';

const appRoute: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'about', component: AboutComponent},
  {path: 'contact', component: ContactComponent},
  {path: 'home', component: HomePageComponent},
  {path: 'category', component: AllRecipesComponent},
  {path: 'browse', component: RecipeBrowseComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'asian-recipe', component: AsianRecipesComponent},
  {path: 'medit-recipe', component: MeditRecipesComponent},
  {path: 'italian-recipe', component: ItalianRecipesComponent},
  {path: 'dessert-recipe', component: DessertsRecipesComponent},
  {path: 'other-recipe', component: OtherRecipesComponent},
  {path: 'login', component: LoginComponent},
  {path: 'signin', component: SigninComponent},
]

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SigninComponent,
    RecipeComponent,
    RecipeBrowseComponent,
    ProfileComponent,
    AboutComponent,
    CommentComponent,
    ContactComponent,
    AsianRecipesComponent,
    MeditRecipesComponent,
    ItalianRecipesComponent,
    DessertsRecipesComponent,
    OtherRecipesComponent,
    AllRecipesComponent,
    HomePageComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatSelectModule,
    FormsModule,
    ReactiveFormsModule,
    MatCardModule,
    MatInputModule,
    HttpClientModule,
    MatButtonModule,
    RouterModule.forRoot(appRoute)

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
