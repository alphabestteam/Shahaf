import { Component, Input } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-fav-recipe',
  templateUrl: './fav-recipe.component.html',
  styleUrls: ['./fav-recipe.component.css']
})
export class FavRecipeComponent {
  recipe: any = null

  @Input() recipe_id: any = null

  constructor(private recipe_service: recipesService) {}

  async getRecipe() {
    try{
      let res = await this.recipe_service.getID(this.recipe_id);
      res.subscribe((data:any) => {
        this.recipe = data
      });
    }

    catch (error){
      console.log('submit failed');
    }
  }

  ngOnInit($event: any): void {
    this.getRecipe();

    setInterval(() => {
      this.getRecipe();
    }, 1000);
  }
}
