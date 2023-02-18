---
slug: "go-sine-displayer"
title: "实践手册：使用 Go 语言显示 Sin 图像"
subtitle: ""
date: 2023-02-17T23:44:14+08:00
draft: true
author: "James"
authorLink: "https://www.jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: ""
keywords: ""
license: ""
comment: true
weight: 0

tags:
- Go
categories:
- Programing

hiddenFromHomePage: false
hiddenFromSearch: false

summary: ""
resources:
- name: featured-image
  src: featured-image.jpg
- name: featured-image-preview
  src: featured-image-preview.jpg

toc:
  enable: true
math:
  enable: false
lightgallery: false
seo:
  images: []

repost:
  enable: true
  url: ""

# See details front matter: https://fixit.lruihao.cn/theme-documentation-content/#front-matter
---

<!--more-->

## Instraction



## Instance

### Code

```go
package main

import (
    "math"
    "gonum.org/v1/plot"
    "gonum.org/v1/plot/plotter"
    "gonum.org/v1/plot/vg"
)

func main() {
    // Create a new plot
    p, err := plot.New()
    if err != nil {
        panic(err)
    }

    // Set the plot title and labels
    p.Title.Text = "Sin Graph"
    p.X.Label.Text = "X"
    p.Y.Label.Text = "Y"

    // Create a new plotter for the sin function
    points := make(plotter.XYs, 0)
    for i := 0; i <= 360; i += 10 {
        rad := float64(i) * math.Pi / 180
        points = append(points, plotter.XY{X: rad, Y: math.Sin(rad)})
    }

    line, err := plotter.NewLine(points)
    if err != nil {
        panic(err)
    }
    p.Add(line)

    // Save the plot to a PNG image file
    if err := p.Save(4*vg.Inch, 4*vg.Inch, "sin.png"); err != nil {
        panic(err)
    }
}
```

### Explain

This program uses the `math`, `gonum.org/v1/plot`, `gonum.org/v1/plot/plotter`, and `gonum.org/v1/plot/vg` packages to create and plot a sin graph.

The `math` package provides mathematical constants and functions, including `math.Pi` and `math.Sin`.

The `gonum.org/v1/plot` package provides a plotting library for Go, including functions to create and manipulate plots, as well as different types of plot elements.

The `gonum.org/v1/plot/plotter` package provides a set of basic types for data plotting, including `plotter.XYs` and `plotter.Line`.

The `gonum.org/v1/plot/vg` package provides a set of types to represent vector graphics, including the `vg.Inch` unit.

The program starts by creating a new plot using the `plot.New()` function. It then sets the plot title and labels using the `Title.Text`, `X.Label.Text`, and `Y.Label.Text` fields of the plot.

Next, it creates a new plotter for the sin function using a loop to calculate the sine values for different angles. It uses `plotter.XYs` to store the x and y values and `plotter.XY` to store each point. It then creates a `plotter.Line` with the points and adds it to the plot.

Finally, it saves the plot to a PNG image file using the `p.Save()` function.

The resulting PNG image file shows the sin graph, with the x-axis labeled "X" and the y-axis labeled "Y". The graph shows the sine function plotted against the angle in radians. The plot shows the sine wave oscillating between -1 and 1, with a period of 2π radians.