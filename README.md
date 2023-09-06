In this project I have build a Image Filtering and Transformation  web app in Flask using Python and OpenCV.  User has the option to choose the image, then choose number of tasks, then
he has to select the tasks which he want to apply on image in the sequence.When user clicks the stylize button he can see the modified image , he also can download the image if he wants

All the backend routes are in app.py, frontend code is inside templates folder consisting of index.html,predict.html and base.html .  Unit test cases are in test_app.py



#SETUP INSTRUCTIONS

1)Install Python

2)Create a Virtual Environment 

3)Install Required Packages - pip install -r requirements.txt

4)Running the Flask Application: -  python app.py

5)Running the Flask Application: -  python test_app.py  make sure flask app is also running



#SYSTEM ARCHITECTURE

#Frontend:
The frontend consists of HTML templates that provide the user interface for interacting with the application. Users can upload images, select image processing tasks, and view the processed results.

index.html: The main page where users can upload an image and select processing tasks.
predict.html: Displays the processed image and provides feedback to the user.
Flask Application (app.py):
The Flask application serves as the backend and handles user requests, image processing, and serving static files. Key components of the Flask application are as follows:

Routes:

/: Renders the index.html template for uploading images and selecting tasks.
/predict: Handles image processing based on user selections, rendering the predict.html template to display the processed image.
/uploads/<filename> and /cartoon_images/<filename>: Serve uploaded and processed images for viewing.
Image Processing Functions:
Functions like cartoonize_2 to cartoonize_10 process images using OpenCV and specific algorithms.

#predict Route Logic:

#Reads the uploaded image, processes it using selected tasks and parameters.
Saves processed images to the cartoon_images directory.
Renders the predict.html template with relevant information.
Static and Uploaded Image Directories:

#static: Stores static files like CSS stylesheets, JavaScript scripts, and images for use by HTML templates.
uploads: Temporary directory for uploaded images before processing.
cartoon_images: Stores processed images after cartoonization.
Unit Tests (test_app.py):
The unit tests ensure the correctness of the application's functionality:

#FlaskAppTest class inherits from unittest.TestCase.
setUp: Creates a test client and sets testing mode to True.
tearDown: Placeholder for test cleanup.
test_home_page: Checks if the home page is accessible.
test_upload_image: Checks if an uploaded image is accessible.
test_upload_and_process_image: Uploads an image and tests the processing functionality. It simulates form data submission with an image.
User Interaction:

Users upload images and select processing tasks through the web interface.
The application processes images based on selected tasks and displays results.
In summary, the system architecture includes a frontend built with HTML templates, a Flask backend handling user interactions and image processing, static and uploaded image directories, and a set of unit tests to ensure the application's functionality. The application provides a user-friendly interface for image processing tasks and real-time feedback on the processed images.
