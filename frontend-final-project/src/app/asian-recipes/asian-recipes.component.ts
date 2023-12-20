import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-asian-recipes',
  templateUrl: './asian-recipes.component.html',
  styleUrls: ['./asian-recipes.component.css']
})
export class AsianRecipesComponent {
  asianRecipes: any = []

  constructor(private asianrecipes: recipesService) {}

  async getAllRecipes() {
    try{
      let res = await this.asianrecipes.getDessert();
      res.subscribe((data:any) => {
        this.asianRecipes = data
        console.log(this.asianRecipes)
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
