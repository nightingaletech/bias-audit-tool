import csv
import random

random.seed(42)

def generate_predictions(filepath, n=500):
    """Generate synthetic model predictions with deliberate bias."""
    groups = ["18-30", "31-50", "51-70", "71+"]
    # accuracy rates per group — bias built in against elderly
    accuracy_rates = {
        "18-30": 0.92,
        "31-50": 0.89,
        "51-70": 0.78,
        "71+":   0.61
    }

    rows = []
    for i in range(n):
        group = random.choice(groups)
        actual = random.choice([0, 1])
        rate = accuracy_rates[group]
        correct = random.random() < rate
        predicted = actual if correct else 1 - actual
        rows.append({
            "id": i + 1,
            "age_group": group,
            "actual": actual,
            "predicted": predicted
        })

    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "age_group", "actual", "predicted"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {n} predictions → {filepath}")

if __name__ == "__main__":
    generate_predictions("predictions.csv")