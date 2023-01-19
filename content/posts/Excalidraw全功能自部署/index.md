---
title: "Excalidraw全功能自部署"
subtitle: ""
date: 2023-01-13T15:54:36+08:00
draft: false
author: "James"
authorLink: "https://jamesflare.com"
authorEmail: "jamesflare1212@gmail.com"
description: ""
keywords: ""
license: ""
comment: false
weight: 0

tags:
- Open Source
- JavaScript
categories:
- Tutorials

hiddenFromHomePage: false
hiddenFromSearch: false

summary: "讲如何全栈部署Excalidraw"
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

## Intro

这可能是中文互联网上唯一一篇讲如何全栈部署Excalidraw的，绝大多数只是部署了一个残血的前端。

本人试图在本地私有化部署Excalidraw，操作是很简单，根据官方的README，一会就完成了是吧。

### Issue

但是有没有发现，分享链接和在线协作有问题，用不了？甚至Libraries还有点问题？

这是因为，几乎全网的搭建教程都只是搭建了excalidraw-app这个前端，它的存储需要excalidraw-json，协作需要excalidraw-room。

这些代码官方都开源了，不过前端的进度实在是太快了，于是乎这些就都用不了了。

比如官方开放的excalidraw-json是S3的存储，现在不出意外是firebase，官方也没出个剥离的版本，那我们怎么办呢？

### Solution

答，**降级**，**构建全栈**。

excalidraw-app我们用官方的，不过版本差不多是9个月前的，讲道理，功能也没少多少，bug也没什么问题，这一代前端可以很好兼容。

excalidraw-json是用不得了，国外也有一些方案用minio来跑S3对接它，但是我测试了，问题有些大，这个后端应该是用不得了，所幸的是，我找到了一个第三方，用自己代码实现的全功能后端，支持v2的api，excalidraw-storage-backend。

excalidraw-room我们用官方的，最新一版，差不多是9个月前的，和前端一致，可以正常使用。

redis，这个是excalidraw-storage-backend所需要的，用于临时存储分享画板的数据，所以它不能保证数据可靠性。

那我们开始吧，本方案使用docker-compose。

- excalidraw-app
- excalidraw-room
- excalidraw-storage-backend
- redis

## Operation

Docker Compose配置

```yaml
version: "3.8"

services:
  excalidraw:
    image: kiliandeca/excalidraw
    healthcheck:
      disable: true
    ports:
      - "80:80" # 默认端口80，可以修改
    environment:
      BACKEND_V2_GET_URL: http://localhost:8080/api/v2/scenes/
      BACKEND_V2_POST_URL: http://localhost:8080/api/v2/scenes/
      LIBRARY_URL: https://libraries.excalidraw.com
      LIBRARY_BACKEND: https://us-central1-excalidraw-room-persistence.cloudfunctions.net/libraries
      SOCKET_SERVER_URL: http://localhost:5000/
      STORAGE_BACKEND: "http"
      HTTP_STORAGE_BACKEND_URL: "http://localhost:8080/api/v2"

  excalidraw-storage-backend:
    image: kiliandeca/excalidraw-storage-backend
    ports:
      - "8080:8080"
    environment:
      STORAGE_URI: redis://redis:6379

  excalidraw-room:
    image: excalidraw/excalidraw-room
    ports:
      - "5000:80"

  redis:
    image: redis
    ports:
      - "6379:6379"
```

本身不支持https，如有需要可以通过反向代理实现，不过记得同时修改environment中的变量

此配置文件经本地测试通过，可完美运行。

{{< image src="excalidrawLocalDemo.webp" >}}

---

如果你6379端口有冲突，那可以选择构建一个network

```bash
docker network create excalidraw-net
```

然后像这样对其进行一些修改，就完成了

