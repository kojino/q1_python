import simple as server
import unittest

class FlaskSeverTest(unittest.TestCase):

    def setUp(self):
        # create a special instance of your server
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        assert response.status_code == 200, "status_code was not OK!"
        assert response.data == "Hello, World!"

if __name__ == '__main__':
    unittest.main()
