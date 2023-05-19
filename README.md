# Real Time Traffic Light Detection using Deep Learning (YOLOv8)



## <u>Table of Contents</u>

* [About](#About)
* [Progress and TODO](#Progress-and-TODO)
* [Download Trained Weights](#Download-Trained-Weights)
* [Get the Dataset](#Get-the-Dataset)
* [Required libraries](#Libraries)
* [Steps to Train](#Steps-to-Train)
* [To Detect Using the Trained Model](#To-Detect-Using-the-Trained-Model)
* [References](#References)



## <u>About</u>

***This project aims to detect traffic light in real time using deep learning as a part of autonomous driving technology.***

* [Click on the following video to get a better idea about the project and predictions](https://drive.google.com/file/d/1dLRaIsBGeR4az3WhZvjODILmEwO8fDJi/view?usp=share_link).

[![Prediction Video]()](https://drive.google.com/file/d/1dLRaIsBGeR4az3WhZvjODILmEwO8fDJi/view?usp=share_link)



## <u>Progress and TODO</u>

* **Implementation of the traffic light and color detection is done. Check the [Download Trained Weights](#Download-Trained-Weights) section to get your desired weight files and try the model on you system.**


- [x] Detecting `traffic_light` sign.
- [x] Detecting `red` sign.
- [x] Detecting `yellow` sign.
- [x] Detecting `green` sign.




## <u>Download Trained Weights</u>

***Download the trained weights from [here](https://drive.google.com/drive/folders/11nL-1PpbyIKa89_QKcn6R-Exl9IRWxpu?usp=share_link).***

* `best.pt`: **Trained for 75 epochs on the traffic lights. Current mAP is 0.9**



## <u>Get the Dataset</u>

This project uses the [Traffic Light Dataset.](https://drive.google.com/drive/folders/1B3ybhabO7rmB4bron83vGtCsSGN1TYFx?usp=share_link). Download the dataset from google drive [here](https://drive.google.com/drive/folders/1B3ybhabO7rmB4bron83vGtCsSGN1TYFx?usp=share_link).

## Libraries required
* python
* numpy
* os
* ultralytics
* pytorch
* imgaug.augmenters
* cv2
* tqdm
* glob
* pandas


## <u>Steps to Train</u>

* **The current train/valid/test split is 70/20/10. The input image size is 416x416. So, it might take a lot of time to train if you train on a nominal GPU. I have trained the model on Google Colab with Tesla T4 GPU/P100 GPU. One epoch took with all the classes around 1/2 hour on a Tesla T4 GPU. Also, check all the folders and files before training.** 

* Prepare the data. **Please do take a look at the paths inside the `prepare_labels.py` file and change them according to your preference and convenience**.
  * `python prepare_labels.py`
  * `preprocessing_images.py`
* Create the train and validation text files (**Current train/validation/test split = 70/20/10**).
* To train on your own system (The current [model](https://drive.google.com/drive/folders/12TCovAPKxQW9875f10h4bu-USBBic27p?usp=share_link) has been trained for 75 epochs.)
  * **To train from scratch**: 

  `model = YOLO("yolov8n.yaml")`

  `results = model.train(data=os.path.join(ROOT_DIR, "google_colab_config.yaml"), epochs=75)`
  




## <u>To Detect Using the Trained Model</u>

* **Download the [weights here](https://drive.google.com/drive/folders/1nGRGqw5KP6js9UbXDL5G99j_jYdKgdXl?usp=sharing) first, and paste them under the `weights` folder.**
  * `!yolo task=detect mode=predict model='/content/drive/MyDrive/color_detection/runs/detect/train2/weights/best.pt' conf=0.25 source='/content/drive/`

 ## <u>Demo Video</u>

* **Demo video** : https://drive.google.com/file/d/1dLRaIsBGeR4az3WhZvjODILmEwO8fDJi/view?usp=share_link

## <u>References</u>

### Articles / Blogs / Tutorials

* [Recognizing Traffic Lights With Deep Learning.](https://www.freecodecamp.org/news/recognizing-traffic-lights-with-deep-learning-23dae23287cc/)
* [Self Driving Vehicles: Traffic Light Detection and Classification with TensorFlow Object Detection API.](https://becominghuman.ai/traffic-light-detection-tensorflow-api-c75fdbadac62)

### Papers

* [Detecting Traffic Lights by Single Shot Detection.](https://arxiv.org/pdf/1805.02523.pdf)
* [A Hierarchical Deep Architecture and Mini-Batch Selection Method For Joint Traffic Sign and Light Detection.](https://arxiv.org/pdf/1806.07987v2.pdf)
* [Accurate traffic light detection using deep neural network with focal regression loss.](https://pdf.sciencedirectassets.com/271526/1-s2.0-S0262885619X00062/1-s2.0-S0262885619300538/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIGJS6acKy%2Bn%2BogLTPASdUHm2kcAgzf%2BqPN9p8OeOtqjLAiEA%2F%2BXJIsDU4zTfeAt64IuxzWijoPZCAo8bGluHqWEyANsqvQMIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgwwNTkwMDM1NDY4NjUiDDRiyVid6olIGdZwzyqRA10sNlWjy52x5aHLEkbyTlAwKwbhfH5gpZfQkY5ZnbhmzmOJAyj16Ij6x1D3cJL3XTMMT9Bj8TXdEOISOnDN2ZDThSTyotxowSzF3GN1V%2Brwgsv07x6GgyUGQz1TsZrbNxrdV2nYPKukv9PUNdcyDXeIWYh5emqvRSl75xtX5%2BGA9%2Be8OkAe8LjrsQJO4M%2BWL5vtSfc2ljzZH%2B%2FWHRwT8YJy8HWVoH1RyEOa1UdOaqfC1f2LYi2AiyAhEg4ODoAqrC9IXDOX%2BynMp4YbmUfUXff%2BCb%2F%2FpBfnuxYXXHGqZxFwf6hex%2FlQietzZ%2FJZnfM1dxZFkWdZjXMPeY6J6k5itnCQt6155HICBAaCD4jnCD93EG3CWTcQFGw5Fa59xkM6dRcyjFCyjvvOoDcOQkOdC9KkqXTEsviKA%2BGtfbR9VdfHxXTz6Eg3L2r0e%2FMD%2BWnKC9gE1O305BfGwVpH8QoC4y2YA6J6EB5SRcYcAYfVHEXae8jFcmT7RwqMlNmkvi5UARGyOOOj0HfuPQQj2Yn1c7qAMKKTk%2FoFOusBF61AXrHbnIYcGm4t9%2FshIODSgtKRGuw2AgBfRK8OQzmSoPfxhmZBph8Cg7vLOWlc6tygObNnLajEnuHOqENs0MNVERQRqeypLtugKOjYPTXhx6c2QHdu3dxq2xxVl4G%2FouOSad0Jk4shK1tvi4zBK7XubyhBnZg2nYEPJY87jCqMiyi8frITa51hPkILVTPH%2BMnWj71w52itNJCgoZ%2FLGKr%2F0yvE4ASCGEP0mGPdv3%2BkRJdQDNXnTlZZJ2jBDnUF8ppTA%2F5Ts8TG0MlXlvVmokNAHToumbuwlKA6LtGQFM5Ik3ksBZ4y2v3mMw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200825T092944Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYZSN4AUAD%2F20200825%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=1a06167c3e97cae86c5f885091428f6313cd222846cba3196edfdd450e77f805&hash=42e81b760f319091bff8aa28f407c0be53b094e96dedd3e5895cf54cbcec3de6&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0262885619300538&tid=spdf-d78c15ef-4334-4615-9de5-b6e7a4fbcc3c&sid=9cbac0327e3d654a474b03703362e7cee4bdgxrqb&type=client)





