import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-asian-recipes',
  templateUrl: './asian-recipes.component.html',
  styleUrls: ['./asian-recipes.component.css']
})
export class AsianRecipesComponent {
  asianRecipes = []

  constructor(private asianService: recipesService) {}

  async getAsianRecipes() {
    try{
      let res = await this.asianService.getAsian();
      res.subscribe((data:any) => {
        this.getAsianRecipes = data
      });
    }

    catch (error){
      console.log('get failed');
    }
  }

  ngOnInit(): void {
    this.getAsianRecipes();

    setInterval(() => {
      this.getAsianRecipes();
    }, 100000);
  }
}
