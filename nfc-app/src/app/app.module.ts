import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { AngularFireModule } from 'angularfire2';
import { AngularFireDatabaseModule, AngularFireDatabase } from 'angularfire2/database';
import { AngularFireAuthModule } from 'angularfire2/auth';

export const firebaseConfig = {
  apiKey: "AIzaSyCP1HtrbReWHgOFQDMv3B8_WVyOCc18UJg",
  authDomain: "nmd-cms.firebaseapp.com",
  databaseURL: "https://nmd-cms.firebaseio.com",
  projectId: "nmd-cms",
  storageBucket: "nmd-cms.appspot.com",
  messagingSenderId: "84102007611"
};
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
