# website_analyzer

This Deep Learning project detect the tags used in HTML page

We use latest deep learning model which provide the accuracy approximately than 50%-65%.

## Packages Used

| **Package** | **Version** |
| ----------- | ----------- |
| Python      | 3.8         |
| OpenCV      | 4.8.1       |
| Yolo        | 8.0.2       |
| PyTorch     | 2.1.2       |
| LabelImg    | 1.8.6       |


## Run Locally

Clone the project

```bash
  git clone https://github.com/sonir746/website_analyzer.git
```

Go to the project directory

```bash
  cd <directory_path>
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Training

Use labelimg library to label the images to create a label data set and train our model to 

<img src="source\images\Labeling.png" alt="loading..." style="width:800px;"/>

### Traning Data
<img src="source\images\TraningData.png" alt="loading..." style="width:800px;"/>

## Traning Rusult

<img src="source\images\results.png" alt="loading..." style="width:800px;"/>

## Testing
1.	After that we imput image for test it.

2.	Model will extract the feature from the model and perform conditional  operation on the given feature.

3.	After that it will show the predicted image till any interruption.

## Source Code

```Python
import cv2
import torch
from ultralytics import YOLO

# give the path of model 
model = YOLO('model/model.pt') 

# give the path of image
img= 'source/images/input_4.png'

while True: 
    # predict the image
    results = model.predict(source=img,save=True, show=True, device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')) 
    
    #press ESC or 'q' or 'Q'  and hold a second for exit window
    if cv2.waitKey(1)==ord("q") or cv2.waitKey(1)==ord("Q") or cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows() 

```

## Input Image
<img src="source\images\input_4.png" alt="loading..." style="width:600px;"/>

## Predicted Image
<img src="source\images\output_4.png" alt="loading..." style="width:600px;"/>

<br>



https://github.com/sonir746/website_analyzer/assets/103484090/266cd097-b887-404d-96fa-77448dfe8f86



## Auther

👨🏻‍💼RAHUL SONI

[![linkedin](https://img.shields.io/twitter/url?url=https%3A%2F%2Fwww.linkedin.com&style=social&logo=Linkedin&logoColor=White&label=Linkedin&labelColor=blue&color=blue&cacheSeconds=3600
)](https://www.linkedin.com/in/rahul-soni-004861227)
[![GitHub](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2F&style=social&logo=GitHub&logoColor=Black&label=GitHub&labelColor=abcdef&color=fedcba&cacheSeconds=3600
)](https://github.com/sonir746)



## Feedback

If you have any feedback, please reach out to us at rahulsoni@gmail.com

Or

Report any issue here
<br>
👇👇👇
<br>
[![GitHub](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com&style=social&logo=GitHub&label=issue&labelColor=grey&color=grey
)](https://github.com/sonir746/website_analyzer/issues)
