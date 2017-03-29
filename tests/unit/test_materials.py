import six
from . import TestBase
import materials    # noqa

if six.PY2:
    from mock import Mock, patch    # noqa
else:
    from unittest.mock import Mock, patch   # noqa


class TestMaterials(TestBase):
    def test_mine_titanium(self):
        self.skipTest(reason='Not tested yet')

    def test_reuse_titanium(self):
        pass

    def test_harvest_rubber(self):
        self.skipTest(reason='Not tested yet')

    def test_reuse_rubber(self):
        self.skipTest(reason='Not tested yet')

    def test_make_glass(self):
        self.skipTest(reason='Not tested yet')

    def test_reuse_glass(self):
        self.skipTest(reason='Not tested yet')
