# Python image quick compressor

### From **Python 3.8.1 slim buster image**

Quick image compressor container using **Pillow**

Use `docker-compose build` to build up the image then put the images you want to compress in the `input` folder. 

Use `docker-compose up` to compress images from `input` folder and get them from `output` folder.

Don't use `-verbose` flag if you don't want to have output informations.