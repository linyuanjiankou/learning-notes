> 区别于我以往写下的文章内容，这一片文章不讲述我从头到尾的学习过程，只记录一些我认为比较重要的、容易遗忘的一些知识点。
> 同时，由于本人较为薄弱的Python编程实力，本文章末尾会记录一些简单的 Python 调用模型的代码，方便查询和复现。
# 知识点
> 官方手册：https://docs.ultralytics.com/
## YOLO模型任务
YOLO 的实例模型包括以下几个分类：
- Detect 目标检测
- OBB 旋转目标检测
- Segment 实例分割
- Pose 姿态估计
- Classify 图像分类
## 模型大小
可以看到，在YOLO示例模型命名末尾，通常会跟着 `nsmlx` 这五个字母，这五个字母代表着该模型的大小，从小到大分别为：
- n - nano 纳米级 很小
- s - small 小
- m - medium 中
- l - large 大
- x - extra-large 超大
## 模型训练
### 数据集
用于模型训练的数据集包含三个部分，训练集、验证集和测试集，包含图片和标签；
整个训练过程就是不断向模型投喂训练集，再用验证集检测模型效果的训练验证循环过程；
测试集一般来说可有可无，用于量化模型最终的训练效果。
### 如何训练
需要准备三样东西，
其一，数据集本体，包含图片和标签的，按照一定格式整理好；
其二，数据集配置文件，以.yaml为后缀，为模型指向训练集和验证集位置；
其三，训练代码，指向数据集配置文件。
#### 数据集格式
一般来说，数据集格式有两种常见的文件结构：
第一，先区分任务 (train, valid, test)，再区分图片 (images) 和标签 (labels)；
第二，先区分图片 (images) 和标签 (labels)，再区分任务 (train, valid, test)。
#### 标签
一行有五个数字，
第一个整数代表物体类型，具体内容写在数据集配置文件中，标签文件只用数字代号；
以图片左上角建系，水平方向为x正半轴，垂直方向为y正半轴，长宽由图片长宽像素大小决定，
后面四个小数分别表示框的 中心点横坐标、中心点纵坐标、宽度、高度；
之所以使用小数，是因为该数值表示与图片像素的占比，中心点横坐标和宽度乘以图片宽度，中心点纵坐标和高度乘以图片长度，就可以得出来框的大小。
#### labelimg 可视化标签
需要提供三个东西的路径：图片文件夹、classes.txt（在标签文件夹内）、标签文件夹；
可视化指令：
```
labelimg 图片文件夹路径 classes文件路径 对应标签文件夹路径
```
#### 训练效率
- batch：批量，这个参数表示将多少张图片打包在一起投喂给模型，影响训练速度和一定程度的训练效果；
- imgsz：图片尺寸，图片需要先缩放再打包，这个参数决定图片需要放大还是缩小；
- cache：图片从硬盘到内存有一个加载过程，设置为 `"ram"` 的时候可以将图片全部从硬盘加载到内存并缩放，之后显存直接读取调用即可；
- workers：进程数，决定同时进行多少个打包进程（包括数据增强等处理）。
总而言之，调节不同参数使得cuda占用率又高又稳，GPU、内存等硬件占用率适当即可。
# 代码片段
### 对目标进行检测
```python
from ultralytics import YOLO

model = YOLO(r"yolo26n.pt")

model.predict(
    source=r"ultralytics/assets",
    save=True,
    show=False,
    # save_txt=True, # 将预测结果以txt的形式保存
)
```
> 更多推理参数及可视化参数见官方手册：https://docs.ultralytics.com/modes/predict
### 摄像头实时检测
```python
import cv2

from ultralytics import YOLO

model = YOLO(r"yolo26n.pt")

results = model(
    source=0,
    stream=True,
)

for result in results:
    plotted = result.plot()
    cv2.imshow("YOLO Inference", plotted)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```
> 说明：其实，第一个代码也可以使用摄像头进行实时检测，但是代价是数据全都存储在内存中（只show不save），这段代码就可以解决这种问题。

### 一些查询模型信息的代码
```python
from ultralytics import YOLO

model = YOLO(r"yolo26n.pt")
print(model.task) # 查询模型任务（detect等）
print(model.names) # 查询可识别物体类型
print(sum(p.numel() for p in model.parameters())) # 统计参数大小

```
### 模型训练代码
```python
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r"yolo26n.pt")

    model.train(
        data="coco8.yaml",
        epochs=10, #训练几轮
        batch=16,  #批
        imgsz=640, #图片尺寸
        workers=0, #工作者（进程）
        cache=False, #缓存
        # amp=False, 
        # val=False, #只训练不验证
    )
```