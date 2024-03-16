from fastapi import FastAPI, File, UploadFile, Response
from pydantic import BaseModel
from transformers import YolosImageProcessor, YolosForObjectDetection
from PIL import Image, ImageDraw
import torch
import io
import matplotlib.pyplot as plt
import matplotlib.patches as patches

app = FastAPI()

class ImageInput(BaseModel):
    file: UploadFile

@app.post("/predict/")
async def predict_yolo(image: UploadFile = File(...)):
    image_data = await image.read()
    img = Image.open(io.BytesIO(image_data))

    model = YolosForObjectDetection.from_pretrained('hustvl/yolos-tiny')
    image_processor = YolosImageProcessor.from_pretrained("hustvl/yolos-tiny")

    inputs = image_processor(images=img, return_tensors="pt")  # Use the PIL Image object directly
    outputs = model(**inputs)

    results = image_processor.post_process_object_detection(
        outputs, threshold=0.9, target_sizes=torch.tensor([img.size[::-1]])
    )[0]

    # Create the response image with bounding boxes
    response_img = img.copy()  # Avoid modifying the original image
    draw = ImageDraw.Draw(response_img)  # Use ImageDraw to draw on the image
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        label_name = model.config.id2label[label.item()]
        draw.rectangle(box, outline='red', width=2)
        draw.text((box[0], box[1]), f'{label_name} {round(score.item(), 3)}', fill='green')

    # Convert the image back to bytes for response
    img_byte_arr = io.BytesIO()
    response_img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)

    # Plot bounding boxes
    plt.figure()
    plt.imshow(response_img)
    ax = plt.gca()
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        label_name = model.config.id2label[label.item()]
        
        # Create a Rectangle patch
        rect = patches.Rectangle((box[0], box[1]), box[2]-box[0], box[3]-box[1], linewidth=2, edgecolor='r', facecolor='none')
        
        # Add the patch to the Axes
        ax.add_patch(rect)
        ax.text(box[0], box[1], f'{label_name} {round(score.item(), 3)}', color='black', fontsize=8, bbox=dict(facecolor='yellow', alpha=0.5))
        
    plt.axis('off')
    plt.tight_layout()

    # Save the plot as bytes
    plot_byte_arr = io.BytesIO()
    plt.savefig(plot_byte_arr, format='JPEG')
    plot_byte_arr.seek(0)
    plt.close()

    return Response(content=plot_byte_arr.read(), media_type="image/jpeg")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
