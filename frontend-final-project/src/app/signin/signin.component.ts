import { Input, Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { LoginService } from '../services/login.services';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})


export class SigninComponent {
  form: FormGroup = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required],
    birthday: ['', Validators.required],
    email: ['', Validators.required],
    id: ['', Validators.required],
  });

  constructor(private signinService: LoginService, private fb: FormBuilder) {}

  async onSubmit() {
    if (this.form.valid) {
      try{
        let username = this.form.get('username')?.value,
        password = this.form.get('password')?.value,
        birthday = this.form.get('birthday')?.value,
        email = this.form.get('email')?.value,
        id = this.form.get('id')?.value

        let res = await this.signinService.signin(username, password, birthday, email, id);
        res.subscribe((data:any) => {
          this.dataSave()
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

  dataSave(){
    let username = this.form.value.username
    sessionStorage.setItem('username', username);
  }

  get(){
    return sessionStorage.getItem('username');
  }
}
