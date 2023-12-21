import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';
import { commentService } from '../services/comment.services';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-desserts-recipes',
  templateUrl: './desserts-recipes.component.html',
  styleUrls: ['./desserts-recipes.component.css']
})
export class DessertsRecipesComponent {

  form: FormGroup = new FormGroup({
    rating: new FormControl(''),
    text: new FormControl(''),
  });

  dessertRecipes: any = []

  username = sessionStorage.getItem('username');

  constructor(private dessertrecipes: recipesService, private comment_service: commentService) {}

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

  ngOnInit(): void {
    this.getAllRecipes();

    setInterval(() => {
      this.getAllRecipes();
    }, 10000);
  }
}
