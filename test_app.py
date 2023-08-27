import unittest
import cv2
from app import app
import os

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_upload_image(self):
        response = self.app.get('/uploads/download.jpg')
        self.assertEqual(response.status_code, 200)

        with response as f:
            data = f.data  

    
        self.assertTrue(data)

    def test_upload_and_process_image(self):
        with open('a.jpg', 'rb') as test_image:
            response = self.app.post(
                '/predict',
                data={
                    'num_tasks': '1',
                    'style_task_1': 'Style2',  
                    'file': (test_image, 'a.jpg')
                },
                content_type='multipart/form-data'
            )

            self.assertEqual(response.status_code, 200)
        

    

if __name__ == '__main__':
    unittest.main()


       
