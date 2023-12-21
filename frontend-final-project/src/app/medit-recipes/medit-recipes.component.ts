import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';
import { commentService } from '../services/comment.services';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-medit-recipes',
  templateUrl: './medit-recipes.component.html',
  styleUrls: ['./medit-recipes.component.css']
})
export class MeditRecipesComponent {

  form: FormGroup = new FormGroup({
    rating: new FormControl(''),
    text: new FormControl(''),
  });

  meditRecipes: any = []

  constructor(private meditrecipes: recipesService, private comment_service: commentService) {}

  username = sessionStorage.getItem('username');

  async getAllRecipes() {
    try{
      let res = await this.meditrecipes.getMedit();
      res.subscribe((data:any) => {
        this.meditRecipes = data
        console.log(this.meditRecipes)
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
