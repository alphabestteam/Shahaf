import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class commentService {
    constructor(private http: HttpClient) {}

    getComment(id: string): Observable<any> {
        return this.http.get(`http://127.0.0.1:8000/comments/${id}/`)
    }

    postComment(username: any, recipe_id:number, text: string, stars: number): Observable<any> {
        return this.http.post(`http://127.0.0.1:8000/comments/`, {'username': username, 'recipe_id': recipe_id, 'text': text, 'stars': stars})
    }
}