import axios from "axios";
import {backendURL} from "src/settings";
import {Injectable} from "@angular/core";


@Injectable({providedIn: "root"})
export class RoomRepository {
  async create(): Promise<string> {
    const response = await axios.post(`${backendURL}/api/room`)
    return response.data
  }

  async getImagesURL(roomID: string): Promise<string[]> {
    const response = await axios.get(`${backendURL}/api/room/${roomID}`)
    const imagesURL: string[] = []

    for (let image of response.data.images) {
      imagesURL.push(`${backendURL}/media/${roomID}/${image.name}`)
    }

    return imagesURL
  }

  async upload(roomID: string, file: File): Promise<void> {
    await axios.post(`${backendURL}/api/room/${roomID}/upload`, {file: file}, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
  }
}
