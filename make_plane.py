"""
The top-level public interface for making planes.

We can specify the number of wheels, motors and plane
length. The main function will try to obtain all the necessary
components which in turn need to obtain materials.
"""
from __future__ import print_function

import argparse
import components
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    '-w', '--wheels',
    type=int,
    default=8,
    help='Number of wheels for our plane, default 8',
)
parser.add_argument(
    '-m', '--motors',
    type=int,
    default=2,  # we are eco-friendly
    help='Number of motors for our plane, default 2',
)
parser.add_argument(
    '-l', '--length',
    type=int,
    default=40,
    help='Length of planes in meters, default 40',
)


def make_plane(wheels, motors, length):
    """
    Make a plane by getting necessary components and putting them
    together. Perform some sanity checks first, of course.

    :param wheels: Number of wheels
    :param motors: Number of motors
    :param length: Plane length
    :return: bool
    """
    log_prefix = '[make_plane] '
    max_wheels = 16
    max_motors = 8
    max_length = 80

    validation_passed = True
    if wheels > max_wheels:
        print(log_prefix + 'Max number of wheels is %s' % max_wheels)
        validation_passed = False
    if motors > max_motors:
        print(log_prefix + 'Max number of motors is %s' % max_motors)
        validation_passed = False
    if length > max_length:
        print(log_prefix + 'Max length is %s' % max_length)
        validation_passed = False

    if not validation_passed:
        return False

    build_successful = True
    body = components.make_body_and_wings(length)
    windows = components.make_windows(4 * length)   # 4 windows per meter of plane
    wheels = components.make_wheels(wheels)
    motors = components.make_motors(motors)

    if not body:
        print('Failed to get plane body from manufacturers')
        build_successful = False
    if not windows:
        print('Failed to get windows from manufacturers')
        build_successful = False
    if not wheels:
        print('Failed to get wheels from manufacturers')
        build_successful = False
    if not motors:
        print('Failed to get motors from manufacturers')
        build_successful = False

    return build_successful


if __name__ == '__main__':
    args = parser.parse_args()
    success = make_plane(args.wheels, args.motors, args.length)

    if success:
        print('Your plane is ready! Parameters: %s wheels, %s motors, %s meters length'
              % (args.wheels, args.motors, args.length))

    sys.exit(int(not success))      # 0 if success, 1 if not success
