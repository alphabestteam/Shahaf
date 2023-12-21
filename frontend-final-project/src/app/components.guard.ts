import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
 
export class recipeGuard implements CanActivate {
  constructor(private router: Router) {}

  canActivate(): any  {
    this.router.navigate(['/home'])
    return false
  }
}
