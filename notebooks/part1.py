import os, io, base64, time
from openai import OpenAI
import gradio as gr

# Load environment variables from .env file
import sys
sys.path.append('../utils')
from helpers import load_env

# Load environment variables
load_env()