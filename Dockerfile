# 使用官方 Python 轻量级镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装（如果你的项目有 requirements.txt）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制项目所有文件到容器的工作目录
COPY . .

# 声明运行时容器提供服务端口
# 注意：微信云托管部署时填写的端口必须与此处保持一致
EXPOSE 5000

# 配置环境变量
ENV FLASK_APP=app.py

# 指定容器启动时运行的命令
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

