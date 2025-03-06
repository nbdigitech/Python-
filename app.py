from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, this is a simple Flask application running on Contabo VPS!"

# Define a route for another page
@app.route('/about')
def about():
    return "This is the About page of the Flask application."

# Start the server when running the script directly
if __name__ == '__main__':
    # Run the app on all available interfaces (0.0.0.0) and port 5001
    app.run(host='0.0.0.0', port=5001)
