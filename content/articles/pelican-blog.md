Title: 安装及配置 Pelican 博客
Category: Default
Date: 2020-01-02
Tags: pelican, blog
Authors: Master
Summary: 如何安装 pelican 博客，并发布在 GitHub Page 上。
Cover: https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/JuniperPhoton_2020-01-02_12-00-00.jpg
Thumbnail: https://raw.githubusercontent.com/tengshan2008/tengshan2008.github.io/master/images/JuniperPhoton_2020-01-02_12-00-00.jpg

# Pelican

Pelican 是一种静态博客生成器，包含大量丰富的主题，拥有简单的部署方法。

## 1. 准备工作

为了发布在 GitHub Page 上，需要先新建一个远程仓库 username.github.io 并将该仓库克隆到本地。

``` shell
git clone https://github.com/{username}/{username}.github.io.git blog
```

由于 Pelican 默认发布 master 分支下的内容，所以，我们将 pelican 项目放到其他分支中。

``` shell
git checkout -b source
```

## 2. 安装

### 2.1 新建 python 虚拟环境

``` shell
cd blog

python -m venv .venv

source .venv/bin/activate
```

### 2.2 安装必要的 python 包

``` shell
python -m pip install pelican markdown ghp-import
```

版本信息：

| Package         | Version |
| --------------- | ------- |
| blinker         | 1.4     |
| docutils        | 0.15.2  |
| feedgenerator   | 1.9     |
| ghp-import      | 0.5.5   |
| Jinja2          | 2.10.3  |
| Markdown        | 3.1.1   |
| MarkupSafe      | 1.1.1   |
| pelican         | 4.2.0   |
| pip             | 19.3.1  |
| Pygments        | 2.5.2   |
| python-dateutil | 2.8.1   |
| pytz            | 2019.3  |
| setuptools      | 42.0.2  |
| six             | 1.13.0  |
| Unidecode       | 1.1.1   |
| wheel           | 0.33.6  |

## 3. 配置

### 3.1 新建 pelican 项目

``` shell
pelican-quickstart
```

### 3.2 填写必要信息

因为我们要在 GitHub Pages 上使用博客，所以 Do you want to upload 中只在 GitHub Pages 选择 [y]。其他选项根据自己的实际情况填写。

``` txt
Welcome to pelican-quickstart v4.2.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Blog Title
> Who will be the author of this web site? Blog Author
> What will be the default language of this web site? [zh] en
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) y
> What is your URL prefix? (see above example; no trailing slash) https://username.github.io
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Asia/Shanghai
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /home/pi/workspace/temp
```

### 3.3 安装主题

新建主题目录

> 注意：pelican-themes 中包含的众多主题，光是 clone 下来是不行的，会有许多空目录，因为许多主题都是 git submodule，所以需要 submodule update 来更新。  
> 同时，这些主题有的已经不适用于 4.2 版本，需要自己对主题进行部分修补，详见 [LINK](https://github.com/getpelican/pelican/pull/2538#issue-257357843)

``` shell
git submodule add https://github.com/onur/medius.git themes/medius

git submodule init

git submodule update --init --recursive

pelican-themes --install themes/medius
```

修改配置文件

``` shell
vim pelicanconf.py
```

添加以下内容

``` python
THEME = 'themes/medius'
```

## 4. 创建内容

在 content 目录下，存放博客文章及各类资源。

``` txt
website
├── content
│   ├── category
│   │   └── article1.rst
│   ├── article2.md
│   ├── pages
│   │   └── about.md
│   └── images
│       └── author.png
└── pelicanconf.py
```

若有静态资源目录，须在配置文件中定义。

``` shell
vim pelicanconf.py
```

添加以下内容

``` python
STATIC_PATHS = ['images']
```

编辑内容参照本博客文章自身。

## 5. 调试与部署

### 5.1 本地调试

``` shell
source .venv/bin/activate

make html && make serve
```

本地服务启用，访问 [http://localhost:8000](http://localhost:8000)

若是需要，提交所有内容。

``` shell
git add -A && git commit -a -m 'initial commit' && git push --all
```

### 5.2 部署在 GitHub Pages 上

``` shell
source .venv/bin/activate

make github
```

## 6. 参考

1. [Create a github hosted Pelican blog with a Bootstrap3 theme](https://a-slide.github.io/blog/github-pelican)
2. [A Pelican Tutorial: Static, Python-Powered Blog with Search & Comments](https://snipcart.com/blog/pelican-blog-tutorial-search-comments)

