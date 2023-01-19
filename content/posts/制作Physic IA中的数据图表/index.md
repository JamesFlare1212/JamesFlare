---
title: "制作Physic IA中的数据图表"
subtitle: ""
date: 2023-01-16T14:14:32+08:00
draft: false
author: "James"
authorLink: "https://jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: ""
keywords: ["Excel","Physic IA","Internal Assessment"]
license: ""
comment: false
weight: 0

tags:
- Excel
categories:
- Tutorials

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "使用Excel绘制满足IB Physic IA的数据图表"
resources:
- name: featured-image
  src: featured-image.jpg
- name: featured-image-preview
  src: featured-image-preview.jpg

toc:
  enable: true
math:
  enable: true
lightgallery: true
seo:
  images: []

repost:
  enable: true
  url: ""

# See details front matter: https://fixit.lruihao.cn/theme-documentation-content/#front-matter
---

## Introduction

在写Physic IA（Internal Assessment）[^10]的时候，大家可能发现数据图表的评分挺复杂。

你需要不少的内容才能获得满分数据图表[^9]，

- The Best Line of Fit for the Data Points
- The Mathematical Relationship Between your two Variables
- The Numerical Value of Gradient
- The Numerical Value of Intercept
- The Correlation Coefficient

不过也并不是非常困难，我们使用Excel就能完成这个任务。

