# Edit the install path to the directory where you put alexa_agent_flask.py
INSTALL_PATH = '/opt/alexa-agent-flask'
import sys
sys.path.append(INSTALL_PATH)
from alexa_agent_flask import app as application
import logging
logging.basicConfig(stream=sys.stderr)


if __name__ == "__main__":
    application.run()
