import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-italian-recipes',
  templateUrl: './italian-recipes.component.html',
  styleUrls: ['./italian-recipes.component.css']
})
export class ItalianRecipesComponent {
  italianRecipes: any = []

  constructor(private italianrecipes: recipesService) {}

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

  ngOnInit(): void {
    this.getAllRecipes();

    setInterval(() => {
      this.getAllRecipes();
    }, 10000);
  }
}
