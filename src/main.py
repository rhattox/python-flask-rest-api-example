from flask import Flask, request
import logging

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/register", methods=['POST'])
def post_email():
    if request.method == 'POST':
        # Get data from the request
        app.logger.info(request.is_json)
        if (request.is_json == True):
            data = request.json  # Assuming the key is 'key' in the form data
            print(data)
            return f'Received POST request with data: {data}'
        else:
            return 'Param not allowed'
    else:
        # Handle other HTTP methods if needed
        return 'Method not allowed', 405


if __name__ == "__main__":
    app.run(debug=True)