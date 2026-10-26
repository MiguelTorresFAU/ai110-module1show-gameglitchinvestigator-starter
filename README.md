# 🎮 Game Glitch Investigator: The Impossible Guesser

## Project Overview

This Streamlit game asks the player to find a randomly selected number within a
difficulty-specific range and attempt limit. The starter version looked
complete but contained state, comparison, hint, scoring, and reset bugs. The
repaired version keeps each game stable across Streamlit reruns, validates
input, gives accurate hints, and calculates a deterministic score.

## Setup and Use

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```

Run the tests with:

```bash
python -m pytest
```

## Bugs Found and Fixes Applied

- The hint labels and messages contradicted each other. Comparison now lives in
  `logic_utils.check_guess`, while `app.py` maps each outcome to the correct
  direction.
- On alternating attempts, the secret changed from an integer to a string. The
  repaired game keeps both the guess and secret as integers and removes the
  exception-driven mixed-type comparison.
- A new game generated a secret from the wrong range and retained old state.
  `reset_game` now uses the selected range and resets attempts, score, status,
  and history together.
- Attempts began at one and were consumed before input validation. They now
  start at zero and increase only after a valid, in-range integer is submitted.
- The old score could increase after an incorrect guess. Scoring is now
  deterministic and awards a larger bonus for winning in fewer attempts.

## Demo Walkthrough

1. The player opens the app on Normal difficulty and sees a range of 1–100,
   eight attempts available, and score 0.
2. With debug secret 96, the player enters 40 and receives “Too low — guess
   higher”; the history records 40 and seven attempts remain.
3. The player enters 99 and receives “Too high — guess lower”; the history now
   records both valid guesses.
4. The player enters 96 and receives “Correct!”; the game enters its won state
   and displays the final score.
5. The player selects **New Game**, which creates a new secret in the active
   difficulty range and clears attempts, score, status, and history.

## Test Results

The suite covers the three comparison outcomes, blank and non-numeric input,
decimal and negative input, fallback difficulty behavior, and deterministic
scoring.

```text
..........                                                               [100%]
10 passed in 0.01s
```

## Document Your Experience

- [x] The game’s purpose is described in the project overview.
- [x] Reproducible starter bugs are detailed above and in `reflection.md`.
- [x] The fixes and their verification are explained above.

## UI Improvements

The repaired interface displays the active range and accurate attempts
remaining, uses directional emojis and clear wording for high/low hints, and
keeps a debug history so a player can verify state across reruns.

## Stretch Work

- [x] Advanced edge-case tests for blank, non-numeric, decimal, and negative
  input are included and passing.
- [x] AI test-generation prompts and the reasons for each edge case are recorded
  in `ai_interactions.md`.
