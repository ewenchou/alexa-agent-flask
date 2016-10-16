#!/usr/bin/env python

from flask import Flask, jsonify
from alexa_agent import AlexaAgent


app = Flask(__name__)


@app.route('/tell-me-a-joke', methods=['GET'])
def tell_me_a_joke():
    agent = AlexaAgent()
    agent.wakeup()
    agent.ask('tell me a joke')
    return jsonify({'code': 200, 'message': 'Was that joke funny?'})


@app.route('/morning-report', methods=['GET'])
def morning_report():
    agent = AlexaAgent()
    agent.wakeup()
    agent.ask([
        "What is today's date",
        "What time is it",
        "How's the weather"
    ])
    return jsonify({'code': 200, 'message': 'Morning report delivered!'})


if __name__ == '__main__':
    app.run(port=8888, debug=True)
