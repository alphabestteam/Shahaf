import { Component } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  submit: boolean = false

  isConnected(){
    return sessionStorage.getItem('username')
  }

  dataRemove(){
    sessionStorage.removeItem('username');
  }
}
