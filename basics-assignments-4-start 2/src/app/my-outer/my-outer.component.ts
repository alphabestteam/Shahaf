import { Component } from '@angular/core';

@Component({
  selector: 'app-my-outer',
  templateUrl: './my-outer.component.html',
  styleUrls: ['./my-outer.component.css']
})
export class MyOuterComponent {
  outerTotal = 0;

  onIncreaseInnerTotal(addTotal: number): void{
    this.outerTotal = addTotal;
  }

  onDecreaseInnerTotal(subtractTotal: number): void{
    this.outerTotal = subtractTotal;
  }
}
