import { Input, Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

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

  form: FormGroup = new FormGroup({
    username: new FormControl(''),
    password: new FormControl(''),
  });

  submit() {
    if (this.form.valid) {
      this.submitEM.emit(this.form.value);
    }
  }
  @Input() error: string | null = '';

  @Output() submitEM = new EventEmitter();
}
