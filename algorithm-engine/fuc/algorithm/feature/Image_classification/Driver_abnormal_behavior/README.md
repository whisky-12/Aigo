# []()Driver_abnormal_behavior/main.py

[![img](https://img.shields.io/badge/python-%3E=3.8.x-green.svg)](https://python.org/)


💡 **「关于」**

这是使用 **MobileNetV3_small_ssld** 模型算法, 可挖掘出驾驶人在疲劳状态下的表情特征，然后将这些定性的表情特征进行量化。最后输入获取到的状态数据进行识别和判断,
识别驾驶员行驶途中，是否存在不同类型的危险驾驶状态。



## 准备工作
```
Python >= 3.8.0 (推荐3.8+版本) 
```

## 运行💈

```bash
1. 进入fuc/algorithm/feature/Image_classification/Driver_abnormal_behavior目录
2. 在独立虚拟环境安装依赖
	pip3 install -r requirements.txt
3. 执行脚本
	python DriverStatusRecognition.py --imagePath=https://www.xxxx.com/xxx.png
4.参数
    imagePath[str]:[必要项]图片路径
```

## 结果

```
返回一个字典{"key":"value"):事件 ： 预测改事件的准确率
{'右手接打电话': 0.9999925}
 
```