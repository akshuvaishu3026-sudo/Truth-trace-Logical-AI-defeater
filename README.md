[README.md](https://github.com/user-attachments/files/33367676/README.md)# Truth Trace

**Follow the logic. Defeat the AI.**

Truth Trace is a command-line logic game. Each round gives you a chain of reasoning with exactly one flawed step. You and a simulated AI both try to find it. The AI gets more accurate every round, so you need to read carefully.

## Run it

```bash
python truth_trace.py
```

Requires Python 3.8+. No dependencies.

## How to play

1. Read the numbered chain of reasoning.
2. Enter the number of the step where the logic breaks.
3. See the AI's guess, the correct answer, and why it was wrong.
4. Score a point for each correct catch. Highest score after all rounds wins.

## Add your own puzzles

Edit the `PUZZLES` list in `truth_trace.py`:

```python
{
    "title": "Your Title",
    "steps": ["Premise...", "Premise...", "Conclusion...", "Bigger conclusion..."],
    "flaw": 4,          # 1-based index of the flawed step
    "why": "Explanation of the fallacy.",
}
```

## Fallacies covered

- Affirming the consequent
- Overgeneralization
- Correlation treated as proof
- Conclusions that outrun their premises

## License

MIT

