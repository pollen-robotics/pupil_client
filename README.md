# Pupil Client Library

[![Build Status](https://travis-ci.org/pollen-robotics/pupil_client.svg?branch=master)](https://travis-ci.org/pollen-robotics/pupil_client)

[Pupil-labs device](https://pupil-labs.com) client library. It retrieves the gaze 3d point from the [Pupil Remote](https://docs.pupil-labs.com/#network-plugins) software and its associate timestamp. The library works asynchronously.

It works on Python >=2.7 & >=3.3.

## Installation

The library can be installed via pip:

```bash
$ (sudo) pip install pupil_client
```

It can also be build from the source. It depends on:
* [pyzmq](https://github.com/zeromq/pyzmq)
* [msgpack](https://github.com/msgpack/msgpack-python)

## Getting Started

First, make sure to setup your Pupils-labs and Pupil remote correctly. Make sure to follow the [official documentation](https://docs.pupil-labs.com). Once you have calibrated your setup and your the Pupil Remote plugin is setup, you can use *pupil_client* as follows:

```python
import time

from pupil_client import PupilClient

# Use the IP where Pupil Remote is running
# The default port is 50020 but you can change it in Pupil Remote
pupil = PupilClient('192.168.0.29', 50020)

# Wait for pupil client to actually receive data from the server.
while not pupil.ready:
    time.sleep(0.1)
print('Pupil Client ready!')

while True:
    # Reads gaze 3d point and timestamp (done asynchronously).
    (x, y, z) = pupil.gaze.pt3d
    timestamp = pupil.gaze.t

    print('Gaze point 3d: {} (at t={})'.format([x, y, z], timestamp)
    time.sleep(1)
```

## License

This project is licensed under the BSD-3.
