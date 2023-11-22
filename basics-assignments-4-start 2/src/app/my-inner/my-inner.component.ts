import { Component, Input, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {
  @Input() total: number = 0;
  innerTotal: number = 5;

  @Output() greaterThanNumber = new EventEmitter<number>();
  @Output() smallerThanMinusNumber = new EventEmitter<number>();

  increaseInnerTotal() {
    this.innerTotal++;

    if (this.innerTotal >= 10) {
      this.innerTotal = 0;
      this.greaterThanNumber.emit(10);
    }
  }

  decreaseInnerTotal() {
    this.innerTotal--;

    if (this.innerTotal <= -10) {
      this.innerTotal = 0;
      this.smallerThanMinusNumber.emit(-10);
    }
  }

}

