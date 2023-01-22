---
title: "真假李宜婷 FALDetector的应用与教程"
subtitle: ""
date: 2023-01-13T13:44:52+08:00
draft: false
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: "本文是基于论文 Detecting Photoshopped Faces by Scripting Photoshop 的复现与使用，原始团队在 GitHub 上公布了代码，我们可以非常简单的在本地部署。你好奇你的小伙伴们有没有 PS 自己的照片吗？"
keywords: "FALDetector"
license: ""
comment: false
weight: 0

tags:
- AI
categories:
- Tutorials
- Sharing
  - Projects

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "本文是基于论文 Detecting Photoshopped Faces by Scripting Photoshop 的复现与使用，原始团队在 GitHub 上公布了代码，我们可以非常简单的在本地部署。你好奇你的小伙伴们有没有 PS 自己的照片吗？"
resources:
- name: featured-image
  src: featured-image.jpg
- name: featured-image-preview
  src: featured-image-preview.jpg

toc:
  enable: true
math:
  enable: false
lightgallery: true
seo:
  images: []

repost:
  enable: true
  url: ""

# See details front matter: https://fixit.lruihao.cn/theme-documentation-content/#front-matter
---

## 前言

本文是基于论文 Detecting Photoshopped Faces by Scripting Photoshop 的复现与使用，原始团队在 GitHub 上公布了代码，我们可以非常简单的在本地部署。

标题有些吸引眼球的意思了，看上去似乎是个社会学文章，其实是技术文章。

不过社会学的也在做就是了。

## 论文

