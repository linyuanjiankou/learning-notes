> 区别于我以往写下的文章内容，这一片文章不讲述我从头到尾的学习过程，只记录一些我认为比较重要的、容易遗忘的一些知识点。
> 同时，由于本人较为薄弱的Python编程实力，本文章末尾会记录一些简单的 Python 调用模型的代码，方便查询和复现。
# 知识点
> 官方手册：https://docs.ultralytics.com/
### YOLO模型任务
YOLO 的实例模型包括以下几个分类：
- Detect 目标检测
- OBB 旋转目标检测
- Segment 实例分割
- Pose 姿态估计
- Classify 图像分类
### 模型大小
可以看到，在YOLO示例模型命名末尾，通常会跟着 `nsmlx` 这五个字母，这五个字母代表着该模型的大小，从小到大分别为：
- n - nano 纳米级 很小
- s - small 小
- m - medium 中
- l - large 大
- x - extra-large 超大
# 代码片段
### 对目标进行检测
```python
from ultralytics import YOLO

model = YOLO(r"yolo26n.pt")

model.predict(
    source=r"ultralytics/assets",
    save=True,
    show=False,
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