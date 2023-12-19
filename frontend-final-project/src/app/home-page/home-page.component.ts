import { Component, OnInit  } from '@angular/core';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent {
  quotes: any = [
    {name: 'Alice', quote: '"This recipe website has become my culinary companion. From quick weekday meals to impressive dinner party dishes, I find inspiration for every occasion!"'},
    {name: 'Bob', quote: '"As someone passionate about cooking, I appreciate the diverse collection of recipes here. The step-by-step instructions make it easy to try new dishes and elevate my skills in the kitchen."'},
    {name: 'Claire', quote: '"This recipe platform is a lifesaver for a busy mom like me. I can always count on finding delicious and family-friendly recipes that are easy to prepare. Its my go-to resource for meal planning."'},
    {name: 'Frank', quote: '"This recipe platform is not just a source of recipes; its a culinary community. Ive learned so much from other users, and the feedback on my own creations has been invaluable in honing my skills."'},
  ]

  quote: any = this.quotes[0];

  index: number = 0;

  getNextRandomQuote(): void{
    if (this.index < 4){
      this.index += 1
    }
    else{
      this.index = 0
    }
    this.quote = this.quotes[this.index]
    console.log(this.quotes[this.index])
  }

  getPreRandomQuote(): void{
    if (this.index > 0){
      this.index -= 1
      console.log(this.index)
    }
    else{
      this.index = 3
    }
    this.quote = this.quotes[this.index]
    console.log(this.quotes[this.index])
  }
}

