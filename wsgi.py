from flask import Flask, request
import requests
import certloader

certloader.load_certs()
application = Flask(__name__)

if __name__ = "__main__":
    application.run()
