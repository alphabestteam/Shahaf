import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  isSuccess = true

  options: number[] = [1, 2, 3];
  selectedOption: number = this.options[0];

  showWarning(): void {
    this.isSuccess = false
  }

  showSuccess(): void {
    this.isSuccess = true
  }

  getRepeatArray(count: number): number[] {
    return Array.from({ length: count }, (_, i) => i);
  }
}
