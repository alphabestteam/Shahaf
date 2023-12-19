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
    {value: 'asian-0', viewValue: 'Asian'},
    {value: 'italian-1', viewValue: 'Italian'},
    {value: 'mediterranean-2', viewValue: 'Mediterranean'},
    {value: 'desserts-2', viewValue: 'Desserts'},
    {value: 'other-2', viewValue: 'Other'},
  ];

  levels: Types[] = [
    {value: 'beginner-0', viewValue: 'Beginner'},
    {value: 'intermediate-1', viewValue: 'Intermediate'},
    {value: 'advanced-2', viewValue: 'Advanced'},
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
