# How to build and run docker image

## Build the docker
1. download [docker file](https://github.com/Sviatoslav1886/Data_science_2023/blob/main/homework_lesson_34/Docker/Dockerfile)
2. Open a terminal in the directory and run the command below:
```bash
docker build -t api-yolo:latest .
```
3. After that run the Docker container using following command:
```bash
docker run -p 8000:8000 api-yolo:latest
```
4. Access the application at 
```https
http://localhost:8000/
```
