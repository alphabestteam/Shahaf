import { ReactiveFormsModule } from '@angular/forms';
import { Input, Component, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';
import { LoginService } from '../services/login.services';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
    form: FormGroup = this.fb.group({
    username: ['', Validators.required],
    password: ['', Validators.required],
  });

  submit: boolean = false

  constructor(private loginServ: LoginService, private fb: FormBuilder) {}

  async onSubmit() {
    if (this.form.valid) {
      try{
        const submit_username = this.form.get('username')?.value;
        const submit_password = this.form.get('password')?.value;
        
        let res = await this.loginServ.login(submit_username, submit_password);
        res.subscribe((data:any) => {
          if (data == 'success'){
            this.dataSave()
            this.form.reset();
          }
        },
        (error: any) => {
          alert('User not found, please signin')
        })
      }

      catch (error){
        console.log('submit failed');
      }
    }
  }
  @Input() error: string | null = '';

  dataSave(){
    let username = this.form.value.username
    sessionStorage.setItem('username', username);
  }

  get(){
    return sessionStorage.getItem('username');
  }
}
