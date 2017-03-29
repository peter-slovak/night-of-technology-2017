"""
Most low-level functions that provide us with base building materials.

Each material may be obtained by various ways and it is only up to the
calling function to decide how.
"""
from __future__ import print_function

import random

# Define the amounts of available titanium for each quality level
TITANIUM_QUANTITY_BY_QUALITY = {
    'low': 1000,
    'normal': 100,
    'best': 50,
}


# TITANIUM
def mine_titanium(quantity=10, quality='best'):
    """
    Mine titanium.

    :param quantity: Tons of titanium we want to mine
    :param quality: Level of quality
    :return: tuple (bool, errormessage)
    """
    if quality not in TITANIUM_QUANTITY_BY_QUALITY.keys():
        return False, 'quality level "%s" not recognized' % quality

    available_qty = TITANIUM_QUANTITY_BY_QUALITY[quality]
    if quantity > available_qty:
        return False, 'Only %s tons of %s quality titanium available' % (available_qty, quality)

    return True, None


def reuse_titanium(quantity=10, quality='normal'):
    """
    Reuse old titanium.

    The 'best' quality can not be achieved, but on the other hand
    we have as much as we want.

    :param quantity: Tons of titanium we want to mine
    :param quality: Level of quality (low, normal)
    :return: tuple (bool, errormessage)
    """
    qualities = ['low', 'normal']
    if quality not in qualities:
        return False, 'Only these qualities are available from broken planes: %s' % qualities

    return True, None


# RUBBER
def harvest_rubber(quantity=5, elasticity='soft'):
    """
    Harvest rubber.

    Rubber is not a commodity, we mostly get as much as we pay for.
    Except when a natural disaster hits the region.

    :param quantity: Tons of rubber we want
    :param elasticity: soft/hard rubber
    :return: tuple (bool, errormessage)
    """
    # 5% chance of rubber unavailability
    if random.randint(1, 100) <= 5:
        return False, 'The rubber factory has been flooded'

    if elasticity not in ['soft', 'hard']:
        return False, 'Unknown elasticity: %s' % elasticity

    return True, None


def reuse_rubber(quantity=5, elasticity='hard'):
    """
    Reuse old rubber.

    Soft elasticity is not available because the rubber is old,
    but we can have as much as we want.

    :param quantity: Tons of rubber we want
    :param elasticity: only 'hard' available
    :return: tuple (bool, errormessage)
    """
    if elasticity != 'hard':
        return False, 'Unknown elasticity: %s' % elasticity

    return True, None


# GLASS
def make_glass(length=10, width=10, depth=0.1):
    """
    Make glass.

    Glass is also not a commodity, so we can always get as much as
    we pay for. The only downside is that glass may unexpectedly break
    at the end of the manufacturing pipeline.

    :param length: glass surface length in m
    :param width: glass surface width in m
    :param depth: glass surface thickness in cm (max 10)
    :return: tuple (bool, errormessage)
    """
    max_depth = 10
    if depth > max_depth:
        return False, 'Glass depth (thickness) maximum is %s cm' % max_depth

    # 2% chance of glass breakage
    if random.randint(1, 100) <= 2:
        return False, 'The glass has broken, but you still have to pay for it'

    return True, None


def reuse_glass(length=10, width=10, depth=0.1):
    """
    Resuse old glass.

    We have any surface shape available, but glass breakage chance is
    much higher.

    :param length: glass surface length in m
    :param width: glass surface width in m
    :param depth: glass surface thickness in cm (max 10)
    :return: tuple (bool, errormessage)
    """
    max_depth = 10
    if depth > max_depth:
        return False, 'Glass depth (thickness) maximum is %s cm' % max_depth

    # 20% chance of glass breakage
    if random.randint(1, 100) <= 20:
        return False, 'The glass has broken'

    return True, None
