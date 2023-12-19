import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class LoginService {
    constructor(private http: HttpClient) {}

    login(username: string, password: string): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/users/login/${username}/${password}/`)
    }

    signin(username: string, password:string, birthday:Date, email:string, id:number): Observable<any> {
        let url = 'http://127.0.0.1:8000/users/'
        let data = {username, password, birthday, email, id}
        return this.http.post(url, data)
    }

    getProfile(username: string): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/users/getUser/${username}/`)
    }
}