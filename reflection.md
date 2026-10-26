# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first screen looked like a normal Streamlit number-guessing game, but its
behavior did not match the displayed rules. A guess above the secret produced a
"Go HIGHER" message, while a guess below it produced "Go LOWER." On every
second valid attempt, `app.py` converted the secret to a string; this forced
`check_guess` into its exception path, compared unlike representations, and
made a correct numeric guess fail. Starting a new game also left the old score,
status, and history in session state and generated a number from 1 to 100 even
when the selected difficulty used a different range.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret `50`, guess `60` | Outcome is `Too High` and the hint tells the player to guess lower | Outcome was labeled `Too High`, but the message said `Go HIGHER!` | No console error; UI showed `📈 Go HIGHER!` |
| Secret `50`, guess `40` | Outcome is `Too Low` and the hint tells the player to guess higher | Outcome was labeled `Too Low`, but the message said `Go LOWER!` | No console error; UI showed `📉 Go LOWER!` |
| Secret `50`, correct guess `50` on an even-numbered attempt | The game reports a win | The secret was converted to `"50"`; the mixed-type comparison entered the fallback and returned `Too Low` | A `TypeError` was caught internally, hiding the underlying mixed-type bug |
| Click **New Game** after playing on Easy | Start a clean Easy game in the range 1–20 with zero attempts, score, and history | A secret from 1–100 was generated while old score, status, and history remained | No console error; debug values contradicted the selected settings |

---

## 2. How did you use AI as a teammate?

I used Codex as an AI coding teammate to inspect the starter code, identify
likely causes, draft focused fixes, and propose tests. Its correct suggestion
was to keep the secret and other game values in `st.session_state`; I verified
that by launching the app, reading secret 96 in the debug panel, submitting 96,
and seeing a win with a score of 100. I did not accept the broader idea of
introducing a separate `GameState` class because it would add unnecessary
architecture to a small Streamlit app; I kept state in Streamlit and moved only
pure logic into `logic_utils.py`, then verified that design with 10 passing
tests and a live browser check.

---

## 3. Debugging and testing your fixes

I treated a bug as fixed only when a focused automated test passed and the live
game behaved the same way. For example, the tests compare guesses 60 and 40 to
a secret of 50 and confirm the outcomes are `Too High` and `Too Low`; these
tests prove that the comparison direction is no longer reversed. Codex also
helped draft edge cases for blank, non-numeric, decimal, and negative input,
which I reviewed to ensure they tested observable behavior instead of internal
implementation details. Finally, I started Streamlit and completed a game using
the debug secret to verify the session-state and win path end to end.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python script from top to bottom whenever the user interacts
with a widget. Ordinary local variables are therefore recreated, so they cannot
reliably hold a secret number or score between guesses. `st.session_state` is a
persistent dictionary for one browser session, and resetting all related keys
together prevents data from an old game from leaking into a new one.

---

## 5. Looking ahead: your developer habits

I want to keep reproducing and documenting bugs before changing code, then make
small commits with tests that describe the repaired behavior. Next time I use
AI, I will give it one bug and the relevant files at a time instead of asking
for a broad rewrite. This project showed me that plausible AI-generated code
can hide inconsistent types and state errors even when the interface looks
finished. AI is most useful when I treat its output as a proposal that must be
read, tested, and simplified.
