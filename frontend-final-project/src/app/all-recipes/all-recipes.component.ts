import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-all-recipes',
  templateUrl: './all-recipes.component.html',
  styleUrls: ['./all-recipes.component.css']
})
export class AllRecipesComponent {

  allRecipes = []

  constructor(private allrecipes: recipesService) {}

  async getAllRecipes() {
    try{
      let res = await this.allrecipes.getAll();
      res.subscribe((data:any) => {
        this.allRecipes = data
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
    }, 100000);
  }
}
