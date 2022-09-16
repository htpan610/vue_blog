# 从仓库拉取带有python的Linux环境 https://hub.docker.com/
FROM python:3.10
# 设置python环境变量，设置为1代表python程序的output实时输出到屏幕
ENV PYTHONUNBUFFERED 1
# 在容器里创建code文件夹并设置为工作目录
RUN mkdir /code
WORKDIR /code
# 更新pip
RUN pip install pip -U
# 将requirements.txt 复制到容器的code目录
ADD requirements.txt /code/
# 安装库
RUN pip install -r requirements.txt
# 将当前目录复制到code目录
ADD . /code/