import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  paragraph = 'Secret Password = tuna';
  click = 0;
  showContent = true;

  toggleOnClick(): void{
    this.showContent = !this.showContent;
    this.click += 1;

  }

  getRepeatArray(count: number): number[] {
    return Array.from({ length: count }, (_, i) => i);
  }
}
