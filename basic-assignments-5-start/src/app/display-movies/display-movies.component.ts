import { Component } from '@angular/core';
import { FILMS } from '../star-wars-fake-db/film-data';

@Component({
  selector: 'app-display-movies',
  templateUrl: './display-movies.component.html',
  styleUrls: ['./display-movies.component.scss']
})
export class DisplayMoviesComponent {
  films = FILMS;
}
