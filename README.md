# log_scale_posters
Various "zoom videos" of multiple scales logarithmically unfolded linear posters.


## The Zoom Videos
One of the original "Zoom Videos" from 1977,

* ["POWERS OF TEN AND THE RELATIVE SIZE OF THINGS IN THE UNIVERSE"](https://www.eamesoffice.com/the-work/powers-of-ten/)
* [YouTube](https://www.youtube.com/watch?v=0fKBhvDjuy0)

A modern update to the original concept, "Cosmic Eye":

* ["Cosmic Eye: A Micro and Macrocosmic View of The Universe"](https://www.rickhanson.net/cosmic-eye-micro-macrocosmic-view-universe/)
* [YouTube](https://www.youtube.com/watch?v=Kpr-bnJ_K78)

Iterative Artwork of Chris Tolworthy rendered into an "Infinite Zoom":

* [Infinite Zoom](http://www.tedagame.com/zoomvideo/)
* [YouTube](https://www.youtube.com/watch?v=0vnA_KIojLg)

Cary & Michael Huang's "Scale of the Universe":

* [Scales of the Universe](https://htwins.net/scale2/)
* [YouTube](https://www.youtube.com/watch?v=6XHa6EDCBzo)

## Acquiring the videos from YouTube
Acquiring the videos from YouTube can be accomplished from following the directions [here](https://www.lifewire.com/convert-youtube-videos-to-mp4-with-vlc-media-player-2438324)

## Rendering frames

ffmpeg -i zoom-no-watermark.mp4 -r 20 frame_%05d.png
