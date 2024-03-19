# How to build and run docker image

## Build the docker
1. download [docker file](https://github.com/Sviatoslav1886/Data_science_2023/blob/main/homework_lesson_34/Dockerfile)
2. Open a terminal in the directory and run the command below:
```bash
docker build -t api-yolo:latest .
```
## Run the Docker container
Run the Docker container using following command:
```bash
docker run -p 8000:8000 api-yolo:latest
```
## Access the application
You can find your application at:
```https
http://localhost:8000/
```

## Screen that show how it works:
![Screenshot](https://github.com/Sviatoslav1886/Data_science_2023/blob/main/homework_lesson_34/Docker/screen_that_works_fine.jpg)


## Screen that show logs:
![Screenshot](https://github.com/Sviatoslav1886/Data_science_2023/blob/main/homework_lesson_34/Docker/screen_that_logs_work_fine.jpg)
