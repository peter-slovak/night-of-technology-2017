import six
from . import TestBase
import make_plane   # noqa

if six.PY2:
    from mock import Mock, patch    # noqa
else:
    from unittest.mock import Mock, patch   # noqa


class TestMakePlane(TestBase):
    def test_make_plane(self):
        self.skipTest(reason='Not tested yet')
