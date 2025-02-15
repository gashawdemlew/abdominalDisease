# Abdominal Disease Stages Detector

## Description

This repository provides the codebase to test a deployed model for the detection of **abdominal disease pain stages**, including:

- Normal
- Acute
- Abscess
- Appendicolith
- Perforated

The model was trained using **image processing** and **computer vision technologies**, specifically object detection approaches. It utilizes MRI images collected from various hospitals in Ethiopia.

---

## Process of Model Development

The model was developed using the following steps:

1. **Image Collection and Preprocessing**:
   - MRI images were collected from hospitals.
   - Preprocessing steps included cleaning, resizing, and normalizing the images for training.

2. **Image Annotation and Augmentation**:
   - Annotation tools such as **Roboflow** and **Labelme** were used to label the datasets.
   - Image augmentation techniques included:
     - Resizing
     - Rotation
     - Adjusting contrast and brightness
     - Other transformations to improve dataset variability.

3. **Model Training**:
   - The model was trained using popular object detection pre-trained models, including:
     - **YOLO** (You Only Look Once)
     - **Faster R-CNN**
     - **SSD** (Single Shot Multibox Detector)

4. **Testing and Evaluation**:
   - The model achieved an **F-score of 82%**, demonstrating good performance in detecting abdominal disease stages.

5. **Model Deployment**:
   - The trained model was deployed on either:
     - **On-premise servers**
     - **Cloud platforms** (paid or free options like Hugging Face).

---

## How to Use This Repository

Follow the steps below to use this repository to test the deployed model:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/gashawdemlew/abdominalDisease.git
cd abdominalDisease
```

---

### 2. Install Required Python Packages

Ensure you have Python installed. Then, install the necessary dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```

---

### 3. Run the Application
Run the app.py file on your local machine:
```bash
python app.py
```

---

### 4. Input Test Data
- Use the test data provided in the test-data folder to evaluate the model.
- Upload MRI images or provide the required input to test the model's performance.

---

## Deployment
The deployed model is available on Hugging Face. You can directly test the model online or integrate it into your application.

### Deployed Model Link: Hugging Face Model [Link](https://huggingface.co/spaces/gashudemman/abdomenDiseaseDetector)
If you prefer to deploy the model yourself, you can use the following platforms:

1. On-Premise Server: Use Docker or other tools to host the model locally.
2. Cloud Platforms:
    - Paid platforms like AWS, GCP (Google Cloud), or Azure.
    - Free platforms like Hugging Face Spaces.

---

## Features
- Abdominal Disease Detection:
        - Detects pain stages including normal, acute, abscess, appendicolith, and perforated.
- Image Processing:
        - Preprocesses and augments MRI images for improved accuracy.
- Object Detection:
        - Leverages pre-trained models like YOLO, Faster R-CNN, and SSD for high performance.
- Cloud Integration:
        - Model is deployable on cloud platforms for easy accessibility.
    
---

## Testing
To test the model:

1. Clone the repository and set it up as described in the "How to Use" section.
2. Use MRI images from the test-data folder or your own data.
3. Run the application, and view the output to check the detected disease stage.

---

## Technologies Used
- Python: The primary programming language.
- Computer Vision: Techniques for image processing and object detection.
- Object Detection Models:
    - YOLO (You Only Look Once)
    - Faster R-CNN
    - SSD (Single Shot Multibox Detector)
- Annotation Tools:
        - Roboflow
        - Labelme
- Deployment: Hugging Face, on-premise servers, or cloud platforms.

---

## License
This project is licensed under the MIT License.


---

## Contact
For questions or support, feel free to reach out:

    - Email: your-email@example.com
    - LinkedIn: Your LinkedIn Profile