import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { Album } from '../albums';
import { AlbumsService } from '../albums.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-albums-detail',
  templateUrl: './albums-detail.component.html',
  styleUrls: ['./albums-detail.component.css']
})
export class AlbumsDetailComponent implements OnInit{
  album: Album;
  updatedAlbum: Album
  constructor(private route: ActivatedRoute, private albumService: AlbumsService, private location: Location) {
    this.album = {} as Album
    this.updatedAlbum = {id: this.album.id, userId: this.album.userId} as Album
  }
  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.albumService.getAlbum(id).subscribe( (album) => {
      this.album = album;
    })
  }
  updateTitle(id: number) {
    this.updatedAlbum.userId = this.album.userId;
    this.albumService.updateTitle(id, this.updatedAlbum).subscribe( (album) => {
      this.album = album;
    })
  }
  returnBack() {
    this.location.back();
  }
}