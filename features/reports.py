"""Reporting helpers for StudySprint.

Heads up: this module is half-built on purpose. `deck_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def deck_summary(data):
    return data["deck_name"] + ": " + str(len(data["cards"])) + " cards"


def category_report(data):
    counts = {}
    cards = data.get("cards", []) if isinstance(data, dict) else data
    for card in cards:
        category = card.get("category", "General")
        counts[category] = counts.get(category, 0) + 1
    return counts

def best_streak(results):
    best = 0
    current = 0
    for result in results:
        if result:
            current += 1
            if current > best:
                best = current
        else:
            current = 0
        return best