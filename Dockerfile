FROM python:3.11-slim

WORKDIR /app

# 🧩 先安装 MySQL 开发依赖 + 编译工具
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt /app/

# 安装 Python 依赖
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . /app/

EXPOSE 8000

# 默认启动命令（适配 Django）
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