**Detecting Photoshopped Faces by Scripting Photoshop [[Project Page]](http://peterwang512.github.io/FALdetector) [[Paper]](https://arxiv.org/abs/1906.05856)**

[Sheng-Yu Wang<sup>1</sup>](https://peterwang512.github.io/), [Oliver Wang<sup>2</sup>](http://www.oliverwang.info/), [Andrew Owens<sup>1</sup>](http://andrewowens.com/), [Richard Zhang<sup>2</sup>](https://richzhang.github.io/), [Alexei A. Efros<sup>1</sup>](https://people.eecs.berkeley.edu/~efros/). <br>
UC Berkeley<sup>1</sup>, Adobe Research<sup>2</sup>. <br>
In [ICCV, 2019](https://arxiv.org/abs/1906.05856).

### (A) Acknowledgments

This repository borrows partially from the [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix), [drn](https://github.com/fyu/drn), and the PyTorch [torchvision models](https://github.com/pytorch/vision/tree/master/torchvision/models) repositories. 

### (B) Citation, Contact

If you find this useful for your research, please consider citing this [bibtex](https://peterwang512.github.io/FALdetector/cite.txt). Please contact Sheng-Yu Wang \<sheng-yu_wang at berkeley dot edu\> with any comments or feedback.

## 部署

介于代码已经开源，使用它并不复杂

### Windows

在 Windows 上面部署，和在 Linux 上差不多，只有一点点不同。

#### Anaconda Shell

首先我们需要安装 [Anaconda](https://www.anaconda.com/)，这一过程没什么困难的，就跳过了。

之后打开 Anaconda Prompt (anaconda3)

{{< image src="anaconda3CLIIcon.webp" caption="Anaconda 3" width="300px" >}}

就会出现一个CMD窗口

```bash
(base) C:\Users\James>
```

不过它默认用的是 Windows 默认的 cmd.exe，

我不是很喜欢，我用的是 WezTerm。

所以需要一点额外操作，

这个 Anaconda Prompt (anaconda3) 快捷方式是以下内容

```bash
%windir%\System32\cmd.exe "/K" C:\Users\James\anaconda3\Scripts\activate.bat C:\Users\James\anaconda3
```

有两种选择，

一个是修改快捷方式里的，

```bash
%windir%\System32\cmd.exe "/K"
```

或者在WezTerm里执行

```bash
C:\Users\James\anaconda3\Scripts\activate.bat C:\Users\James\anaconda3
```
{{< image src="anaconda3WezTeamAnacondaBase.webp" caption="Anaconda 3 WezTerm" width="400px" >}}

效果是差不多的。

我们之后的命令都需要在这里面操作，当报错的时候请检查是不是在 Anaconda Prompt (anaconda3) 里进行的。

#### Anaconda Channels

在国内访问默认的源可能有些慢和不稳定，我们可以使用清华大学的镜像

这样通过如下命令添加

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```

设置搜索时显示通道地址，这样可以方便我们发现有没有正确配置源

```bash
conda config --set show_channel_urls yes
```

#### Environment

之后我们需要在 Anaconda 里创建一个虚拟环境，这里取名为`FALD`。

```bash
conda create -n FALD python=3.6
```

这一步可能会消耗一点时间，

它会安装一些必要组件，conda 询问时记得同意,

输入`yes` + Enter。

在完成之后，我们再进入`FALD`

```bash
conda activate FALD
```

记住，往后我们每次要对 FALdetector 进行操作的时候都要进入这个环境。

#### Work Path

之后我们需要按照论文里的指示，配置环境

首先，需要拉取源码，位于 [GitHub FALdetector](https://github.com/PeterWang512/FALdetector)

不过我为大家准备了处理好的版本，位于 [FALdetector]()

这是因为，你需要人工下载两个东西，一个是模型，一个是测试集。

原文提供了两个脚本

- download_weights.sh
- download_valset.sh

不过 Shell 脚本在 Windows 上并不好配置，我们只能手动下载了。

如果你有动手能力，那也可以手动地把这两个东西下到位。

或者使用我这个放好了的版本。

```txt
https://drive.jamesflare.com/api/v3/file/get/86171/FALdetector.7z?sign=aErdfOxvXdZH89kAhthihQm1DsC4E3qnDunWXgApHLU%3D%3A0
```

新建一个文件夹，然后在放入解压的文件之前，

启用 Windows 区分大小写功能

```bash
fsutil.exe file SetCaseSensitiveInfo 文件夹位置 enable
```

这是保险起见，不做应该也没问题，

请在一个新的 CMD 窗口以管理员执行。

下载后我们解压到那个启用 Windows 区分大小写功能的文件夹，

这里我放到桌面。

之后我们需要进入我们解压好的FALdetector目录，

在这里是`C:\Users\James\Desktop\FALdetector`

```bash
cd C:\Users\James\Desktop\FALdetector
```

不出意外你的输出应该类似于

```bash
(FALD) C:\Users\James\Desktop\FALdetector>
```

#### Requirements

接下来我们需要配置一下依赖，

在用 pip 安装的时候，我选择了使用镜像来加速

使用以下参数

```bash
-i https://pypi.tuna.tsinghua.edu.cn/simple
```

注意，需要在环境`FALD`下操作

安装 cmake

```bash
pip install cmake -i https://pypi.tuna.tsinghua.edu.cn/simple
```

和一些其他包
- dlib
- mmcv
- scipy
- numpy
- matplotlib
- opencv_python
- Pillow
- torch>=0.4.0
- torchvision

```bash
conda install dlib
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
pip install mmcv scipy numpy matplotlib opencv_python Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 运行

所有准备工作已经就绪。

项目拥有两个程序

- global_classifier.py
- local_detector.py

global_classifier.py 用于给出概率，输出类似

```txt
Probibility being modified by Photoshop FAL: 98.82%
```

使用方法为

```bash
python global_classifier.py --input_path "输入文件" --model_path weights/global.pth
```

示例

```bash
(FALD) C:\Users\James\Desktop\FALdetector>python global_classifier.py --input_path "examples/sampleVivanLi (13).jpg" --model_path weights/global.pth

Probibility being modified by Photoshop FAL: 2.72%
```

local_detector.py 用于生成热力图，

使用方法为

```bash
python local_detector.py --input_path "输入文件" --model_path weights/local.pth --dest_folder 输出目录
```

示例

```bash
(FALD) C:\Users\James\Desktop\FALdetector>python local_detector.py --input_path "examples/sampleVivanLi (154).jpg" --model_path weights/local.pth --dest_folder out/
```

然后我们就可以在 out 文件夹下找到生成的三张图片了

{{< image src="heatmapVivanLi154.webp" caption="Vivan Li 154 Heatmap" width="400px" >}}

第一张是 dlib 识别并裁切的人像，也是 FALdetector 的输入文件，

第二张是 FALdetector 生成的热力图，体现了 AI 对光流场的预测，显示了潜在的篡改区域，

第三张是 FALdetector 基于预测结果，尝试对图像进行的还原。

根据我的观察，他们有些很准，有些还是比较困难，颜色，像素，光照都很影响结果。

仅供参考

## 额外

额外我还找了个叫 Asshiteru 的人的图像，这是其中一张

```txt
(FALD) C:\Users\James\Desktop\FALdetector>python global_classifier.py --input_path "examples/aishiteruSample (36).jpg" --model_path weights/global.pth

Probibility being modified by Photoshop FAL: 97.92%
```

```txt
(FALD) C:\Users\James\Desktop\FALdetector>python local_detector.py --input_path "examples/aishiteruSample (36).jpg" --model_path weights/local.pth --dest_folder out/36/
```

{{< image src="heatmapAsshiteru36.webp" caption="Asshiteru 36 Heatmap" width="400px" >}}

两个完整例子可从下方下载

```txt
//FALDVivanLi.zip
https://drive.jamesflare.com/api/v3/file/get/86172/FALDVivanLi.zip?sign=ca-b00_d0GbBn40HsBG3v8IaZTY2KlmsW0R-ZLLFpr8%3D%3A0

//FALDAsshiteru.zip
https://drive.jamesflare.com/api/v3/file/get/86170/FALDAsshiteru.zip?sign=9G5oCp9uapNbUvmOeyih87HxR2Dz_t3PUx64tcvnyqE%3D%3A0
```

## 总结

这无疑给我们提供了一个全新的视角，在此之前我认为 Vivan 的图像应该大部分是被篡改过的，但是现在我改变主意了。

330 个样本里，拥有明显痕迹的也就 20+。

87%+ 以上都是几乎原图，这与我们的主观严重不符。

或许很少有人会有把一个人 300+ 张图像放在一起观察的机会，

但是对我而言，依然有数张图像我认为是非常好看的，比如 Sample13，而且 Probibility being modified by Photoshop FAL 的值非常低。

可见，PS 技术可能并没有起到确定性作用，更多的还是构图和摄影技术。

Asshiteru，我对她是谁，几乎没有概念。

不过，她超过半数的图像都有明显的篡改痕迹，听说她挺有名的。

小巫见大巫了，属于是。

## 缺点

这个项目是 Adobe 资助的，3 年了，他们也没有放出模型训练的细节和源码，可能有一些商业的考量在里面吧。

带来的结果就是有不少局限性。

比如对色彩不敏感，对轮廓很敏感。

就是说，美白，磨皮，大概率是对结果没有影响的。而且在这些例子里，诸如瘦脸，增大眼睛等功能也没有很激进，于是乎对判别也有挑战。

还有对脸以外的区域也没有判别力。

## 预告

我们爬取了 Instagram 上一部分，30 位博主，大约 22,000 张图像，一个更大样本的社会学研究，测试正在进行。