import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';
import { FormGroup, FormControl } from '@angular/forms';
import { commentService } from '../services/comment.services';

@Component({
  selector: 'app-italian-recipes',
  templateUrl: './italian-recipes.component.html',
  styleUrls: ['./italian-recipes.component.css']
})
export class ItalianRecipesComponent {

  form: FormGroup = new FormGroup({
    rating: new FormControl(''),
    text: new FormControl(''),
  });

  italianRecipes: any = []

  username = sessionStorage.getItem('username');

  constructor(private italianrecipes: recipesService, private comment_service: commentService) {}

  async getAllRecipes() {
    try{
      let res = await this.italianrecipes.getItalian();
      res.subscribe((data:any) => {
        this.italianRecipes = data
        console.log(this.italianrecipes)
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
