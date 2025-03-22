import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
if __name__ == '__main__':
	model = YOLO('ultralytics/cfg/models/11/yolo11n.yaml')   # 修改yaml
	model.load('yolo11n.pt')  #加载预训练权重
	model.train(data='cat.yaml',   #数据集yaml文件
	            imgsz=640,
	            epochs=200,
	            batch=64,
	            workers=8,
	            device=0,   #没显卡则将0修改为'cpu'
	            optimizer='SGD',
                amp = False,
	            cache=False,   #服务器可设置为True，训练速度变快
	)
