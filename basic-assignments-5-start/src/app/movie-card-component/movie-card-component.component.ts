import { Component, Input } from '@angular/core';
import { StarWarsMovie } from '../app.component';

@Component({
  selector: 'app-movie-card-component',
  templateUrl: './movie-card-component.component.html',
  styleUrls: ['./movie-card-component.component.scss']
})
export class MovieCardComponentComponent {
  @Input() movie: StarWarsMovie= {
    title: '',
    episode_id: 1,
    opening_crawl: '',
    director: '',
    producer: '',
    release_date: '',
  };
}
