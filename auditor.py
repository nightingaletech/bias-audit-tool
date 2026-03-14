import csv

def load_predictions(filepath):
    """Load predictions CSV and return a list of dicts."""
    rows = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def accuracy_by_group(rows, group_col):
    """Compute accuracy per demographic group."""
    groups = {}
    for row in rows:
        group = row[group_col]
        actual = row["actual"]
        predicted = row["predicted"]
        if group not in groups:
            groups[group] = {"correct": 0, "total": 0}
        groups[group]["total"] += 1
        if actual == predicted:
            groups[group]["correct"] += 1
    results = {}
    for group, counts in groups.items():
        results[group] = counts["correct"] / counts["total"]
    return results

def flag_disparity(accuracies, threshold=0.10):
    """Flag groups where accuracy is more than threshold below the best group."""
    best = max(accuracies.values())
    flagged = {}
    for group, acc in accuracies.items():
        gap = best - acc
        if gap > threshold:
            flagged[group] = round(gap, 3)
    return flagged

if __name__ == "__main__":
    rows = load_predictions("predictions.csv")
    print(f"Loaded {len(rows)} predictions\n")

    accuracies = accuracy_by_group(rows, "age_group")
    print("ACCURACY BY GROUP")
    for group, acc in sorted(accuracies.items()):
        bar = "█" * int(acc * 20)
        print(f"  {group:<8} {acc:.1%}  {bar}")

    print("\nDISPARITY FLAGS")
    flagged = flag_disparity(accuracies)
    if flagged:
        for group, gap in flagged.items():
            print(f"  {group:<8} ⚠  {gap:.1%} below best group")
    else:
        print("  No significant disparities detected")