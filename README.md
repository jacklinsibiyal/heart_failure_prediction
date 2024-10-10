# Heart Failure Prediction App

This project is a web application designed to predict the likelihood of heart failure based on a user's health data. The app uses a Random Forest model trained on a dataset of heart health indicators to provide predictions and insights. The application is built using Python and Flask, with additional support from various data science libraries.

## Project Structure

The project files are organized as follows:

- **app.py**: The main file for the Flask application. It handles routes, user interactions, and model predictions.
- **heart.csv**: The dataset used for training and testing the machine learning model. It contains heart health indicators and corresponding labels for heart failure.
- **heart_failure_prediction.ipynb**: A Jupyter notebook containing the data exploration, preprocessing, and model training code for the heart failure prediction model.
- **random_forest_model.pkl**: A pre-trained Random Forest model saved as a pickle file. This model is loaded by the application to make predictions based on user inputs.
- **requirements.txt**: Lists all the dependencies required to run the project.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/jacklinsibiyal/heart_failure_prediction
   cd heart_failure_prediction
   ```

2. **Install the dependencies**:

   Make sure you have Python installed. Install the required Python packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   Execute the following command to start the Flask application:

   ```bash
   python app.py
   ```

   The application should now be running on `http://127.0.0.1:5000/`.

## Usage

- The application provides a simple web interface where users can input their health data (e.g., age, blood pressure, cholesterol levels, etc.).
- Once the data is submitted, the app uses the pre-trained Random Forest model to predict the likelihood of heart failure and displays the result.

## Demo

Try the live demo of the application [here](https://heart-failure-prediction-vzj3.onrender.com/).

## Model Training

The model used in this application is a **Random Forest** classifier trained using the `heart.csv` dataset. The training process and detailed analysis can be found in the `heart_failure_prediction.ipynb` Jupyter notebook. This notebook includes:

- Data exploration and visualization
- Data preprocessing and feature engineering
- Model training, validation, and evaluation
- Saving the trained model as a `pickle` file for use in the web application.

## License

This project is licensed under the MIT License. Feel free to modify and use the code for your purposes.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure you run tests before submitting.

## Contact

For any questions or issues, please contact Jacklin Sibiyal via [LinkedIn](https://www.linkedin.com/in/jacklinsibiyal/).
