import json
import os

class GameStats:
    """Track the statistics for alien invasion. """

    def __init__(self, ai_game):
        """Initialize statistics. """
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.load_high_score()

    def load_high_score(self):
        """Load the high score from a file."""
        filename = 'high_score.json'
        if not os.path.exists(filename):
            return 0
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            return data.get('high_score', 0)
        except Exception:
            return 0

    def save_high_score(self):
        """Save the high score to a file."""
        filename = 'high_score.json'
        try:
            with open(filename, 'w') as f:
                json.dump({'high_score': self.high_score}, f)
        except Exception:
            pass  # Optionally print/log an error

    def reset_stats(self):
        """Initialize statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1