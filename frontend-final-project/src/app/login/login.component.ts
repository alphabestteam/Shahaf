import { ReactiveFormsModule } from '@angular/forms';
import { Input, Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { LoginService } from '../services/login.services';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
    form: FormGroup = new FormGroup({
    username: new FormControl(''),
    password: new FormControl(''),
  });

  submit: boolean = false

  constructor(private loginServ: LoginService) {}

  async onSubmit() {
    if (this.form.valid) {
      try{
        const submit_username = this.form.get('username')?.value;

        await this.loginServ.login(submit_username);
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
