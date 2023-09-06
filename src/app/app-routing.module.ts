import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {RoomComponent} from "@app/room/room.component";
import {HomeComponent} from "@app/home/home.component";

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'room/:id', component: RoomComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
