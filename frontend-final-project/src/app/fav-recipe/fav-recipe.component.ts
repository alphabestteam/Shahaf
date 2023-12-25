import { Component, Input } from '@angular/core';
import { recipesService } from '../services/recipes.services';
import { commentService } from '../services/comment.services';

@Component({
  selector: 'app-fav-recipe',
  templateUrl: './fav-recipe.component.html',
  styleUrls: ['./fav-recipe.component.css']
})
export class FavRecipeComponent {

  rate: number = 1;

  max: number = 5;
  
  isReadOnly: boolean = true;

  recipe: any = null

  @Input() recipe_id: any = null

  username = sessionStorage.getItem('username');

  constructor(private comment_service: commentService, private recipe_service: recipesService) {}

  async removeFav(recipe_id: any){
    let res = await this.comment_service.removeFav(this.username, recipe_id);
        res.subscribe((data:any) => {
          alert('Recipe was removed from favorites')
        });
  }

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
