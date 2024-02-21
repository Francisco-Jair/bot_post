# docker build -t myapp .
docker run -v .:/app myapp 
# docker run -it -v .:/app myapp
# docker run -it -v $(pwd):/app myapp