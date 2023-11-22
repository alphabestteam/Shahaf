import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'basics-assignments-5-start';
  opening_crawl = `Luke Skywalker has returned to
    his home planet of Tatooine in
    an attempt to rescue his
    friend Han Solo from the
    clutches of the vile gangster
    Jabba the Hutt.
    
    Little does Luke know that the
    GALACTIC EMPIRE has secretly
    begun construction on a new
    armored space station even
    more powerful than the first
    dreaded Death Star.
    
    When completed, this ultimate
    weapon will spell certain doom
    for the small band of rebels
    struggling to restore freedom
    to the galaxy...`;

}

export interface StarWarsMovie {
  title: string;
  episode_id: number;
  opening_crawl: string;
  director: string;
  producer: string;
  release_date: string; 
}
