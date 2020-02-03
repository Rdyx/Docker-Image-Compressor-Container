# Python image quick compressor

### From **Python 3.8.1 slim buster image**

Quick image compressor container using [**Pillow**](https://pillow.readthedocs.io/en/stable/).


Use `docker-compose build` to build up the image then put the images you want to compress in the `input` folder.

Use `docker-compose up` to compress images from `/input/` folder and get them from `/output/` folder.

You can also directly use the scripts from `/src/`. Don't forget to create `/input/` and `/output/` folders at the same level as `/src/` and put the images you want to process into `/input/`.

---
## Flags
### `--verbose`
Used to have output informations.

### `--max-height [number]`
Resize image from the max heightyou want for your pictures.

### `--max-width [number]`
Resize image from the max width you want for your pictures.

### `--ratio [float]`
Resize image based on a ratio.

### `--quality [number]`
Set the quality of compression (default to 65).

---
*Note that you can use `--max-height` and `--max-width` at same time to force pictures to be under a determined dimensions.*

*Note that you **can't** use `--max-*` with `--ratio`.*