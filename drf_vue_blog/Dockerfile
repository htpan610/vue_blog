FROM python:3.6
ENV PYTHONUNBUFFERED 1

# 添加这两行
# 使用了清华源之后，会造成安装python3-dev时产生依赖关系
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev -y

RUN mkdir /code
WORKDIR /code
RUN pip install pip -U
ADD requirements.txt /code/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ADD . /code/