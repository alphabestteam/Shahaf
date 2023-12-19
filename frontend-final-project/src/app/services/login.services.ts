import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class LoginService {
    constructor(private http: HttpClient) {}

    login(username: string): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/users/login/${username}`)
    }

    signin(username: string, password:string, birthday:Date, email:string, id:number): Observable<any> {
        let url = 'http://127.0.0.1:8000/users/'
        let data = {'username': username, 'password': password, 'birthday': birthday, 'email': email, 'id': id}
        return this.http.post(url, data)
    }
}