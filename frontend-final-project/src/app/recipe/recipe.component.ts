import { Component, Input } from '@angular/core';
import { commentService } from '../services/comment.services';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-recipe',
  templateUrl: './recipe.component.html',
  styleUrls: ['./recipe.component.css']
})
export class RecipeComponent {

  form: FormGroup = new FormGroup({
    rating: new FormControl(''),
    text: new FormControl(''),
  });

  @Input() recipes: any

  // recipe_id: any

  username = sessionStorage.getItem('username');

  constructor(private comment_service: commentService) {}

  async addFav(recipe_id: any){
    let res = await this.comment_service.addFav(this.username, recipe_id);
        res.subscribe((data:any) => {
          alert('Recipe was added to favorites')
        });
  }

  async onSubmit(recipe_id: any){
    if (this.form.valid) {
      try{
        const rating = this.form.get('rating')?.value;
        const text = this.form.get('text')?.value;
        console.log(recipe_id)
        
        let res = await this.comment_service.postComment(this.username, recipe_id, text, rating);
        res.subscribe((data:any) => {
          this.form.reset();
        });

        (error: any) => {
          alert('User not found, please signin')
        }
      }

      catch (error){
        console.log('submit failed');
      }
    }
  }
}
