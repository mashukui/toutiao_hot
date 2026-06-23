# 今日头条热榜爬虫/Toutiao Hot Board Crawler

> 基于Python3的今日头条热榜数据采集脚本，支持热榜标题、热度值、分类、标签和详情链接等核心字段导出。

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+"></a>
  <a href="https://pypi.org/project/requests/"><img src="https://img.shields.io/badge/requests-required-green.svg" alt="requests"></a>
  <a href="https://pypi.org/project/pandas/"><img src="https://img.shields.io/badge/pandas-required-orange.svg" alt="pandas"></a>
</p>

## 📖 项目简介

本项目是一个面向Python爬虫初学者的今日头条热榜采集示例。脚本通过请求今日头条PC端热榜接口，解析返回的JSON数据，并将热榜内容整理为CSV文件，方便后续用Excel、Python或其他数据分析工具处理。

源码结构简单，适合学习以下内容：

- 使用`requests`发送HTTP请求
- 解析接口返回的JSON数据
- 提取列表数据中的核心字段
- 使用`pandas`生成表格数据
- 将结果保存为CSV文件

## 🎬 运行演示

源码运行演示视频：[点击查看Bilibili演示视频](https://www.bilibili.com/video/BV1zw411e783/)

## ✨ 功能特点

- 无需登录账号，不依赖Cookie
- 自动抓取今日头条热榜数据
- 自动生成热榜排名
- 支持提取标题、热度值、标签、分类和链接
- 自动规范化部分热榜链接
- 保存为`UTF-8-SIG`编码的CSV文件，兼容Excel打开

## 📊 采集字段

| 字段 | 说明 | 示例 |
| --- | --- | --- |
| 热榜排名 | 当前热榜排序，从1开始 | 1 |
| 热榜标题 | 热榜事件或文章标题 | 姆巴佩梅开二度 |
| 热度值 | 平台返回的热度数值 | 11671729 |
| 热榜标签 | 平台返回的榜单标签 | hot |
| 热榜分类 | 平台返回的分类信息 | sports |
| 热榜链接 | 热榜详情页、文章页或直播页链接 | https://www.toutiao.com/trending/... |

## 📄 运行结果示例

脚本运行完成后，会在当前目录生成：

```text
头条热榜.csv
```

CSV示例：

| 热榜排名 | 热榜标题 | 热度值 | 热榜标签 | 热榜分类 |
| --- | --- | --- | --- | --- |
| 1 | 姆巴佩梅开二度 | 11671729 | hot | sports |
| 2 | 美股：纳指跌1.32% SpaceX跌超16% | 10561017 |  | finance |
| 3 | 近4000家外资企业追加在华投资 | 9556003 |  |  |

## 🚀 快速开始

### 环境要求

- Python3.8+
- Windows/macOS/Linux

### 安装依赖

```bash
pip install requests pandas
```

### 基本使用

```bash
python3 toutiao_hot.py
```

运行时终端会输出接口响应状态码、热榜数量和抓取到的热榜标题。运行完成后，采集结果会保存到`头条热榜.csv`。

## ⚙️ 核心原理

### 请求地址

```text
https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc
```

### 请求头

脚本只设置了基础`User-Agent`，不需要配置Cookie、Token或账号信息。

```python
h1 = {
    'User-Agent': 'Mozilla/5.0 ... Safari/605.1.15',
}
```

### 核心流程

1. 请求今日头条热榜接口
2. 使用`response.json()`解析接口数据
3. 遍历返回结果中的`data`列表
4. 提取`Title`、`HotValue`、`Label`、`InterestCategory`、`Url`等字段
5. 使用`pandas.DataFrame`整理数据
6. 导出为CSV文件

## 🎯 适用场景

- Python爬虫入门练习
- 热点事件观察
- 热榜数据归档
- CSV数据处理学习
- pandas表格生成示例

## ❓ 常见问题

### 运行后没有生成CSV怎么办？

先确认依赖是否安装成功：

```bash
pip install requests pandas
```

再确认当前目录是否有`toutiao_hot.py`，并在脚本所在目录运行命令。

### 为什么脚本突然报错？

热榜接口字段可能会发生变化。如果返回结构调整，脚本中读取字段的位置也需要同步修改。

### 是否需要Cookie？

当前脚本不需要Cookie。请不要把个人Cookie、Token、账号密码等敏感信息提交到公开仓库。

## ⚠️ 注意事项

- 请合理控制运行频率，避免对目标站点造成压力。
- 本项目仅用于学习研究，不建议用于商业采集或批量抓取。
- 接口可用性和字段结构可能随目标网站调整而变化。
- 使用本项目时，请自行遵守目标网站的服务条款、robots规则以及相关法律法规。

## 📌 免责声明

本项目仅供学习和研究使用。因使用本项目产生的任何问题或后果，由使用者自行承担。
