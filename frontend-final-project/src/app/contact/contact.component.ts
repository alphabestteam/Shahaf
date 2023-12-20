import { Input, Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { recipesService } from '../services/recipes.services';

interface Types {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent {
  types: Types[] = [
    {value: 'asian', viewValue: 'Asian'},
    {value: 'italian', viewValue: 'Italian'},
    {value: 'mediterranean', viewValue: 'Mediterranean'},
    {value: 'desserts', viewValue: 'Desserts'},
    {value: 'other', viewValue: 'Other'},
  ];

  levels: Types[] = [
    {value: 'beginner', viewValue: 'Beginner'},
    {value: 'intermediate', viewValue: 'Intermediate'},
    {value: 'advanced', viewValue: 'Advanced'},
  ];

  form: FormGroup = this.fb.group({
    name: ['', Validators.required],
    ingredients: ['', Validators.required],
    preparation: ['', Validators.required],
    cuisine: new FormControl(''),
    time: ['', Validators.required],
    level: new FormControl(''),
  });

  constructor(private recipeService: recipesService, private fb: FormBuilder) {}

  async onSubmit() {
    if (this.form.valid) {
      try{
        let name = this.form.get('name')?.value,
        ingredients = this.form.get('ingredients')?.value,
        preparation = this.form.get('preparation')?.value,
        cuisine = this.form.get('cuisine')?.value,
        time = this.form.get('time')?.value,
        level = this.form.get('level')?.value

        let res = await this.recipeService.submit(name, ingredients, preparation, cuisine, time, level);
        res.subscribe((data:any) => {

          this.form.reset();
        });
      }

      catch (error){
        console.log('submit failed');
      }
    }
  }
  @Input() error: string | null = '';

  @Output() submitEM = new EventEmitter();
}
