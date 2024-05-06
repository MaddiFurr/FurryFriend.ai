import discord
from discord import Webhook
from .BotService import bot
from .SettingsService import settings

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '> ')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#This function checks if the user has the proper permissions to run a command and returns true if they do, false if they don't
async def single(prompt):
    GOOGLE_API_KEY = settings.GOOGLE_API_KEY
    
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(prompt, stream=False)
    
    return response
    