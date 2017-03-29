"""
Middle-layer functions that collect base resources by any
means available and build a component we ask.
"""
from __future__ import print_function

import materials

# If we fail to buy a material from manufacturers, try to reuse
# some from old and broken planes
REUSE_MATERIALS_IF_NOT_AVAILABLE = True


def make_wheels(count):
    """
    Make wheels.

    :param count: Number of wheels
    :return: bool
    """
    log_prefix = '[components.make_wheels] '

    # Get rubber
    rubber = materials.harvest_rubber(quantity=count, elasticity='hard')

    if not rubber[0] and REUSE_MATERIALS_IF_NOT_AVAILABLE:
        print(log_prefix + 'could not harvest rubber, attempting reuse: %s' % rubber[1])
        rubber = materials.reuse_rubber(quantity=count, elasticity='hard')

    if not rubber[0]:
        print(log_prefix + 'rubber not available: %s' % rubber[1])
        return False

    # Get titanium
    titanium = materials.mine_titanium(quantity=count, quality='normal')

    if not titanium[0] and REUSE_MATERIALS_IF_NOT_AVAILABLE:
        print(log_prefix + 'could not mine titanium, attempting reuse: %s' % titanium[1])
        titanium = materials.reuse_titanium(quantity=count, quality='low')

    if not titanium[0]:
        print(log_prefix + 'titanium not available: %s' % titanium[1])
        return False

    return True


def make_windows(count):
    """
    Make windows.

    :param count: Number of windows
    :return: bool
    """
    log_prefix = '[components.make_windows] '

    # Get glass
    glass = materials.make_glass()

    if not glass[0] and REUSE_MATERIALS_IF_NOT_AVAILABLE:
        print(log_prefix + 'could not make glass, attempting reuse: %s' % glass[1])
        glass = materials.reuse_glass()

    if not glass[0]:
        print(log_prefix + 'glass not available: %s' % glass[1])
        return False

    return True


def make_body_and_wings(body_length):
    """
    Make motors.

    :param body_length: Body length
    :return: bool
    """
    log_prefix = '[components.make_body_and_wings] '

    # Get titanium
    titanium = materials.mine_titanium(quantity=body_length, quality='best')

    if not titanium[0] and REUSE_MATERIALS_IF_NOT_AVAILABLE:
        print(log_prefix + 'could not mine titanium, attempting reuse: %s' % titanium[1])
        titanium = materials.reuse_titanium(quantity=body_length, quality='normal')

    if not titanium[0]:
        print(log_prefix + 'titanium not available: %s' % titanium[1])
        return False

    return True


def make_motors(count):
    """
    Make motors.

    :param count: Number of motors
    :return: bool
    """
    log_prefix = '[components.make_motors] '

    # Get titanium
    titanium = materials.mine_titanium(quantity=count, quality='best')

    if not titanium[0] and REUSE_MATERIALS_IF_NOT_AVAILABLE:
        print(log_prefix + 'could not mine titanium, attempting reuse: %s' % titanium[1])
        titanium = materials.reuse_titanium(quantity=count, quality='best')

    if not titanium[0]:
        print(log_prefix + 'titanium not available: %s' % titanium[1])
        return False

    return True
