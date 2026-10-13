"""Truth Trace: follow the logic, defeat the AI.

Each round shows a chain of reasoning with one flawed step.
You and a (simulated) AI both try to find it. Spot it, and explain
why, to score. The AI gets sharper every round.
"""
import random

PUZZLES = [
    {
        "title": "The Umbrella Argument",
        "steps": [
            "All people carrying umbrellas today got wet.",
            "Maria is carrying an umbrella.",
            "Therefore Maria got wet.",
            "Therefore it must have rained today.",
        ],
        "flaw": 4,
        "why": "Umbrellas also shield sun, and people can get wet from other causes. Wet does not prove rain.",
    },
    {
        "title": "The Fast Server",
        "steps": [
            "Every server in the fast cluster responds in under 50 ms.",
            "Server B responds in 30 ms.",
            "Therefore Server B is in the fast cluster.",
            "Therefore Server B is covered by the fast-cluster SLA.",
        ],
        "flaw": 3,
        "why": "Affirming the consequent: fast cluster implies fast response, not the reverse.",
    },
    {
        "title": "The Safe Bridge",
        "steps": [
            "The bridge held 10 trucks yesterday.",
            "Today there are 10 trucks on it.",
            "The bridge held yesterday's load, so it will hold today's.",
            "Therefore the bridge is safe at any load.",
        ],
        "flaw": 4,
        "why": "Surviving one load says nothing about all loads. This overgeneralizes.",
    },
    {
        "title": "The Popular App",
        "steps": [
            "Ten million people downloaded the app.",
            "Popular apps are well built.",
            "Therefore the app is popular and well built.",
            "Therefore the app has no security flaws.",
        ],
        "flaw": 4,
        "why": "Popularity and quality do not guarantee security. The conclusion jumps beyond the premises.",
    },
]


def ask_step(prompt, n):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and 1 <= int(raw) <= n:
            return int(raw)
        print(f"Enter a number from 1 to {n}.")


def ai_guess(puzzle, accuracy):
    n = len(puzzle["steps"])
    if random.random() < accuracy:
        return puzzle["flaw"]
    return random.choice([i for i in range(1, n + 1) if i != puzzle["flaw"]])


def main():
    random.shuffle(PUZZLES)
    you = ai = 0
    accuracy = 0.35
    print("=== TRUTH TRACE: follow the logic, defeat the AI ===\n")
    for rnd, p in enumerate(PUZZLES, 1):
        print(f"Round {rnd}: {p['title']}")
        for i, s in enumerate(p["steps"], 1):
            print(f"  {i}. {s}")
        mine = ask_step("Which step is flawed? ", len(p["steps"]))
        theirs = ai_guess(p, accuracy)
        print(f"AI picks step {theirs}.")
        print(f"Answer: step {p['flaw']}. {p['why']}")
        you += mine == p["flaw"]
        ai += theirs == p["flaw"]
        print(f"Score: You {you} | AI {ai}\n")
        accuracy = min(0.9, accuracy + 0.15)
    print("You win!" if you > ai else "Tie." if you == ai else "The AI wins this time.")


if __name__ == "__main__":
    main()
