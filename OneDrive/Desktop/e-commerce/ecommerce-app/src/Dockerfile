FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 8080
CMD ["python", "-c", "from flask import Flask; app = Flask(__name__); @app.route('/')\ndef home(): return 'Hello from EKS Pod!'; app.run(host='0.0.0.0', port=8080)"]