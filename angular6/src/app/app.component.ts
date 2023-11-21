import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'angular6';
  
  userForm: FormGroup = new FormGroup({});;
  formError = this.userForm.valid;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.userForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]]
    });
  }

  outputForm() {
    if (this.formError) {
      console.log(this.userForm.value)
    }
    else {
      console.log(this.userForm.errors)
    }
  }
}
