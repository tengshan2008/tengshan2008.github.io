Title: lucaslorentz/caddy-docker-proxy 简易教程
Category: Default
Date: 2020-01-13
Tags: docker, caddy
Author: Master
Summary: 如何使用 caddy-docker-proxy 实现反向代理
Cover: https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/JuniperPhoton_2020-01-13_12-00-00.jpg
Thumbnail: https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/JuniperPhoton_2020-01-13_12-00-00.jpg

# lucaslorentz/caddy-docker-proxy 简易教程

[GitHub](https://github.com/lucaslorentz/caddy-docker-proxy) [DockerHub](https://hub.docker.com/r/lucaslorentz/caddy-docker-proxy/)

## 1. 什么是 caddy-docker-proxy

使用 caddy 对 docker 网络进行代理。其本身也是一个 docker 容器。可以对当前 docker 网络中的容器做反向代理。实现子域名的绑定，同时网络服务容器不需要映射本地端口。

## 2. 下载镜像

``` shell
docker pull lucaslorentz/caddy-docker-proxy:latest
```

如果你是 arm 架构设备，例如树莓派，请使用其他镜像。

``` shell
docker pull lucaslorentz/caddy-docker-proxy:latest-arm32v6
```

## 3. 运行容器

容器开放 80, 443, 2015 端口用作反向代理。

``` shell
docker run --name caddy -d \
    -p 2015:2015 \
    -p 80:80 \
    -p 443:443 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    lucaslorentz/caddy-docker-proxy:latest-arm32v6 \
    -agree -email example@mail.com \
    -log stdout -docker-process-caddyfile
```

> -agree 表示同意 Let's Encrypt 的协议  
> -email 如果未在 Caddyfile 中指定用于 TLS 的邮箱，将使用此处的邮箱地址  
> -log 启用日志，输出在 stdout 中，通过 docker logs -f caddy 查看  
> -docker-process-caddyfile 不知道有啥用

## 4. 举例

运行一个 docker 容器网站。

``` shell
docker run --name=flask-website -d \
    -l caddy.address=example.com \
    -l caddy.targetport=8080 \
    -l caddy.proxy.transparent= \
    -l caddy.tls=example@mail.com \
    username/image:latest
```

caddy 的更多配置方法见 [GitHub](https://github.com/lucaslorentz/caddy-docker-proxy) 仓库

在 docker 网络中生成如下 Caddyfile 配置

``` Caddyfile
example.com {
  proxy / 172.17.0.7:8080 {
    transparent
  }
  tls example@mail.com
}
```

