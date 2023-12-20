import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-desserts-recipes',
  templateUrl: './desserts-recipes.component.html',
  styleUrls: ['./desserts-recipes.component.css']
})
export class DessertsRecipesComponent {
  dessertRecipes: any = []

  constructor(private dessertrecipes: recipesService) {}

  async getAllRecipes() {
    try{
      let res = await this.dessertrecipes.getDessert();
      res.subscribe((data:any) => {
        this.dessertRecipes = data
        console.log(this.dessertRecipes)
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
