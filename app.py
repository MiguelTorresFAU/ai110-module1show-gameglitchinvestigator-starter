"""Streamlit interface for the repaired number-guessing game."""

import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def reset_game(low: int, high: int, difficulty: str) -> None:
    """Reset every value that belongs to one game session."""
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.active_difficulty = difficulty


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("A repaired number-guessing game with reliable hints and state.")

st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# FIX: Codex suggested keeping persistent values in session_state. The reset
# also covers difficulty changes so the secret always matches the shown range.
if (
    "secret" not in st.session_state
    or st.session_state.get("active_difficulty") != difficulty
):
    reset_game(low, high, difficulty)

st.subheader("Make a guess")
attempts_left = max(0, attempt_limit - st.session_state.attempts)
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input("Enter your guess:", key=f"guess_input_{difficulty}")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # FIX: Reset the complete session using the selected difficulty range.
    reset_game(low, high, difficulty)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, error = parse_guess(raw_guess)

    if not ok:
        st.error(error)
    elif not low <= guess_int <= high:
        st.error(f"Enter a number between {low} and {high}.")
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        # FIX: Keep both values as integers and centralize comparison logic.
        outcome = check_guess(guess_int, st.session_state.secret)
        hint_messages = {
            "Win": "🎉 Correct!",
            "Too High": "📉 Too high — guess lower.",
            "Too Low": "📈 Too low — guess higher.",
        }

        if show_hint:
            st.warning(hint_messages[outcome])

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
            st.error(
                f"Out of attempts! The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

st.divider()
st.caption("Built with AI assistance and verified with automated tests.")
