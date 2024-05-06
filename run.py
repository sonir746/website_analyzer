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