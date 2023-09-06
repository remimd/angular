import { Component } from '@angular/core';
import {RoomRepository} from "src/repositories/room.repository";
import {Router} from "@angular/router";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  constructor(private router: Router, private repository: RoomRepository) {
  }

  async create(): Promise<void> {
    const room_id = await this.repository.create()
    await this.router.navigate([`room/${room_id}`])
  }
}
