FROM python:3.10-slim
WORKDIR /app

# Install cron
RUN apt-get update && apt-get install -y cron

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script and the cron runner script
COPY elt_pipeline.py .
COPY run-cron.sh .

#RUN ln -s /usr/local/bin/python3 /usr/local/bin/python

# Make the shell script executable
RUN chmod +x run-cron.sh

# Set the entrypoint to the shell script
CMD ["./run-cron.sh"]