[^9]: 此内容来源于 [引用1](https://www.gradepod.com/blog/the-exact-structure-and-subtitles-you-should-use-in-your-ib-physics-internal-assessment)
[^10]: IA的全称是Internal Assessment

***

明确一下我们要在Excel里绘制的内容，

- 离散图（Scatter）
- 数据点（Plot Markers）
- X轴标签（X Axis Title）
- Y轴标签（X Axis Title）
- 图标题（Graph Title）
- 误差框（Error Bar）
- 最贴合曲线（Best Fit Line）
- 最差贴合上限曲线（Max Fit Line）
- 最差贴合下限曲线（Min Fit Line）
- 曲线的公式（Equations）

至此就翻译成一个ICT方面的任务了。

## Excel

### Graph Type

首先要明确应该使用哪种图表。通常是离散图（Scatter），这种图表会将所有数据标注在图表上。

## Example Data

那我们随便用个例子做讲解吧，

|Try 1|Try 1|Try 2|Try 2|Try 3|Try 3|
|:----|:----|:----|:----|:----|:----|
|Temperature / ℃ ±5|Time / s ±2|Temperature / ℃ ±5|Time / s ±2|Temperature / ℃ ±5|Time / s ±2|
|4|3|6|7|2|1|
|9|10|11|15|9|11|
|10|15|12|21|10|15|
|14|24|16|31|12|27|
|16|30|18|35|17|30|
|21|41|23|39|18|35|
|22|45|22|45|22|44|
|26|55|24|55|21|45|
|28|60|28|60|26|50|
|30|62|30|65|26|55|
|32|70|34|75|30|67|
|34|75|37|81|32|70|
|38|86|38|84|34|75|
|40|90|40|90|36|81|
|42|94|42|94|42|94|
|44|99|44|99|45|100|

在这个例子里，实验重复了三次（实际中可能不够，我们只做一个演示）。

且定实验的目的是证明某个东西的温度变化和时间成正比例，$Temperature \propto Time$，也就是我们最后应该得到一个Linear的图像。

## Example Scatter

这是最终的成品效果，

{{< image src="example.svg" width="100%" caption="Example Scatter" >}}

那我们来看看是如何一步一步制作的吧。

## How to Make

接下来我将逐步演示，从头到尾构建此图表的过程。

### Import Data

Check List，到现在为止，我们完成了，

- [ ] **离散图（Scatter）**
- [ ] 数据点（Plot Markers）
- [ ] X轴标签（X Axis Title）
- [ ] Y轴标签（X Axis Title）
- [ ] 图标题（Graph Title）
- [ ] 误差框（Error Bar）
- [ ] 最贴合曲线（Best Fit Line）
- [ ] 最差贴合上限曲线（Max Fit Line）
- [ ] 最差贴合下限曲线（Min Fit Line）
- [ ] 曲线的公式（Equations）

本节让我们准备操作，**离散图（Scatter）**。

***

首先我们需要把数据导入Excel，

{{< image src="enterDataIntoExcel.webp" width="100%" caption="Enter Data Into Excel" >}}

这其实不太讲究，实在不行一个一个手打也行，这里我用[Example Data](#example-data)里的数据。

再次提醒，在真实的IA中，建议有5次重复的实验的数据，3次可能不够，我们这里只是演示ICT技术用，无需过多要求。

可能会好奇，这里有多列数据怎么办？一种方法是把他们重新组织合并成两列，但是这样有多列也不要紧，我选择的方法是第二种，选择数据源`Data Source`的时候指定多列，这部分在后面有详细讲述。

### Insert Scatter Graph

Check List，到现在为止，我们完成了，

- [ ] **离散图（Scatter）**
- [ ] 数据点（Plot Markers）
- [ ] X轴标签（X Axis Title）
- [ ] Y轴标签（X Axis Title）
- [ ] 图标题（Graph Title）
- [ ] 误差框（Error Bar）
- [ ] 最贴合曲线（Best Fit Line）
- [ ] 最差贴合上限曲线（Max Fit Line）
- [ ] 最差贴合下限曲线（Min Fit Line）
- [ ] 曲线的公式（Equations）

本节让我们操作，**离散图（Scatter）**。

***

选一个对的图表类型是很重要的，绝大多数情况我们需要的是Scatter（离散图）。

{{< image src="insertScatterGraph.webp" width="100%" caption="Insert Scatter Graph" >}}

选好图表类型，点`OK`确认。

{{< image src="rawScatterGraph.webp" width="100%" caption="Raw Scatter Graph" >}}

现在差不多应该是这样的一个画面。

看到有点不对劲是吧，怎么花花绿绿，而且关键的元素怎么都没有，不急，慢慢来。

### Config Best Fit Data

Check List，到现在为止，我们完成了，

- [x] 离散图（Scatter）
- [ ] **数据点（Plot Markers）**
- [ ] X轴标签（X Axis Title）
- [ ] Y轴标签（X Axis Title）
- [ ] 图标题（Graph Title）
- [ ] 误差框（Error Bar）
- [ ] 最贴合曲线（Best Fit Line）
- [ ] 最差贴合上限曲线（Max Fit Line）
- [ ] 最差贴合下限曲线（Min Fit Line）
- [ ] 曲线的公式（Equations）

本节让我们操作，**数据点（Plot Markers）**。

***

首先我们需要让图表读取正确的数据集，

{{< image src="selectScatterGraphData.webp" width="100%" caption="Select Scatter GraphData" >}}

我们右键图表，选择`Select Data`选择数据。

{{< image src="selectScatterGraphDataSource.webp" width="100%" caption="Select Scatter Graph Data Source" >}}

`Select Data Source`选择数据源界面是帮助我们标定所需绘制的数据的。

可以看到原先是自动把3组数据分成了3个分离的`Series`集。而我们希望它们都在一个`Series`里，这样就拥有统一的颜色。

首先点击`Remove`移除原先的所有数据集，然后我们选择`Add`添加。

{{< image src="selectScatterGraphDataSourceForX.webp" width="100%" caption="Select Scatter Graph Data Source For X" >}}

它会询问你`Series`名，`Series X Values`,`Series Y Values`。

这里我希望X轴是时间，Y轴是温度。注意的是，选择多个Table时可以按住`Ctrl`按键，框选多个列表。MacOS可能是`Command`键。你也可以选择手动整合多个列表。每个Sheet之间用`,`作为分割。其实在你使用`Ctrl`多选时，Excel自动帮你做好了这件事。

```txt
=(Sheet1!$B$3:$B$18,Sheet1!$D$3:$D$18,Sheet1!$F$3:$F$18)
```

这是Example中所用的表达公式。可以看见，结构是，

```txt
=(列表1,列表2,列表3)
```

大家在操作时注意就好，当报错时记得回头检查。

{{< image src="selectScatterGraphDataSourceForY.webp" width="100%" caption="Select Scatter Graph Data Source For Y" >}}

对于`Series Y Values`，操作是接近的。

不过有一点，默认会有一个`={1}`的值，如果不删掉直接在后方添加会导致错误，请注意。

{{< image src="checkSelectedScatterGraphDataSource.webp" width="100%" caption="Check Selected Scatter Graph Data Source" >}}

到这，3个项`Series`名，`Series X Values`,`Series Y Values`都填写好了。

`Series`名是可选的，但是为了方便区分，还是建议大家填一个。

{{< image src="checkSelectedScatterGraphData.webp" width="100%" caption="Check Selected Scatter Graph Data" >}}

这是完成后的样子。

完成一定要点`OK`确认，不然就白忙活了。

### Config Error Bars

Check List，到现在为止，我们完成了，

- [x] 离散图（Scatter）
- [x] 数据点（Plot Markers）
- [ ] X轴标签（X Axis Title）
- [ ] Y轴标签（X Axis Title）
- [ ] 图标题（Graph Title）
- [ ] **误差框（Error Bar）**
- [ ] 最贴合曲线（Best Fit Line）
- [ ] 最差贴合上限曲线（Max Fit Line）
- [ ] 最差贴合下限曲线（Min Fit Line）
- [ ] 曲线的公式（Equations）

本节让我们操作，**误差框（Error Bar）**。

***

添加误差框不是一件难事，一种办法是从`Chart Design`，`Add Chart Element`中添加

{{< image src="makeErrorBarForBestFitLine.webp" width="100%" caption="Make Error Bar for Best Fit Line" >}}

选择`Standard Error`。这时可能发现它们的尺寸不太对，不要紧。

{{< image src="changeXErrorBar.webp" width="100%" caption="Select X Error Bar" >}}

点击图表中的误差线打开菜单。如果没到正确的地方，可以手动选择，这里我们先处理X轴方向的误差框。

{{< image src="changeXErrorBarFixedValue.webp" width="100%" caption="Config X Error Bar Fixed Value" >}}

X轴在Example中是Time时间，Time时间的误差范围我们先前在表格中有体现（省去数值）。

|Temperature / ℃ ±5|Time / s ±2|
|:-------------------:|:-----------:|
|\<Value\>|\<Value\>|

Time的误差为±2，这里为了效果定了一个很高的数值，实际不是这样的。

***

{{< admonition type=note title="提醒" open=true >}}
接下来很长一段都是讲述Uncertainties​的内容，如果你自认为完全理解，那么可以跳过，直接到Error Bar设置部分。
{{< /admonition >}}

这可能是要经过计算的，我想这在正常的IB Physic课程中有所讲述，

> Topic 1: Measurement and Uncertainties​

如果不确定，那我们简述一下。

***

首先，误差分为三种。

> Absolute Uncertainty: $\Delta x$
> 
> Fractional Uncertainty: $\cfrac{\Delta x}{x}$
> 
> Percentage Uncertainty: $\cfrac{\Delta x}{x} \times 100 \\%$

我们日常能碰到的基本上就是，

> Absolute Uncertainty: $\Delta x$
>
> Percentage Uncertainty: $\cfrac{\Delta x}{x} \times 100 \\%$

如果我的数据是计算出来的，比如我实验测电流（$I$）[^3]和电压（$V$）[^4]，但是我图表要绘制功率（$P$）[^5]。那么功率（$P$）的Error Bar要怎么绘制呢？

***

这种情况需要先算出功率（$P$）的误差（Uncertainty）。

[^2]: 误差的英文是 Uncertainty
[^3]: 电流的物理符号是 $I$
[^4]: 电压的物理符号是 $V$
[^5]: 功率的物理符号是 $P$

功率为 $P = IV$ [^7]，其是两个数值相乘。

[^7]: 功率的计算公式之一是：电流 $\times$ 电压

> **Addition/Subtraction**
> 
> Form: $y = a \pm b$
> 
> Uncertainty: $\Delta y = \Delta a + \Delta b$ (sum of absolute uncertainties)
>
> ***
> 
> **Multiplication/Division**	
> 
> Form: $y = a \times b$ or $y = \cfrac{a}{b}$
> 
> Uncertainty: $\cfrac{\Delta y}{y} = \cfrac{\Delta a}{a} + \cfrac{\Delta b}{b}$ (sum of fractional uncertainties)
>
> ***
> 
> **Power**
> 
> Form: $y = a^n$
> 
> Uncertainty: $\cfrac{\Delta y}{y} = \| n \| \bigg( \cfrac{\Delta a}{a} \bigg)$ (\|n\| times of fractional uncertainty)

这样的话就属于**Multiplication/Division**，重新构造一下公式，把我们的 $P = IV$ 纳入。

这样就得到了 $\cfrac{\Delta P}{P} = \cfrac{\Delta I}{I} + \cfrac{\Delta V}{V}$。

***

接下来我们得到 $\Delta I$ 和 $\Delta V$ 就可以算出 $\Delta P$ 了。而这两个的值一般取决于仪表，如果制造商没有标注，那就是最后一位读数的精度。不过有些例外，比如实验中是通过人来掐秒表计时，那么公认的人类反应时间是200毫秒，即使秒表再精准，也不该使用标注值，应该使用 $\pm 200 ms $ 作为Uncertainty。永远**使用最不准的一个来作为衡量**。

注意，制造商可能会标注 $\pm 1 \\%$ 这样的数值，那么它本身就是Percentage Uncertainty，直接把它转换为Fractional Uncertainty即可，还记得上方的 $\cfrac{\Delta P}{P} = \cfrac{\Delta I}{I} + \cfrac{\Delta V}{V}$ 吗？它的RHS[^1]中，每一个项和上面展示的Fractional Uncertainty公式 $\cfrac{\Delta x}{x}$ 完全一样。如果不明白两个之间是怎么转换的，为什么就可以直接用了？那么想想，我们说的百分比%，是不是就是百分之几，$\cfrac{x}{100}$ 的意思？

同时也不要搞混了，$\Delta x$ 的意思是 $x$ 的变化，比如 $+ 1$，$- 1$ 或者 $\pm 1$。而 $\pm 1 \\%$ 显然不能算数。

[^1]: RHS（Right Hand Side）

***

假设我们使用的电流表的标注是 $\pm 1 \\%$（这在现实中不太可能发生，为了演示）。同时假设电压表没有标注，但是它是数字式的，某个读数长这样 $1145.14 V$，那么它的Uncertainty就是 $\pm 0.01 A$。

最后假设现在某一组数据的值是 $I = 2.01$，$V = 1.51$，通过 $P = IV$ 得到 $P = 3.0351$。这显然是不正确的，因为有效数字位数（Significant Figures）[^6]，和精度都对不上。换一句话说，它缺少误差（Uncertainty）。

要算出Uncertainty，把内容带入公式，得到 $\cfrac{\Delta P}{3.0351} = \cfrac{1}{100} + \cfrac{0.01}{1.51}$。如果你计算正确的话，就会得到 $\Delta P = 0.05045$。但是不能直接写 $P = 3.0351 \pm 0.05045 W$，这样是不对的，因为有效数字（Significant Figures）的位数不正确。

[^6]: 有效数字位数的英文为 Significant Figures

***

这我就简单讲述一下规则，

首先，**读数的精度不能高于误差**

看起来是废话，其实我是说，类似 $11.4514 \pm 0.1$ 这样的情况是不能出现的。

因为 11.4514 的精度是 0.0001，而误差是 0.1，这显然是不可接受的。修正一下就是 $11.5 \pm 0.1$。

其次，**误差只能有一位有效数字**

什么是有效数字？我这里暂时不会论述，因为会搞得文章过于杂乱，这应该在物理和数学中都有提及。

举个例子，$1145.14 \pm 0.114$ 这个写法就是错误的，因为 0.114 有三位有效数字（Significant Figures），修正一下应该是 $1145.14 \pm 0.1$。

然后发现这也不对，因为上面说过，读数的精度不能高于误差，于是再次修改 $1145.1 \pm 0.1$ 这就是最终结果。

如果一个结果两个问题都存在，那么按照以下顺序修正

1. 误差只能有一位有效数字
2. 读数的精度不能高于误差

回到上文的例子，结果 $P = 3.0351 \pm 0.05045 W$ 经过修正，会得到 $P = 3.04 \pm 0.05 W$，这便是正确的结果。

***

是不是兴奋地以为把 0.05 填到Excel里就万事大吉了？哈哈，小子，还没结束，希望心态别炸。

这只是一个数值，而画图用的是图表，显然我们不太能给每一个点设置Error Bar，所以我们用的是图表中，所有值的一个普遍的Uncertainty，也就是表格顶端所标注的。

|Temperature / ℃ ±5|Time / s ±2|
|:-------------------:|:-----------:|
|\<Value\>|\<Value\>|

在我的例子中，很简单，因为这两个数值是我测量得来的，而且是一个Absolute Uncertainty，直接照抄，搬入Excel的`Error Amount`，`Fixed Value`即可。可是如果我们的Uncertainty是一个Percentage Uncertainty，或者这个项是计算出来的，而非直接测量获得的。比如说上文举例的功率，它就是由两个原始测量值相乘获得的，这样每个数值的Absolute Uncertainty都不一样。那我们怎么确立，像Temperature / ℃ ±5中，±5一样的Uncertainty填入Excel中呢？

不急，我们可以先统计每一个数值的Absolute Uncertainty，再计算最大值和最小值之间的差，然后除以2，也就是所谓的Half Range。

什么意思呢，比如我有{1,1,2,3,1,4,2,4}这几个值，那它们的Half Range就是 $(4 - 1) \div 2 = 1.5$。

什么？你说我之前算一个 $P = 3.04 \pm 0.05 W$ 得到它 0.05 的Absolute Uncertainty就花了那么多功夫，我要是有几十，上百个数值岂不是要我命？非也非也，Excel可以轻松帮助你计算，当然这是ICT知识了，完全讲述一边又是一篇文章了，我就稍微给点思路，还是用刚才的功率计算为例。

随便创造一个数据

|Current / A ± 1%|Voltage / V ± 0.01|
|:----|:----|
|1.01|1.52|
|1.35|1.32|
|1.21|1.42|

接下来可以另起一列，定为功率的Uncertainty

|Current / A ± 1%|Voltage / V ± 0.01|Uncertainty for Power|
|:----|:----|:----|
|1.01|1.52| |
|1.35|1.32| |
|1.21|1.42| |

那么，我们的计算本质上是什么？是 $\cfrac{\Delta P}{P} = \cfrac{\Delta I}{I} + \cfrac{\Delta V}{V}$。重新构造一下，把我们要的 $\Delta P$ 挪至LHS[^8]。

[^8]: LHS（Left Hand Side）

这样就得到了 $\Delta P = \bigg(\cfrac{\Delta I}{I} + \cfrac{\Delta V}{V} \bigg) \times P$。

$\cfrac{\Delta I}{I}$，$I$，$\Delta V$ 和 $V$ 我们都可以从图表中获得，$P$ 可以由已知的 $I$ 和 $V$ 计算获得。

最后重新构造一下得到，$\Delta P = \bigg(\cfrac{\Delta I}{I} + \cfrac{\Delta V}{V} \bigg) \times (I \times V)$。

***

在Excel里，我们重新构造一下，就有了

```txt
=((1%)+(0.01/B2))*(A2*B2)
```

{{< image src="uncertaintyExcelExampleForPower.webp" width="500px" caption="Uncertainty Calculation for Power in Excel" >}}


这样的公式。

|Current / A ± 1%|Voltage / V ± 0.01|Uncertainty for Power|
|:----|:----|:----|
|1.01|1.52|0.025452|
|1.35|1.32|0.03132|
|1.21|1.42|0.029282|

是不是很简单啊。

***

继续我们的主题，接下来设置Y轴的Error Bar，先从菜单切换对象。

{{< image src="changeYErrorBar.webp" width="100%" caption="Change Y Error Bar" >}}

接下来和X轴的操作别无二致，设置好相关选项。

{{< image src="changeYErrorBarFixedValue.webp" width="100%" caption="Change Y Error Bar Fixed Value" >}}

这里我Temperature的Absolute Uncertainty是±5，设置`Fixed Value`为5，因为是±，所以方向是Both，这样就完成了。

### Add Axis Titles

Check List，到现在为止，我们完成了，

- [x] 离散图（Scatter）
- [x] 数据点（Plot Markers）
- [ ] **X轴标签（X Axis Title）**
- [ ] **Y轴标签（X Axis Title）**
- [ ] 图标题（Graph Title）
- [x] 误差框（Error Bar）
- [ ] 最贴合曲线（Best Fit Line）
- [ ] 最差贴合上限曲线（Max Fit Line）
- [ ] 最差贴合下限曲线（Min Fit Line）
- [ ] 曲线的公式（Equations）

本节让我们操作，**X轴标签（X Axis Title）**，**Y轴标签（X Axis Title）**。

***

首先我们添加两个轴标题的元素，

{{< image src="addAxisTitles.webp" width="100%" caption="Add Axis Titles" >}}

在这之后双击文本框修改其中的内容，包括样式，位置等。

{{< image src="changeAxisTitles.webp" width="100%" caption="Change Axis Titles" >}}

这样就完成了。

### Add Graph Title

Check List，到现在为止，我们完成了，

- [x] 离散图（Scatter）
- [x] 数据点（Plot Markers）
- [x] X轴标签（X Axis Title）
- [x] Y轴标签（X Axis Title）
- [ ] **图标题（Graph Title）**
- [x] 误差框（Error Bar）
- [ ] 最贴合曲线（Best Fit Line）
- [ ] 最差贴合上限曲线（Max Fit Line）
- [ ] 最差贴合下限曲线（Min Fit Line）
- [ ] 曲线的公式（Equations）

本节让我们操作，**图标题（Graph Title）**。

***

和修改轴标题一样简单，直接双击标题文本框修改。

{{< image src="changeGraphTitle.webp" width="100%" caption="Change Graph Title" >}}

如果没有标题文本框，那可以像添加轴标题一样添加图标题元素`Element`。

### Add Fit Line

Check List，到现在为止，我们完成了，

- [x] 离散图（Scatter）
- [x] 数据点（Plot Markers）
- [x] X轴标签（X Axis Title）
- [x] Y轴标签（X Axis Title）
- [x] 图标题（Graph Title）
- [x] 误差框（Error Bar）
- [ ] **最贴合曲线（Best Fit Line）**
- [ ] **最差贴合上限曲线（Max Fit Line）**
- [ ] **最差贴合下限曲线（Min Fit Line）**
- [ ] 曲线的公式（Equations）

本节让我们操作，**最贴合曲线（Best Fit Line）**，**最差贴合上限曲线（Max Fit Line）**，**最差贴合下限曲线（Min Fit Line）**。

***

在添加之前我们先要计算出Max Fit Line，Min Fit Line.

{{< image src="calculateMaxFitPoints.webp" width="100%" caption="Calculate Max Fit Points" >}}

我们可以理解为两个极值连接的一条曲线，而这条曲线是其中最陡峭的一个。

因为只要确定两点即可确定一条直线，我们只要算出那两个点即可。如果没理解的话我稍微列个表格，

**Max Fit Line**

|Series Y Values|Series X Values|
|:----|:----|
|Y Min - Absolute Uncertainty|X Min - Absolute Uncertainty|
|Y Max + Absolute Uncertainty|X Max + Absolute Uncertainty|

同理可得，

**Min Fit Line**

|Series Y Values|Series X Values|
|:----|:----|
|Y Min + Absolute Uncertainty|X Min + Absolute Uncertainty|
|Y Max - Absolute Uncertainty|X Max - Absolute Uncertainty|

{{< image src="addFitLineDataSource.webp" width="100%" caption="Add Fit Line Data Source" >}}

在算完两条线，四个点，八个值后，把这两组数据分别加入图表，可以参照[Config Best Fit Data](#config-best-fit-data)章节操作。

{{< image src="checkDataSource.webp" width="100%" caption="Check Data Source" >}}

操作完差不多是这样，记得按`OK`保存。

至此，我们的工作还未结束，因为现在一切东西都是数据点，并不是我们想要的曲线。

{{< image src="addTrendlines.webp" width="100%" caption="Add Trendlines" >}}

而添加曲线也很简单，Excel把它称作趋势线（Trendline）。

瞄准数据点右键，`Add Trendline`即可。

### Add Equations

Check List，到现在为止，我们完成了，

- [x] 离散图（Scatter）
- [x] 数据点（Plot Markers）
- [x] X轴标签（X Axis Title）
- [x] Y轴标签（X Axis Title）
- [x] 图标题（Graph Title）
- [x] 误差框（Error Bar）
- [x] 最贴合曲线（Best Fit Line）
- [x] 最差贴合上限曲线（Max Fit Line）
- [x] 最差贴合下限曲线（Min Fit Line）
- [ ] **曲线的公式（Equations）**

本节让我们操作，**曲线的公式（Equations）**。

{{< image src="configTrendlines.webp" width="100%" caption="Config Trendlines" >}}

点击曲线打开配置页面，把`Display Equation on chart`勾选上，这样就会显示曲线的公式了。

其余的选项，比如是线性（Linear），指数（Exponential）等就按自己需要了。我在一开始就假定这个例子是线性的关系，所以选`Linear`即可。

{{< image src="previewTrendlines.webp" width="100%" caption="Preview Trendlines" >}}

如法炮制，把剩下几个曲线也添加完，然后双击编辑公式的文本框，在它们前面加上标注。

顺手把底下不需要的Label删除。

### Ending Work

现在，所有必要工作已经完成，

- [x] 离散图（Scatter）
- [x] 数据点（Plot Markers）
- [x] X轴标签（X Axis Title）
- [x] Y轴标签（X Axis Title）
- [x] 图标题（Graph Title）
- [x] 误差框（Error Bar）
- [x] 最贴合曲线（Best Fit Line）
- [x] 最差贴合上限曲线（Max Fit Line）
- [x] 最差贴合下限曲线（Min Fit Line）
- [x] 曲线的公式（Equations）

在拿去用之前建议，

{{< image src="finalWork.webp" width="100%" caption="Final Work" >}}

调整一下颜色，字体，位置等美化一下。

这就是最终成品了，拥有所有我们要的元素，满分图表了。

## Source File

这是Excel原文件，可以拿去研究

{{< link href="example.xlsx" content="example.xlsx" title="Download example.xlsx" download="example.xlsx" card=true >}}

## Reference

1. [The EXACT Structure And Subtitles You Should Use In Your IB Physics Internal Assessment [Updated for 2023]](https://www.gradepod.com/blog/the-exact-structure-and-subtitles-you-should-use-in-your-ib-physics-internal-assessment)
2. [Topic 1: Measurement and uncertainties​](https://ibphysics.org/topic1/)