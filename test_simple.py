from unittest import TestCase
from pymms import mms
from pymms import research_instruments as ri


class PyMmsTestCase(TestCase):
    
    def test_run(self):
        observer = ri.Table()
        xt= mms.Composite( 10, 1, observer)
        self.assertEqual(xt.runtest(), 'Test mms')
