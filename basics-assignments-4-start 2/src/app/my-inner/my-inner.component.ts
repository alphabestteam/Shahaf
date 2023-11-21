import { Component, Input, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {
  @Input() outerTotal: number = 0;
  innerTotal: number = 5;

  @Output() greaterThan10 = new EventEmitter<number>();
  @Output() smallerThanMinus10 = new EventEmitter<number>();

  incrementInnerTotal() {
    this.innerTotal++;

    if (this.innerTotal > 10) {
      this.innerTotal = 0;
      this.greaterThan10.emit(this.outerTotal + 10);
    }

    else if (this.innerTotal < -10) {
      this.innerTotal = 0;
      this.smallerThanMinus10.emit(this.outerTotal - 10);
    }
  }

}
