import cv2  # 导入OpenCV库，用于图像处理和显示
from ultralytics import YOLO  # 导入YOLO模型，用于目标检测

# 加载预训练的YOLO模型
# 这里传入模型文件的路径（例如：yolo11n.pt）
model = YOLO(r"D:\Desktop\Yolov11Project\ultralytics-8.3.83\yolo11n.pt")

# 打开摄像头
# cv2.VideoCapture(0) 表示打开默认摄像头（通常是电脑自带的摄像头）
cap = cv2.VideoCapture(0)

# 设置跳帧数
# 例如 skip_frames = 5 表示每5帧处理一次，其余帧跳过
skip_frames = 5

# 初始化帧计数器
# 用于记录当前处理到第几帧
frame_count = 0

# 设置图像缩放比例
# scale_percent = 50 表示将图像分辨率缩小到原来的50%
scale_percent = 50

# 进入主循环，持续读取摄像头帧
while cap.isOpened():
    # 读取一帧图像
    # success 是一个布尔值，表示是否成功读取帧
    # frame 是当前帧的图像数据
    success, frame = cap.read()
    # 如果读取失败（例如摄像头断开），退出循环
    if not success:
        break

    # 帧计数器加1
    frame_count += 1

    # 跳帧逻辑：如果当前帧不是需要处理的帧，跳过本次循环
    if frame_count % skip_frames != 0:
        continue

    # 降低图像分辨率
    # 计算缩放后的图像宽度和高度
    width = int(frame.shape[1] * scale_percent / 100)  # 原始宽度乘以缩放比例
    height = int(frame.shape[0] * scale_percent / 100)  # 原始高度乘以缩放比例
    dim = (width, height)  # 目标图像尺寸

    # 使用OpenCV的resize函数缩放图像
    # cv2.INTER_AREA 是一种插值方法，适合缩小图像
    resized_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # 使用YOLO模型对缩放后的图像进行目标检测
    # results 是检测结果的列表，每个元素对应一帧的检测结果
    results = model(resized_frame)

    # 绘制检测结果
    # results[0] 表示第一帧的检测结果
    # plot() 方法将检测框、标签等信息绘制到图像上
    annotated_frame = results[0].plot()

    # 显示带有检测结果的图像
    # 窗口标题为 "YOLOv11 Detection"
    cv2.imshow("YOLOv11 Detection", annotated_frame)

    # 检测键盘输入
    # 如果按下 'q' 键，退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
# 关闭摄像头连接
cap.release()

# 关闭所有OpenCV创建的窗口
# 清理资源
cv2.destroyAllWindows()