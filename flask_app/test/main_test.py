import os
import main
import unittest

class FlaskrTestCase(unittest.TestCase):
    """
     It's a main application test class for funtional testing. A|B testing engine can be devided by three modules 
    which are controller, service and database access object. Each modules need to do unit testing and finally get a 80% code coverage rate.
    Functional test that have been described and implemented in this class is a key to keep application quality high and will be used for load test.
    """
    def setUp(self):
        """
         set up initialize steps before test begin like creating db connection or test client
        """
        pass

    def tearDown(self):
        """
         finalize step after whole tests are end
        """
        pass


if __name__ == '__main__' :
    unittest.main()

