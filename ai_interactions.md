# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

Not attempted as a separate feature-expansion stretch challenge.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Empty or whitespace input | "Draft a focused pytest for blank guessing-game input." | Assert that whitespace returns an unsuccessful parse with `Enter a guess.` | Yes | A blank form submission is common and should not consume an attempt or crash. |
| Non-numeric text | "Add a behavior test for a word entered as a guess." | Parse `banana` and assert a whole-number validation error. | Yes | User input is text, so accidental words must be handled safely. |
| Decimal text | "Test that the parser does not silently truncate a decimal guess." | Parse `12.8` and assert that it is rejected. | Yes | The starter converted floats to integers, which changed the player's input without warning. |
| Negative integer | "Separate integer parsing from range validation with a negative-value test." | Confirm `-4` parses as an integer before the UI rejects it as out of range. | Yes | This keeps the pure parser focused while preserving range checks in the UI layer. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

Not attempted as a separate linting stretch challenge.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

Not attempted.
