import { Component } from '@angular/core';
import { LoginService } from '../services/login.services';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  submit: boolean = false

  profile: any = null;

  recipe: any = null;

  username :any = null

  constructor(private profileService: LoginService) {}

  getUser():void {
    if (this.username){
      this.profileService.getProfile(this.username).subscribe((data: any) => {
        this.profile = data
        console.log(this.profile)
      });
    }
    else{
      console.error('Username is null.'); 
    }
  }

  isConnected(){
    return sessionStorage.getItem('username')
  }

  dataRemove(){
    sessionStorage.removeItem('username');
  }

  ngOnInit(): void {
    this.username = sessionStorage.getItem('username')
    this.getUser();

    setInterval(() => {
      this.getUser();
    }, 1000);
  }
}
