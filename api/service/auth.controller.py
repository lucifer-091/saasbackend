from functools import wraps
import random
import smtplib
from flask import Blueprint, jsonify, request
from api import db



authservice = Blueprint('authservice', __name__)

    