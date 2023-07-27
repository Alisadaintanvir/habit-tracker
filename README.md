# Pixela Habit Tracker
A simple Python script to track your jogging distance using the Pixela API. This script creates a user, a graph, and allows you to post, update, and delete pixels on the graph to track your jogging progress.

## Prerequisites
Before running the script, make sure you have the following:

- Python installed on your system.
- requests and dotenv Python packages installed. You can install them using the following command:
  `pip install requests dotenv`

##  Getting Started
- Clone this repository to your local machine.
- Create a .env file in the same directory as the script.
- Inside the .env file, add the following lines and replace YOUR_USERNAME and YOUR_TOKEN with your Pixela username and token:

`user_name=YOUR_USERNAME`
`TOKEN=YOUR_TOKEN`

## Usage
Run the script using the following command:

`python main.py`

The script will guide you through the process of creating a user, a graph, posting pixels, updating pixels, and deleting pixels.

## Important Note
If you want to modify the script or use it in your project, make sure to review and uncomment the appropriate sections of the code related to creating a user, graph, posting pixels, updating pixels, and deleting pixels.

## License
This project is licensed under the MIT License.

## Acknowledgments
This script utilizes the Pixela API, a service provided by Asai Yusuke.
