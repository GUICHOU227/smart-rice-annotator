from ultralytics import YOLO
import multiprocessing
import matplotlib.pyplot as plt
import cv2

if __name__ == '__main__':
    multiprocessing.freeze_support()

    model = YOLO("./autolabel_model/exp012/weights/best.pt")

    results = model.predict(
        source="./testimage",  # 指定訓練任務檔
        conf=0.1,  # 輸入影像大小
        save=True,  # 訓練世代數
        save_txt=True,  # 等待世代數，無改善就提前結束訓練
        save_conf=False,
        save_crop=True,  # 批次大小
        visualize=False)














