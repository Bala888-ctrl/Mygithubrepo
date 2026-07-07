# 1. Grab a tiny box that already has Python 3.10 installed
FROM python:3.10-slim

# 2. Set the working directory inside the box
WORKDIR /app

# 3. Copy our application files into the box
COPY app.py .
COPY test_app.py .

# 4. Tell the box what to do when it opens
CMD ["python", "app.py"]