from unittest import TestCase


class TestBase(TestCase):
    """
    Provides a common setUp and tearDown methods for
    child test classes.
    """
    def setUp(self):
        """
        This method is executed before every test. If you inherit
        from this class and implement your own setUp(), you should
        also call this one via super() - unless you want to override
        it instead of extending.
        """
        super(TestBase, self).setUp()
        # Your setup commands here

    def tearDown(self):
        """
        This method is executed after every test and should destroy
        data that could potentially leak to other tests (like database
        entries or files with content). Same thing with inheritance
         as in setUp() applies.
        """
        # Your teardown commands here
        super(TestBase, self).tearDown()
