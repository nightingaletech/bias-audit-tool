# Bias Audit Tool

A Python tool that audits ML model predictions for demographic bias — computing 
accuracy per group and flagging disparities that indicate unfair model behaviour.

---

## The problem

A model can appear highly accurate overall while systematically failing specific 
demographic groups. A healthcare model that is 91% accurate for patients aged 
18–30 but only 52% accurate for patients aged 71+ is not a safe model — but 
that failure is invisible without a group-level audit.

Bias Audit Tool makes it visible.

---

## Quickstart
```bash
git clone https://github.com/nightingaletech/bias-audit-tool.git
cd bias-audit-tool
python generate_data.py
python auditor.py --file predictions.csv
```

---

## Example output
```
============================
  BIAS AUDIT REPORT
  predictions.csv | 500 predictions
============================

ACCURACY BY GROUP
  18-30    90.4%  ██████████████████
  31-50    91.4%  ██████████████████
  51-70    70.0%  ██████████████
  71+      52.0%  ██████████

DISPARITY FLAGS
  71+      ⚠  39.4% below best group
  51-70    ⚠  21.4% below best group

============================
```

---

## Configuration

Edit `config.py` to point at your own predictions file:

| Setting | Default | Description |
|---|---|---|
| `DATA_PATH` | `predictions.csv` | Path to your predictions CSV |
| `GROUP_COLUMN` | `age_group` | Demographic column to audit |
| `DISPARITY_THRESHOLD` | `0.10` | Flag groups more than 10% below the best group |

Your CSV must have at minimum these columns: `actual`, `predicted`, and whichever 
column you set as `GROUP_COLUMN`.

---

## Generating synthetic data

If you don't have real predictions, use the included generator:
```bash
python generate_data.py
```

This creates `predictions.csv` with 500 synthetic predictions across four age 
groups, with deliberate bias built in against older groups — so you can verify 
the tool catches what it should.

---

## Why this matters for AI safety

Demographic disparity in model predictions is one of the most documented and 
consequential failure modes in deployed ML systems. It has been observed in 
healthcare risk scoring, criminal recidivism prediction, hiring tools, and 
facial recognition systems.

Bias Audit Tool is a lightweight first step toward making these disparities 
visible before a model reaches production.

---

## Roadmap

- [ ] Support multiple demographic columns in one run
- [ ] CSV export of audit results
- [ ] Intersectional analysis (e.g. age group × gender)
- [ ] HTML report output

---

## License

MIT
