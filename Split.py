import os  # 导入操作系统模块，用于处理文件和目录路径
import shutil  # 导入文件操作模块，用于复制文件
import random  # 导入随机模块，用于打乱数据顺序

# random.seed(0)  # 设置随机种子，确保每次运行代码时随机结果一致（可选）

def split_data(file_path, label_path, new_file_path, train_rate, val_rate, test_rate):
    """
    划分数据集为训练集、验证集和测试集
    :param file_path: 图片文件夹路径
    :param label_path: 标签文件夹路径
    :param new_file_path: 新数据集存放路径
    :param train_rate: 训练集比例
    :param val_rate: 验证集比例
    :param test_rate: 测试集比例
    """
    # 获取图片文件夹中的所有文件
    images = os.listdir(file_path)
    # 获取标签文件夹中的所有文件
    labels = os.listdir(label_path)

    # 将图片文件名（去掉扩展名）和完整文件名存入字典
    images_no_ext = {os.path.splitext(image)[0]: image for image in images}
    # 将标签文件名（去掉扩展名）和完整文件名存入字典
    labels_no_ext = {os.path.splitext(label)[0]: label for label in labels}

    # 匹配图片和标签文件，生成一个元组列表，每个元组包含文件名（无扩展名）、图片文件名、标签文件名
    matched_data = [(img, images_no_ext[img], labels_no_ext[img]) for img in images_no_ext if img in labels_no_ext]

    # 检查未匹配的图片文件
    unmatched_images = [img for img in images_no_ext if img not in labels_no_ext]
    # 检查未匹配的标签文件
    unmatched_labels = [label for label in labels_no_ext if label not in images_no_ext]

    # 如果有未匹配的图片文件，打印提示信息
    if unmatched_images:
        print("未匹配的图片文件:")
        for img in unmatched_images:
            print(images_no_ext[img])
    # 如果有未匹配的标签文件，打印提示信息
    if unmatched_labels:
        print("未匹配的标签文件:")
        for label in unmatched_labels:
            print(labels_no_ext[label])

    # 打乱匹配后的数据顺序
    random.shuffle(matched_data)
    # 计算总数据量
    total = len(matched_data)

    # 划分训练集、验证集和测试集
    train_data = matched_data[:int(train_rate * total)]  # 训练集
    val_data = matched_data[int(train_rate * total):int((train_rate + val_rate) * total)]  # 验证集
    test_data = matched_data[int((train_rate + val_rate) * total):]  # 测试集

    # 处理训练集
    for img_name, img_file, label_file in train_data:
        # 原始图片路径
        old_img_path = os.path.join(file_path, img_file)
        # 原始标签路径
        old_label_path = os.path.join(label_path, label_file)
        # 新图片存放目录
        new_img_dir = os.path.join(new_file_path, 'train', 'images')
        # 新标签存放目录
        new_label_dir = os.path.join(new_file_path, 'train', 'labels')
        # 创建新目录（如果不存在）
        os.makedirs(new_img_dir, exist_ok=True)
        os.makedirs(new_label_dir, exist_ok=True)
        # 复制图片到新目录
        shutil.copy(old_img_path, os.path.join(new_img_dir, img_file))
        # 复制标签到新目录
        shutil.copy(old_label_path, os.path.join(new_label_dir, label_file))

    # 处理验证集
    for img_name, img_file, label_file in val_data:
        # 原始图片路径
        old_img_path = os.path.join(file_path, img_file)
        # 原始标签路径
        old_label_path = os.path.join(label_path, label_file)
        # 新图片存放目录
        new_img_dir = os.path.join(new_file_path, 'val', 'images')
        # 新标签存放目录
        new_label_dir = os.path.join(new_file_path, 'val', 'labels')
        # 创建新目录（如果不存在）
        os.makedirs(new_img_dir, exist_ok=True)
        os.makedirs(new_label_dir, exist_ok=True)
        # 复制图片到新目录
        shutil.copy(old_img_path, os.path.join(new_img_dir, img_file))
        # 复制标签到新目录
        shutil.copy(old_label_path, os.path.join(new_label_dir, label_file))

    # 处理测试集
    for img_name, img_file, label_file in test_data:
        # 原始图片路径
        old_img_path = os.path.join(file_path, img_file)
        # 原始标签路径
        old_label_path = os.path.join(label_path, label_file)
        # 新图片存放目录
        new_img_dir = os.path.join(new_file_path, 'test', 'images')
        # 新标签存放目录
        new_label_dir = os.path.join(new_file_path, 'test', 'labels')
        # 创建新目录（如果不存在）
        os.makedirs(new_img_dir, exist_ok=True)
        os.makedirs(new_label_dir, exist_ok=True)
        # 复制图片到新目录
        shutil.copy(old_img_path, os.path.join(new_img_dir, img_file))
        # 复制标签到新目录
        shutil.copy(old_label_path, os.path.join(new_label_dir, label_file))

    # 打印提示信息
    print("数据集已划分完成")


if __name__ == '__main__':
    # 图片文件夹路径
    file_path = r"D:\Desktop\Yolov11Project\data\JPEGImages"
    # 标签文件夹路径
    label_path = r'D:\Desktop\Yolov11Project\data\labels'
    # 新数据集存放路径
    new_file_path = r"D:\Desktop\Yolov11Project\data\VOCdevkit"
    # 调用函数划分数据集
    split_data(file_path, label_path, new_file_path, train_rate=0.8, val_rate=0.1, test_rate=0.1)