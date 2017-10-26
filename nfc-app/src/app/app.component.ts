import { Component } from '@angular/core';

import { AngularFireDatabase, AngularFireList } from 'angularfire2/database';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'nmd-cms',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  personsListRef: AngularFireList<any[]>;
  personsList: Observable<any[]>;

  constructor(public af: AngularFireDatabase) {
    this.personsListRef = af.list('/persons');
    this.personsList = this.personsListRef.snapshotChanges().map(changes => {
      return changes.map(c => ({ key: c.payload.key, ...c.payload.val() }));
    });
  }
}
