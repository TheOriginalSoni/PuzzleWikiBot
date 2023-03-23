# PWB (PuzzleWikiBot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- [PuzzleWikiBot](#puzzle-wiki-bot)
  - [What is PuzzleWikiBot](#what-is-puzzlewikibot)
  - [How to install](#how-to-install)
  - [Current Modules](#current-modules)
  - [Acknowledgements](#acknowledgements)
  - [Contributing/Issues](#contributingissues)

## What is PuzzleWikiBot

A Discord bot that uses [Puzzles Wiki](https://www.puzzles.wiki/wiki/Main_Page) to query info for Puzzlehunts on discord.

If you would like to add PWB to your server, please contact `@Soni#3662` on discord or use the invite link.

## Inviting the Bot to your server

- Message `@Soni#3662` on discord to get Bot invite link

- Use the Link and add the Bot to your discord server. Note that you need "Manage Server" permission to do that.

- Use `~help` or `~about` to get a quick guide to the bot.

- In case of any problems, message us on discord or [open a new issue on Github](TODO).

## How to install your own instance

### Prerequisites - 

- [python3.7 or newer](https://realpython.com/installing-python/)

- [Git](https://github.com/git-guides/install-git)

- [Pip package installer for Python](https://phoenixnap.com/kb/install-pip-windows)

Note that you may use another Python installer (instead of Pip), or Host (instead of Heroku) but that will require you figuring out the required setup and configuation changes yourself.

### Installation

We recommend using [virtual environments](https://docs.python.org/3/tutorial/venv.html) to manage python packages for our repo. To clone the repo and install dependencies, run the following on the Command Line

```bash
#Clone the bot locally
git clone TODO
cd puzzlewikibot
virtualenv venv -p=3.10
#Technically optional, but using virtualenv is usually a good idea
pip install -r requirements.txt && pre-commit install
#This installs all the python dependancies the bot needs
```

To run the bot locally, you will need a `.env` file which is used by [python-dotenv](https://github.com/theskumar/python-dotenv) to load `ENV` variables. Copy `.env.template` into `.env` with  

```bash
cp .env.template .env
```

and fill in the blanks in order to get the bot running. 

Once you do all that, run


```bash
source venv/bin/activate
python bot.py
```

and the bot will run on the supplied discord token's account.

### Hosting

Once you have the bot running and basic commands (like `~help`) run properly, you can host it externally. Our instance of the bot is [hosted on Heroku](https://medium.com/@linda0511ny/create-host-a-discord-bot-with-heroku-in-5-min-5cb0830d0ff2)


### Other useful things

If you have github + heroku, using Heroku's [Github integration](https://devcenter.heroku.com/articles/github-integration) allows you to automatically push Github pushes to also deploy on Heroku. (Using `git push` to push to both Github and Heroku)

When deploying on heroku, any variables stored in .env locally cannot be pushed to any public repos. It's advisable to use [Heroku Config Vars](https://devcenter.heroku.com/articles/config-vars) to store them.

## Current Modules

TODO

## Acknowledgements

Big thanks to [Kevin Esslinger](https://github.com/kevslinger) and his [Bot-Be-Named](https://github.com/kevslinger/bot-be-named)
repo for much inspiration and code. 

## Contributing/Issues

If you find any issues, bugs, or improvements, please feel free to open an issue and/or pull request! Thank you!

Feel free to find me on discord, `@Soni#3662` with any questions you may have!