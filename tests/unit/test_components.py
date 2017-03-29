from . import TestBase
import components

from mock import Mock, patch
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class TestComponents(TestBase):
    def test_make_wheels(self):
        wheel_count = 4

        # Case 1 - everything OK on the first try
        stdout = StringIO()
        with \
                patch('materials.harvest_rubber', Mock(return_value=(True, None))) as harvest_rubber_patch,\
                patch('materials.mine_titanium', Mock(return_value=(True, None))) as mine_titanium_patch,\
                patch('sys.stdout', stdout):
            result = components.make_wheels(wheel_count)

        self.assertTrue(result)

        harvest_rubber_patch.assert_called_once()
        harvest_rubber_patch.assert_called_with(quantity=wheel_count, elasticity='hard')

        mine_titanium_patch.assert_called_once()
        mine_titanium_patch.assert_called_with(quantity=wheel_count, quality='normal')

        # Case 2 - rubber and titanium are reused
        stdout = StringIO()
        rubber_message = 'No more rubber'
        titanium_message = 'Titanium unavailable'
        with \
                patch('materials.harvest_rubber', Mock(return_value=(False, rubber_message))) as harvest_rubber_patch,\
                patch('materials.mine_titanium', Mock(return_value=(False, titanium_message))) as mine_titanium_patch,\
                patch('materials.reuse_rubber', Mock(return_value=(True, None))) as reuse_rubber_patch,\
                patch('materials.reuse_titanium', Mock(return_value=(True, None))) as reuse_titanium_patch, \
                patch('sys.stdout', stdout):
            result_reuse = components.make_wheels(wheel_count)

        self.assertTrue(result_reuse)

        harvest_rubber_patch.assert_called_once()
        harvest_rubber_patch.assert_called_with(quantity=wheel_count, elasticity='hard')
        reuse_rubber_patch.assert_called_once()
        reuse_rubber_patch.assert_called_with(quantity=wheel_count, elasticity='hard')

        mine_titanium_patch.assert_called_once()
        mine_titanium_patch.assert_called_with(quantity=wheel_count, quality='normal')
        reuse_titanium_patch.assert_called_once()
        reuse_titanium_patch.assert_called_with(quantity=wheel_count, quality='low')

        # Split the output into lines and strip ending \n-s
        output = [line.strip() for line in stdout.getvalue().splitlines()]

        # Test that both warnings have been printed by components.make_wheels()
        self.assertIn(
            '[components.make_wheels] could not harvest rubber, attempting reuse: %s' % rubber_message,
            output
        )

        self.assertIn(
            '[components.make_wheels] could not mine titanium, attempting reuse: %s' % titanium_message,
            output
        )

        # Case 3 - couldn't get neither rubber nor titanium

    def test_make_windows(self):
        self.skipTest(reason='Not tested yet')

    def test_make_body_and_wings(self):
        self.skipTest(reason='Not tested yet')

    def test_make_motors(self):
        self.skipTest(reason='Not tested yet')
