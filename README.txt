# Efficient Data Stream Anomaly Detection

## Overview

This project implements a Python script for detecting anomalies in a continuous data stream.

## Files

- `DataDetection.py`: Script implementing the anomaly detection algorithm.
- `DataGeneration.py`: Script for generation the data stream.
- `Visualization.py`: Main script for visualization of the data stream and anomalies.
- `requirements.txt`: Lists the required Python libraries.
- `README.md`: This documentation file.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/17andreafranco/DataAnomalyDetection.git
   ```

2. **Install Dependencies:**

   Ensure you have Python 3.x installed. Install the necessary libraries using:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Simulate Data Stream:**

   Run the data stream simulation script:

   ```bash
   python DataGeneration.py
   ```

   This will start generating a data stream.

2. **Detect Anomalies:**

   Run the anomaly detection script:

   ```bash
   python DataDetection.py
   ```

   This script will process the simulated data stream and detect anomalies in real-time.

3. **Visualize Data and Anomalies:**

   Run the visualization script:

   ```bash
   python Visualization.py
   ```

   This will open a window displaying the real-time data stream and any detected anomalies.

## Algorithm

PyOD:

The project uses PyOD, a comprehensive Python library for detecting outlying objects in multivariate data.
For this project, we use the Isolation Forest algorithm provided by PyOD.

## Data Validation

Anomalous data points are flagged based on the PyOD model’s predictions.

## Dependencies

The project requires the following Python libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `pyod`

These libraries are listed in the `requirements.txt` file.

