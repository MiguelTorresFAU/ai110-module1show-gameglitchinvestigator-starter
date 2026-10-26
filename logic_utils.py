"""Pure game logic for the Game Glitch Investigator project."""


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the inclusive number range for a supported difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, ranges["Normal"])


def parse_guess(raw: str | None) -> tuple[bool, int | None, str | None]:
    """Validate user input and return a parsed integer or an error message."""
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        value = int(raw.strip())
    except (TypeError, ValueError):
        return False, None, "Enter a whole number."

    return True, value, None


def check_guess(guess: int, secret: int) -> str:
    """Compare a guess with the secret and return the game outcome."""
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Award a larger score for a win reached in fewer valid attempts."""
    if outcome != "Win":
        return current_score

    win_points = max(10, 100 - 10 * (attempt_number - 1))
    return current_score + win_points
