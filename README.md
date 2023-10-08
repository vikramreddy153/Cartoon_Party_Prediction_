             Party Prediction App 
               Documentation                  
Overview
The Party Prediction App is a web application that predicts the winning political party based on various features using machine learning. This documentation provides an overview of the project's components, including the HTML templates, Python code for model training, and CSS for styling.
Components
	HTML Template (index.html)
The HTML template defines the structure of the web page. It includes sections for displaying the predicted winning party and model accuracy, as well as a header and footer.
 	Header
•	The header contains a transparent black background with white text.
•	It displays the logo of the Party Prediction App, which is centered horizontally.
 	Main Content
•	The main content section includes two sections:
1.	Predicted Winning Party: Displays the predicted winning party, which is dynamically generated based on machine learning predictions.
2.	Model Accuracy: Displays the model's accuracy on the test dataset, also dynamically generated.
 	Footer
•	The footer, like the header, has a transparent black background with white text.
•	It displays the copyright notice for the Party Prediction App.
	Python Code (app.py)
The Python code is responsible for training the machine learning model, making predictions, and rendering the web page using the Flask web framework.
 	Libraries Used
•	Flask: Used to create the web application.
•	pandas: Used for data manipulation and analysis.
•	sklearn: Used for machine learning tasks such as model training and evaluation.
 	Model Training and Prediction
•	The code loads a dataset from a CSV file and preprocesses it.
•	It encodes categorical variables using LabelEncoder and one-hot encoding.
•	The dataset is split into training and testing sets.
•	A logistic regression model is created and trained on the training data.
•	Predictions are made on the test dataset to calculate accuracy.
•	The winning party is predicted for the entire dataset based on model predictions.
 	Flask Web Application
•	The Flask web application serves the HTML template (index.html).
•	It passes the accuracy and winning party information to the template for dynamic rendering.
•	The app runs in debug mode, allowing for testing and development.
	CSS Styling (style.css)
The CSS stylesheet provides styling for the web page, improving its visual appeal and user experience.
 	Reset and Basic Styling
•	Default styles for body, h1, h2, and p elements are reset.
•	The body element uses the Philosopher font, has a white background, and is styled for responsive design.
•	The header section has a transparent black background, white text, and centered content.
•	header h1 sets the font size for the header title.
•	The main section is styled with a maximum width, margin for centering, and a white background.
•	h2 elements have a specific font size and margin for better readability.
•	section elements have a background color, padding, and border for styling.

 	Center Alignment
•	The .center-text class is defined for center-aligning text within section elements.
 	Responsive Design
•	Media queries are used to adjust styles for screens with a maximum width of 600px, improving the mobile user experience.
Conclusion
The Party Prediction App combines HTML templates, Python code, and CSS styling to create a web application that predicts political party outcomes. Users can access the web page to view the predicted winning party and model accuracy. The project demonstrates the integration of machine learning with web development using the Flask framework.

