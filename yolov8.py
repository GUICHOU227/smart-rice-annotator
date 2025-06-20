import ultralytics
from ultralytics import YOLO
import multiprocessing



if __name__ == '__main__':
    multiprocessing.freeze_support()

    model = YOLO('yolov8n.pt')
    results = model.train(
        data="C:/Users/sophia/PycharmProjects/pythonProject/data_yaml/Rice_Seedling_Datasets.yaml",  # Specify training task file
        imgsz=640,  # Input image size
        epochs=100,  # Number of training epochs
        patience=50,  # Number of epochs to wait for improvement before early stopping
        batch=10,  # Batch size
        project='yolov8_project_1',  # Project name
        name='exp01',
        optimize=False,  # Disable optimization (use CPU for NMS)
    )
