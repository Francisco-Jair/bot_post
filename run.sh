docker build -t myapp .
# docker run -it myapp 
docker run -it -v .:/app myapp