# Python assessment

This is a project with task templates.

## Tasks

### Detector

Implement [an application](detector) that analyzes detection data and alerts if a presence is detected during the
restricted time. The application consists of following parts to be implemented:
* [a configuration](detector/src/config.py)

  The configration defines the restricted time and other parameters (if required).
* [detection data producer](detector/src/data.py)

  The producer generates data by the following cyclic pattern and puts it to the queue: 2 minutes the presence is
  detected, 2 minute the presence is not detected.
* [detector](detector/src/detector.py)

  The detector receives data from the queue and analyzes it.
* [alert manager](detector/src/alert.py)

  The alert manager receives an alert and logs it.
