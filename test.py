from unittest import TestCase
from app import app
import json

class TestApp(TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_index_route(self):
        # Test the index route to check if it returns a 200 status code and the correct content
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Forex Converter</h1>', response.data) #shows HTML tag ensuring that the template is properly rendered
        self.assertIn(b'<label for="base_currency">From Currency:</label>', response.data)#using label for is better accessability
        self.assertIn(b'<label for="target_currency">To Currency:</label>', response.data)
        self.assertIn(b'<label for="amount">Amount:</label>', response.data)

    # Add a method to mock the API response- recommended by CHATgpt to isolate the test from external dependencies and ensures predictable and controlled test scenarios.
    def mock_api_response(self, data):
        with mock.patch('requests.get') as mock_get: #uses the mock.patch context manager from the unittest.mock module & temporarily replaces the requests.get function with a mock object named mock_get within the context of this block. 
            response_mock = mock.Mock() #create new instance of Mock obj which is a special obj to mimic behav of API response.
            response_mock.status_code = 200
            response_mock.json.return_value = data
            mock_get.return_value = response_mock
            response = self.app.post('/convert', data=data)
            return response
        
    def test_convert_currency(self):
        # Test the convert_currency route with valid input
        data = {
            'base_currency': 'USD',
            'target_currency': 'EUR',
            'amount': '100'
        }
        response = self.app.post('/convert', data=data) #test the post submitting the data dictionary. bypass the actual form submission and directly send it to the server using the test client.
    # Check if the response data contains the expected conversion result
        self.assertIn(b'Result:', response.data)# the capitalization of R is confusing
        self.assertIn(b'United States dollar equals', response.data)

    def test_convert_currency_valid_input(self):
        # Another Test the convert_currency route with valid input
        data = {
            'base_currency': 'USD',
            'target_currency': 'USD',
            'amount': '1'
        }
        response = self.app.post('/convert', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Result:', response.data)
        self.assertIn(b'$1.00', response.data)

    def test_convert_currency_invalid_currency_code(self):
        # Test the convert_currency route with invalid currency code
        data = {
            'base_currency': 'XYZ',  # Invalid currency code
            'target_currency': 'EUR',
            'amount': '100'
        }
        response = self.app.post('/convert', data=data)
        self.assertIn(b'Invalid currency code.', response.data)