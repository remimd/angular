import {Component} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {RoomRepository} from "src/repositories/room.repository";

@Component({
  selector: 'app-room',
  templateUrl: './room.component.html',
  styleUrls: ['./room.component.scss']
})
export class RoomComponent {
  private id: string | null
  public imagesURL: string[]

  constructor(private route: ActivatedRoute, private repository: RoomRepository) {
    this.id = null
    this.imagesURL = []
  }

  async ngOnInit(): Promise<void> {
    this.id = this.route.snapshot.paramMap.get('id');
    await this.fetchImages()
  }

  async fetchImages(): Promise<void> {
    this.imagesURL = await this.repository.getImagesURL(this.id as string)
  }

  async upload(event: any): Promise<void> {
    const file = event.target.files[0]
    await this.repository.upload(this.id as string, file)
    event.target.value = null
    await this.fetchImages()
  }
}
