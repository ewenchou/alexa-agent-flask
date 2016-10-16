# Alexa Agent Flask

Example of how to invoke [Alexa Agent](https://github.com/ewenchou/alexa-agent) using a simple Flask web API.

# Requirements

1. Follow the README in the [Alexa Agent](https://github.com/ewenchou/alexa-agent) repository to install and setup.
2. Install Flask: `sudo pip install flask`
3. (Optional): Install Apache and setup Flask app with WSGI (see `sample-apache.conf`)

# Testing

1. Clone this repository and run the Flask app script:

    ```
    cd /opt
    git clone https://github.com/ewenchou/alexa-agent-flask.git
    cd alexa-agent-flask
    python alexa_agent_flask.py
    ```

2. Send HTTP GET request to the example URL:

    ```
    curl http://127.0.0.1:8888/tell-me-a-joke
    curl http://127.0.0.1:8888/morning-report
    ```
