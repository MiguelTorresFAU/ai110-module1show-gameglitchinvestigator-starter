"""Tests for the pure guessing-game logic."""

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    """A guess equal to the secret is a win."""
    assert check_guess(50, 50) == "Win"


def test_guess_too_high():
    """A guess above the secret is labeled too high."""
    assert check_guess(60, 50) == "Too High"


def test_guess_too_low():
    """A guess below the secret is labeled too low."""
    assert check_guess(40, 50) == "Too Low"


def test_empty_guess_is_rejected():
    """Blank input produces a useful validation error."""
    assert parse_guess("   ") == (False, None, "Enter a guess.")


def test_non_numeric_guess_is_rejected():
    """Non-numeric input is rejected instead of crashing."""
    assert parse_guess("banana") == (False, None, "Enter a whole number.")


def test_decimal_guess_is_rejected_instead_of_truncated():
    """A decimal string is not silently changed into another guess."""
    assert parse_guess("12.8") == (False, None, "Enter a whole number.")


def test_valid_negative_integer_is_parsed():
    """Parsing remains responsible only for integer syntax."""
    assert parse_guess("-4") == (True, -4, None)


def test_unknown_difficulty_uses_normal_range():
    """An unknown difficulty falls back to the normal range."""
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_wrong_guess_does_not_change_score():
    """An incorrect guess cannot add arbitrary bonus points."""
    assert update_score(0, "Too High", 2) == 0


def test_earlier_win_scores_more_points():
    """Winning sooner earns a larger deterministic bonus."""
    assert update_score(0, "Win", 1) > update_score(0, "Win", 5)
