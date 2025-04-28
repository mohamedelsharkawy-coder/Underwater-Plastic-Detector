# Underwater Plastic Detector 🌊♻️

## Project Overview
Plastic pollution is a serious threat to our oceans and marine life, and it significantly harms the environment. The **Underwater Plastic Detector** project aims to automatically detect plastic waste underwater using AI. By leveraging deep learning models, this tool can help in identifying and managing underwater plastic pollution, contributing toward a cleaner and healthier planet.

![Underwater Plastic Detection Demo](video.gif)


## Project Pipeline
The project follows a standard machine learning pipeline:

1. **Data Gathering**  
   - Collected datasets from various sources: **Plastopal**, **TrashCan**, and **DeepTrash**.
2. **Data Preprocessing**  
   - Organized, cleaned, and formatted data into YOLO format.
3. **Model Building and Training**  
   - Utilized **YOLOv8n** (YOLOv8 Nano) from the **Ultralytics** library.
4. **Model Evaluation**  
   - Evaluated the model using metrics like mAP (mean Average Precision) and detection performance on unseen images.
5. **Model Deployment**  
   - Deployed the model as a **Flask API** hosted on **Google Colab** using **ngrok** for public access.

## Tech Stack and Tools

- Ultralytics YOLOv8n
- Python
- Flask (for building the API)
- Ngrok (for deployment tunneling)
- Google Colab (for training and hosting)
- OpenCV, NumPy, and Pandas (for data handling)

## Dataset Sources

- [Plastopal Dataset](https://universe.roboflow.com/k-s/plastopol-kyppj)
- [TrashCan Dataset](https://universe.roboflow.com/applied-machine-learning/trashcan-dataset)
- [DeepTrash Dataset](https://universe.roboflow.com/yolov5-thesis-paper/deeptrash-v2.0)

