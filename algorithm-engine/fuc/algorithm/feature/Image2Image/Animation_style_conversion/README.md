# []()algorithm/feature/Image2Image/Fusion_transformation/main.py

[![img](https://img.shields.io/badge/python-%3E=3.8.x-green.svg)](https://python.org/)


💡 **「关于」**

本模型StyleProNet整体采用全卷积神经网络架构(FCNs)，结合艺术风格迁移算法可以将给定的图像转换为任意的艺术风格
通过encoder-decoder重建艺术风格图片。
StyleProNet的核心是无参数化的内容-风格融合算法Style Projection，模型规模小，响应速度快。
模型训练的损失函数包含style loss、content perceptual loss以及content KL loss，
确保模型高保真还原内容图片的语义细节信息与风格图片的风格信息。


## 准备工作
```
Python >= 3.8.0 (推荐3.8+版本) 
```

## 运行💈

```bash
1. 进入fuc/algorithm/feature/Image2Image/Fusion_transformation/目录
2. 在独立虚拟环境安装依赖
	pip3 install -r requirements.txt
3. 执行脚本
	python main.py --content_imagePath=https://www.xxxx.com/xxx.png --styles_imagePath=https://www.xxxx.com/xxx.png
4.参数
    content_imagePath[str]:[必要项]基础图片路径
    styles_imagePath[str]:[必要项]期望风格图片路径
    use_gpu[bool]:[非必要项]是否使用 GPU加速推理,目前阶段默认False, **若使用GPU,请先设置CUDA_VISIBLE_DEVICES环境变量**
    alpha (float):画风融合权重, 默认0.5, 接口正在调整,现阶段暂不支持调整 
	
```

## 结果

```
输出结果图片的路径(str)

 
```