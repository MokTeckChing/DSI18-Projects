from models.experimental import attempt_load
from utils.general import check_img_size, non_max_suppression
from utils.datasets import LoadStreams, LoadImages
import torch

def img_predict(source, webcam = False):

    imgsz = source

    imgsz = check_img_size(imgsz, s=model.stride.max())

#    if webcam:
#        view_img = True
#        cudnn.benchmark = True  # set True to speed up constant image size inference
#        dataset = LoadStreams(source, img_size=imgsz)

#    else:
#        dataset = LoadImages(source, img_size=imgsz)

    dataset = LoadImages(source, img_size=imgsz)

    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

    img = torch.zeros((1, 3, imgsz, imgsz), device=device)

    model = attempt_load(weights, map_location=device)

    names = model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    pred = model(img)[0]
    pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)





    if view_img:
        cv2.imshow(str(p), im0)
