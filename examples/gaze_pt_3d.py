import time

from pupil_client import PupilClient


if __name__ == '__main__':
    # Use the IP where Pupil Remote is running
    # The default port is 50020 but you can change it in Pupil Remote
    pupil = PupilClient('192.168.0.29', 50020)

    # Wait for pupil client to be synced with the remote
    while not pupil.ready:
        time.sleep(0.1)
    print('Pupil Client ready!')

    while True:
        # Reads gaze 3d point and timestamp (done asynchronously).
        (x, y, z) = pupil.gaze.pt3d
        ttimestamp = pupil.gaze.t

        print('Gaze point 3d: {} (at t={})'.format([x, y, z], timestamp)
        time.sleep(1)
