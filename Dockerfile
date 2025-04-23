FROM python:3.9-slim

WORKDIR /app

# Copy the departure timer script
COPY departure_timer.py ./

# Make the script executable
RUN chmod +x departure_timer.py

# Default entrypoint
ENTRYPOINT ["./departure_timer.py"]