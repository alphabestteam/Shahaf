import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Routes } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { DisplayMoviesComponent } from './display-movies/display-movies.component';
import { RouterModule } from '@angular/router';
import { MovieCardComponentComponent } from './movie-card-component/movie-card-component.component';

const starWarsMovies: Routes = [
  
  {path: 'starWarsMovies', component: DisplayMoviesComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    DisplayMoviesComponent,
    MovieCardComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    RouterModule.forRoot(starWarsMovies)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
