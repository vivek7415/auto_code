import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class UserQueryService {

  constructor(private http:HttpClient) { }

  UserQuery(query): Observable<any>  {
    let url = "http://localhost:3000/query/"+query;
    console.log(query);
   return this.http.get<any>(url); 
  }
}