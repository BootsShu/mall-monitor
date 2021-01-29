FROM python:2.7.13

WORKDIR /usr/src/app

# COPY requirements.txt ./

RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple

RUN pip config set install.trusted-host mirrors.aliyun.com

COPY . .

RUN wget https://nodejs.org/dist/v12.16.1/node-v12.16.1-linux-x64.tar.xz && tar -xf node-v12.16.1-linux-x64.tar.xz -C /opt

ENV EXECJS_RUNTIME=$PATH:/opt/node-v12.16.1-linux-x64/bin

RUN ln -s /opt/node-v12.16.1-linux-x64/bin/node /usr/local/bin/

RUN ln -s /opt/node-v12.16.1-linux-x64/bin/npm /usr/local/bin/

RUN echo 'node 版本：' && node -v

RUN echo 'python 版本：' && python -V

RUN pip install --no-cache-dir -r requirements.txt

CMD  cd web && python server.py