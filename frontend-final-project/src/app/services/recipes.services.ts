import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class recipesService {
    constructor(private http: HttpClient) {}

    getAll(): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/recipes/`)
    }

    getAsian(): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/recipes/getAsian`)
    }

    getMedit(): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/recipes/getMedit`)
    }

    getItalian(): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/recipes/getItalian`)
    }

    getDessert(): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/recipes/getDessert`)
    }

    getOther(): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/recipes/getOther`)
    }

    submit(name: string, ingredients:string, preparation:string, type:string, time: string, level:string): Observable<any> {
        let url = 'http://127.0.0.1:8000/recipes/'
        let data = {name, ingredients, preparation, type, time, level}
        return this.http.post(url, data)
    }
}