```yaml
version: "3.8"

services:
  excalidraw:
    image: kiliandeca/excalidraw
    healthcheck:
      disable: true
    ports:
      - "80:80"
    environment:
      BACKEND_V2_GET_URL: http://localhost:8080/api/v2/scenes/
      BACKEND_V2_POST_URL: http://localhost:8080/api/v2/scenes/
      LIBRARY_URL: https://libraries.excalidraw.com
      LIBRARY_BACKEND: https://us-central1-excalidraw-room-persistence.cloudfunctions.net/libraries
      SOCKET_SERVER_URL: http://localhost:5000/
      STORAGE_BACKEND: "http"
      HTTP_STORAGE_BACKEND_URL: "http://localhost:8080/api/v2"

  excalidraw-storage-backend:
    image: kiliandeca/excalidraw-storage-backend
    ports:
      - "8080:8080"
    environment:
      STORAGE_URI: redis://redis:6379

  excalidraw-room:
    image: excalidraw/excalidraw-room
    ports:
      - "5000:80"

  redis:
    image: redis
    expose:
      - "6379"

networks:
  default:
    external:
      name: excalidraw-net
```

## Run

找一个，或者新建一个目录，创建docker-compose文件

```bash
nano docker-compose.yml
```

填入docker-compose配置，记得按你的实际情况修改。

随后我们要配置一下反向代理，我的Web Server是OpenLiteSpeed，其他的同理。

首先需要创建External App，类型是Web Server，一共三个，分别对应

- excalidraw
- excalidraw-room
- excalidraw-storage-backend

名字可以相对应，下面三个是必填的，可以参考我的配置

|Setting|Value|
|-|-|
|Max Connections|2000|
|Initial Request Timeout (secs)|60|
|Retry Timeout (secs)|0|

地址端口对应docker-compose中的。

随后我们需要创建一个Vitrual Host，以下供参考

|Setting|Value|
|-|-|
|Virtual Host Name|excalidraw|
|Virtual Host Root|excalidraw|
|Config File|conf/vhosts/$VH_NAME/vhconf.conf|
|Max Keep-Alive Requests|20000|
|Follow Symbolic Link|Yes|
|Enable Scripts/ExtApps|Yes|
|Restrained|Yes|
|Enable GZIP Compression|Yes|
|Enable Brotli Compression|Yes|

在创建Vitrual Host之前你需要在/usr/local/lsws下创建一个目录

```bash
mkdir /usr/local/lsws/excalidraw
```

然后完成引导选项，不知道怎么填的话可以参考上面的参数。

也可以参照[OpenLiteSpeed：从入门到放弃-荒岛 (lala.im)](https://lala.im/6991.html)

我们就可以去Rewrite里配置了，添加如下Rewrite Rules

```txt
RewriteCond %{SERVER_PORT} ^80$
RewriteRule .* https://%{SERVER_NAME}%{REQUEST_URI} [R=301,L]

RewriteEngine on
RewriteRule /api/(.*) http://excalidraw-storage-backend/api/$1 [P]
RewriteRule /socket.io/(.*) http://excalidraw-room/socket.io/$1 [P]
RewriteRule /(.*) http://excalidraw/$1 [P,L]
```

完事后记得在Rewrite Control里开启，Enable Rewrite设置为Yes，不然就白给了。

```txt
RewriteCond %{SERVER_PORT} ^80$
RewriteRule .* https://%{SERVER_NAME}%{REQUEST_URI} [R=301,L]
```

我在重写规则中加入了如上配置，这是自动跳转https，如果你没有https的需要，记得修改。

还记得一个问题吗，excalidraw-room用websocket实现实时通信，我们也需要让它支持websocket。

在OpenLiteSpeed中，它有一个专门的项。去到Web Socket Proxy，新建一条

```txt
URL /socket.io/
Address 127.0.0.1:<你设置的excalidraw-room端口>
```

接下来设置好域名，到General设置，SSL如有需要也可以去SSL项设置。

最后记得在Listener里把Virtual Host加上。

## Ending

### Stack

{{< image src="stackDrawing.webp">}}

## Addtional

不要被我这里的OpenLiteSpeed搞混了，用Nginx什么的本质上没区别，搞对结构即可。