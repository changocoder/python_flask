docker run -it -p 5000:5000 -w /home/api -v %cd%:/home/api python:3.7-buster /bin/bash
#para el dockerfile
docker run --rm -d -p 5000:5000 pythonflask:0.1