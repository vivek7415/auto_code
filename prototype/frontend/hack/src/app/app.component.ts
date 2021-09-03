import { Component } from '@angular/core';
import { UserQueryService } from './user-query.service';
import { DomSanitizer } from '@angular/platform-browser';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})



export class AppComponent {
  constructor( private service: UserQueryService, private sanitizer: DomSanitizer) { }


  code: any;
  fileUrl;
  title = 'hack';
  public lan = ["java","python"];
  selected:string='java';

  ngOnInit() {
    console.log(this.code)
    const data = this.code;
    const blob = new Blob([data], { type: 'application/octet-stream' });

    this.fileUrl = this.sanitizer.bypassSecurityTrustResourceUrl(window.URL.createObjectURL(blob));
  }

  // query:Query=new Query;
  onClickSubmit(form) {
    console.log("You have entered : " + form.value.userQuery +" " + form.value.userLanguage);
    this.service.UserQuery(form.value.userQuery +" " + form.value.userLanguage).subscribe(response=>{
      // console.log(response)
      this.code = response[0];
    });

 }


  }

