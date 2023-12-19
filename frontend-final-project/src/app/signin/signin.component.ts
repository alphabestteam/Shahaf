import { Input, Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { LoginService } from '../services/login.services';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})


export class SigninComponent {
  form: FormGroup = new FormGroup({
    username: new FormControl(''),
    password: new FormControl(''),
    birthday: new FormControl(''),
    email: new FormControl(''),
    id: new FormControl(''),
  });

  constructor(private signinService: LoginService) {}

  async onSubmit() {
    if (this.form.valid) {
      try{
        let username = this.form.get('username')?.value,
        password = this.form.get('password')?.value,
        birthday = this.form.get('birthday')?.value,
        email = this.form.get('email')?.value,
        id = this.form.get('id')?.value

        await this.signinService.signin(username, password, birthday, email, id);
        this.dataSave()
        this.form.reset();
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
