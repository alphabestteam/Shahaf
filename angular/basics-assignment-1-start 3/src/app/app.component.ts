import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  isSuccess = true

  showWarning(): void {
    this.isSuccess = false
  }

  showSuccess(): void {
    this.isSuccess = true
  }
}
