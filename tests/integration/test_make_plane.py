from . import TestBase
import make_plane

from mock import Mock, patch    # noqa
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class TestMakePlane(TestBase):
    def test_make_plane(self):
        """
        Test that everything works fine when we supply
        the right parameters
        """
        result = make_plane.make_plane(wheels=6, motors=4, length=30)
        self.assertTrue(result)

    def test_make_plane_validation_errors(self):
        """
        Simulate validation errors in make_plane()
        """
        stdout = StringIO()

        wheels = 30
        motors = 80
        length = 200

        with patch('sys.stdout', stdout):
            result = make_plane.make_plane(wheels, motors, length)

        self.assertFalse(result)

        output = [line.strip() for line in stdout.getvalue().splitlines()]
        self.assertIn('[make_plane] Max number of wheels is 16', output)
        self.assertIn('[make_plane] Max number of motors is 8', output)
        self.assertIn('[make_plane] Max length is 80', output)

    def test_make_plane_build_errors(self):
        self.skipTest(reason='Not tested yet')
