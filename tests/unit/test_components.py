import six
from . import TestBase
import components   # noqa

if six.PY2:
    from mock import Mock, patch    # noqa
else:
    from unittest.mock import Mock, patch   # noqa


class TestComponents(TestBase):
    def test_make_wheels(self):
        self.skipTest(reason='Not tested yet')
