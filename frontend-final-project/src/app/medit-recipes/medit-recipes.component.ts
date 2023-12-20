import { Component } from '@angular/core';
import { recipesService } from '../services/recipes.services';

@Component({
  selector: 'app-medit-recipes',
  templateUrl: './medit-recipes.component.html',
  styleUrls: ['./medit-recipes.component.css']
})
export class MeditRecipesComponent {
  meditRecipes: any = []

  constructor(private meditrecipes: recipesService) {}

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

  ngOnInit(): void {
    this.getAllRecipes();

    setInterval(() => {
      this.getAllRecipes();
    }, 10000);
  }
}
