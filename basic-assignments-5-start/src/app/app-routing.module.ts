import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DisplayMoviesComponent } from './display-movies/display-movies.component';

const starWarsMovies: Routes = [
  {path: 'starWarsMovies', component: DisplayMoviesComponent}
]

@NgModule({
  imports: [RouterModule.forRoot(starWarsMovies)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
