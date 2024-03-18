# Object Detection Web Application

## Overview
This application is a web application built using FastAPI that utilizes a machine learning model, specifically the pre-trained model 'hustvl/yolos-tiny', for object detection of images using YOLOS (You Only Look One-time Object Detection System). It allows users to submit images through a web interface and receive images with frames overlaid on them showing detected objects.

## Main Components

### Architecture
The service implemented as an API. List of the available endpoits:

*  '/' - index endpoint with server health-check.
*  '/predict/' - endpoint for classification image using image from user.

### Localization model
You can find the YOLO S model [here](https://huggingface.co/hustvl/yolos-tiny).


- **FastAPI**: Utilized for creating a web interface and handling HTTP requests.
- **YOLOS model for object detection**: Implements a YOLOS model using the transformers library.
- **pydantic BaseModel**: Defines the structure of the input data, specifically the image passed as input.
- **Prediction processing function (predict_yolo)**: Receives the uploaded image, performs YOLOS object detection, overlays the image with borders and labels showing the detection results, and returns the modified image.
- **Root path processing function (read_root)**: A simple function returning a JSON object containing the words "Hello" and "World".
- **Matplotlib and PIL**: Used for image manipulation and visualization.
- **uvicorn**: Utilized to launch a web server hosting the FastAPI application.

## Usage
Once the server is running, users can make a POST request to the /predict/ path by sending an image, and the application will return an image with borders and labels displaying the detected objects.
