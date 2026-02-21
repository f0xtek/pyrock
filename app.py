"""
Generates a random secure password string using a combination of passwords
from the RockYou database.
"""

from flask import Flask, render_template
import secrets
import bs4
import requests

APP = Flask(__name__)


def get_rockyou():
    """
    Scrape the RockYou passwords from SecLists rockyou.txt files
    """
    url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-20.txt'
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    content = response.text
    soup = bs4.BeautifulSoup(content, features="html.parser")
    pws = soup.prettify().split('\n')
    pws.pop()
    return pws


@APP.route('/')
def index():
    """
    Render the webpage.
    """
    return render_template('template.html')


@APP.route('/generate/')
def generate():
    """
    Generate a passphrase fromt he rockyou passwords.
    """
    passwords = get_rockyou()
    password = ' '.join(secrets.choice(passwords) for i in range(4))
    return render_template('generate.html', password=password)


if __name__ == '__main__':
    APP.run(debug=False)
