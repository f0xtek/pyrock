# PyRock 🔐

A Flask web application that generates cryptographically secure passphrases using words sourced from the infamous [RockYou](https://en.wikipedia.org/wiki/RockYou#Data_breach) leaked password database.

## Overview

PyRock combines four randomly chosen words from the RockYou password list to create a memorable yet highly secure passphrase. This approach draws on the [XKCD-style](https://xkcd.com/936/) passphrase concept — easy to remember, hard to crack.

## Features

- 🎲 Generates a 4-word passphrase using cryptographically secure random selection (`secrets` module)
- 🌐 Simple, clean web interface powered by Bootstrap
- ⚡ Lightweight Flask backend
- 🔒 No debug mode in production

## Requirements

- Python 3.13+
- [pipenv](https://pipenv.pypa.io/en/latest/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/f0xtek/pyrock.git
   cd pyrock
   ```

2. **Install dependencies with pipenv:**

   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

## Usage

Run the Flask development server:

```bash
python app.py
```

Then open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

Click the **Generate!** button to get a new passphrase.

## How It Works

1. When you click **Generate!**, the app fetches the `rockyou-20.txt` password list from the [SecLists](https://github.com/danielmiessler/SecLists) GitHub repository.
2. It then uses Python's `secrets.choice()` to cryptographically randomly select 4 passwords from the list.
3. The 4 words are joined together into a passphrase and displayed on screen.

## Project Structure

```
pyrock/
├── app.py              # Main Flask application
├── templates/
│   ├── template.html   # Home page template
│   └── generate.html   # Generated passphrase display template
├── Pipfile             # pipenv dependency definition
├── Pipfile.lock        # Locked dependency versions
└── README.md
```

## Dependencies

| Package          | Purpose                                |
|------------------|----------------------------------------|
| Flask            | Web framework                          |
| requests         | HTTP requests to fetch the password list |
| beautifulsoup4   | HTML parsing                           |

## Security Notes

- Passphrase selection uses Python's `secrets` module (cryptographically secure PRNG), not the weaker `random` module.
- The Flask app runs with `debug=False` to prevent exposure of sensitive debug information in production.
- HTTP requests include a timeout to prevent indefinite hanging.

## License

This project is open source. See the repository for details.
