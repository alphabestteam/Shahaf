import { Component, Input } from '@angular/core';
import { commentService } from '../services/comment.services';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent {

  @Input() recipe_comment_id: any

  @Input() recipe_id: any

  comment:any = []

  username = sessionStorage.getItem('username');

  constructor(private comment_service: commentService) {}

  async getAllRecipes() {
    try{
      let res = await this.comment_service.getComment(this.recipe_comment_id);
      res.subscribe((data:any) => {
        this.comment = data
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
