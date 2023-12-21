import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { LoginService } from './services/login.services';

@Injectable({
  providedIn: 'root'
})
 
export class authGuard implements CanActivate {
  constructor(private router: Router, private authService: LoginService) {}

  username = sessionStorage.getItem('username');

  canActivate(): any  {
    if (!this.username){
      this.router.navigate(['/home'])
      return false
    }
    return true
  }
}