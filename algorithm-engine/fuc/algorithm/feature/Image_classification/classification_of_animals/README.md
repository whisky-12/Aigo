# []()Image_classification/classification_of_animals/main.py

[![img](https://img.shields.io/badge/python-%3E=3.8.x-green.svg)](https://python.org/)


💡 **「关于」**

这是使用 **ResNet-vd** 卷积神经网络, ResNet-vd是ResNet 原始结构的变种，可用于图像分类和特征提取,本模型采用百度自建动物数据集训练得到，支持7978种动物的分类识别


## 准备工作
```
Python >= 3.8.0 (推荐3.8+版本) 
```

## 运行💈

```bash
1. 进入fuc/algorithm/feature/Image_classification/classification_of_animals目录
2. 在独立虚拟环境安装依赖
	pip3 install -r requirements.txt
3. 执行脚本
	python main.py --imagePath=https://www.xxxx.com/xxx.png --top_k=xxx
4.参数
    imagePath[str]:[必要项]图片路径
    use_gpu[bool]:[非必要项]是否使用 GPU加速推理,目前阶段默认False, **若使用GPU,请先设置CUDA_VISIBLE_DEVICES环境变量**
    top_k (int):[非比要项] 返回预测图片中的前 k 个结果,默认为1个,建议对需求进行讨论后调整
	
```

## 结果

```
返回一个字典res (list[dict]) 菜品名称 ：预测改菜品的准确率
{'醉排骨': 0.23897601664066315, '荔枝肉': 0.06515346467494965}
当前默认top_k=1时 只返回概率最高的结果
{'醉排骨': 0.23897601664066315}
 
```