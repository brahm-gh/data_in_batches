# Environmental Sensor Data Batch Loader

This project loads environmental telemetry data into a MongoDB database using Docker.

### Dataset
The dataset https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset contains wind turbine sensor data including:

Wind speed
Power output
Wind direction
Timestamp


### Instructions

1. Start MongoDB container:

```bash
docker run -d --name mongo-db -p 27017:27017 mongo
```
2. Build and run the loader:
```bash
docker-compose up --build
```
