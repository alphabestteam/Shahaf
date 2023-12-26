import { Component, Input } from '@angular/core';
import { commentService } from '../services/comment.services';
import { FormGroup, FormControl } from '@angular/forms';
import { RatingModule } from 'ngx-bootstrap/rating';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent {

  rate: number = 1;

  max: number = 5;
  
  isReadOnly: boolean = true;

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

  async deleteComment() {
    try{
      let res = await this.comment_service.removeComment(this.username, this.comment.comment_id);
      res.subscribe((data:any) => {
      });
    }

    catch (error){
      console.log('delete failed');
    }
  }

  ngOnInit($event: any): void {
    this.getAllRecipes();

    setInterval(() => {
      this.getAllRecipes();
    }, 10000);
  }
}
