from unittest import TestCase
from pymms import mms
from pymms import research_instruments as ri
from pymms import drawing
from pymms import print_results


class PyMmsTestCase(TestCase):
    
    def test_run(self):
        observer = ri.Table()
        xt= mms.Composite( 10, 1, observer)
        pr = print_results.print_results(dp)
        visio = drawing.Visualization(dp)
        self.assertEqual(xt.runtest(), 'Test mms')
