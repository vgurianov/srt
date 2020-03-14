from unittest import TestCase
from pymms import mms
from pymms import mms_ex
from pymms import research_instruments as ri
from pymms import drawing
from pymms import print_results


class PyMmsTestCase(TestCase):
    
    def test_run(self):
        observer = ri.Table()
        xt= mms.Composite( 10, 5, observer)
        xt_ex= mms_ex.Composite( 10, 5, observer,5)
        dp = ri.DataProcessing(observer, 5, 10, 10)
        pr = print_results.TablePrint(dp)
        visio = drawing.Visualization(dp)
        self.assertEqual(xt.runtest(), 'Test mms')
