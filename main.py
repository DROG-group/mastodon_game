import time
from app.services import game_logic

def main():
    # Initialization or setup code
    print("Mastodon Game Initializing...")

    # Hand over to the primary games logic
    game_logic.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMastodon Game Stopped.")