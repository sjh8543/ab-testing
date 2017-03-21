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
        self.app = main.app.test_client()

    def tearDown(self):
        """
         finalize step after whole tests are end
        """
        pass

    def test_admin(self):
        """
         It's test function for admin URL"
        """
        rv = self.app.get('/admin')
        assert "It's admin URL" in rv.data.decode('utf-8')

    def test_collecting(self):
        """
         It's test function for collecting URL"
        """
        rv = self.app.get('/collecting')
        assert "It's collecting URL" in rv.data.decode('utf-8')

    def test_routing(self):
        """
         It's test function for routing url
        """
        rv = self.app.get('/routing')
        assert "It's routing URL" in rv.data.decode('utf-8')

    def test_reporting(self):
        """
         It's test function for reporting url
        """
        rv = self.app.get('/reporting')
        assert "It's reporting URL" in rv.data.decode('utf-8')
    
if __name__ == '__main__' :
    unittest.main()
