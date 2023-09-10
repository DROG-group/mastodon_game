# Mastodon Game

A social media adventure game built on the Mastodon platform. Dive into a dynamic environment, interact with bots, and unravel the mysteries of the Mastodon instance.

## Features

- Dynamic environment with thousands of bots.
- Real-time interactions and events.
- Customizable game scenarios and story arcs.
- Robust error handling and logging.

## Setup

1. Clone the repository:

2. Navigate to the project directory:

3. Install the required packages

pip install -r requirements.txt
4. Change the API throttle limit

sed -i 's/limit: 100/limit: 10000/g' /path/to/mastodon/config/initializers/rack_attack.rb
5. Set up the environment variables. Copy the `.env.example` to `.env` and fill in the required details.

6. Run the game:
python main.py


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)