# log_scale_posters

Various "zoom videos" of multiple scales logarithmically unfolded linear posters. I would love to see one of these printed out and put in a classroom.

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

Cary & Michael Huang's "Scale of the Universe" (this is what I want as a poster):

* [Scales of the Universe](https://htwins.net/scale2/)
* [YouTube](https://www.youtube.com/watch?v=6XHa6EDCBzo)

Kurzgesagt "Universe in a Nutshell" (NOT YET RENDERED) (or this one!!!):

* [Universe in a Nutshell](https://shop-us.kurzgesagt.org/products/universe-in-a-nutshell-app)
* [YouTube](https://www.youtube.com/watch?v=PGh8SWjnIEI)

## Acquiring the videos from YouTube

Acquiring the videos from YouTube can be accomplished from following the directions [here](https://www.lifewire.com/convert-youtube-videos-to-mp4-with-vlc-media-player-2438324)

## Rendering frames

ffmpeg -i video.mp4 -r 20 frame_%05d.png

## "Unfolding" and "Fusing"

The following renderings can be created by running the `unfold_and_fuse.py` script with the following parameters:

`./unfold_and_fuse.py --start=1044 --end=1486 --gap=7 --edge=539 --tolerance=20 --sample_radius=94.5 {cosmic eye frame directory}`

## Results

* Powers of Ten:
![Powers of Ten](./result_imgs/PowersOfTen.png)
* Cosmic Eye:
![Cosmic Eye](./result_imgs/CosmicEye.png)
* Tedagame Infinite Zoom:
![Tedagame](./result_imgs/TedAGame.Infinite.Zoom.png)
* Scale of the Universe:
![Scale of the Universe](./result_imgs/ScaleOfTheUniverse.png)
