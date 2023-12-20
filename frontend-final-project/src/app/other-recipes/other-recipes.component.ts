import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-other-recipes',
  templateUrl: './other-recipes.component.html',
  styleUrls: ['./other-recipes.component.css']
})
export class OtherRecipesComponent {
  otherRecipes: any = []

  constructor(private othertrecipes: recipesService) {}

  async getAllRecipes() {
    try{
      let res = await this.othertrecipes.getOther();
      res.subscribe((data:any) => {
        this.otherRecipes = data
        console.log(this.otherRecipes)
      });
    }

    catch (error){
      console.log('submit failed');
    }
  }

  ngOnInit(): void {
    this.getAllRecipes();

    setInterval(() => {
      this.getAllRecipes();
    }, 10000);
  }
}
