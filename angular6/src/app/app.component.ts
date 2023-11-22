import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title: string = 'angular6';
  
  userForm: FormGroup = new FormGroup({});;
  formError: boolean = this.userForm.valid;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.userForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]]
    });
  }

  outputForm(): void {
    if (this.formError) {
      console.log(this.userForm.value)
    }
    else {
      console.log(this.userForm.errors)
    }
  }

  usernameIsTouched(): boolean {
    return (this.userForm.get('username')?.invalid && (this.userForm.get('username')?.touched || this.userForm.get('username')?.dirty))??false
  }

  passwordIsTouched(): boolean {
    return (this.userForm.get('password')?.invalid && (this.userForm.get('password')?.touched || this.userForm.get('password')?.dirty))??false
  }

  emailIsTouched(): boolean {
    return (this.userForm.get('email')?.invalid && (this.userForm.get('email')?.touched || this.userForm.get('email')?.dirty))??false
  }
}
