# 🏏 IPL Analytics — Backing Opinions with Numbers

A data analysis project exploring 19 seasons of Indian Premier League cricket (289,673 balls bowled across 1,218 matches) to answer three questions everyone has opinions about — but rarely checks with data.

## Questions Answered

| # | Question | Finding |
|---|----------|---------|
| 1 | Do toss winners win more matches? | **No.** 50.5% win rate — statistically a coin flip |
| 2 | Which phase is most linked to winning? | **Middle overs (6–14)** — largest run gap between winners & losers |
| 3 | Who are the all-time top batters and bowlers? | **Kohli** (9,050 runs), **Chahal** (229 wickets) |

## Project Structure

```
ipl-analytics/
├── data/
│   └── ipl_ball_by_ball.csv      # Raw ball-by-ball data (cricsheet.org)
├── src/
│   ├── load_data.py              # Data loading & validation
│   ├── toss_analysis.py          # Q1: Toss impact analysis
│   ├── phase_analysis.py         # Q2: Powerplay / Middle / Death overs
│   ├── player_rankings.py        # Q3: Top batters & bowlers
│   └── visualize.py              # All chart generation (matplotlib)
├── notebooks/
│   └── ipl_analysis.ipynb        # Full end-to-end Jupyter notebook
├── outputs/
│   └── summary_stats.json        # Pre-computed results (auto-generated)
├── charts/                       # Generated chart PNGs (auto-generated)
│   ├── chart1_toss_impact.png
│   ├── chart2_phase_runs.png
│   └── chart3_player_rankings.png
├── run_analysis.py               # One-command entry point
└── requirements.txt
```

## Quick Start

```bash
# 1. Clone / download this repo
# 2. Install dependencies
pip install -r requirements.txt

# 3. Run everything — generates all charts and prints the summary
python run_analysis.py

# Or explore interactively
jupyter notebook notebooks/ipl_analysis.ipynb
```

## Data Source

Ball-by-ball CSV from **[cricsheet.org](https://cricsheet.org/matches/)** → Indian Premier League → CSV format.  
Each row = one ball bowled. Columns include batter, bowler, runs, extras, wicket kind, match result, toss info.

To download fresh data yourself:
```bash
python src/load_data.py --download
```

## Key Results

### Chart 1 — Toss Impact
Toss winners win **50.5%** of matches. Toss losers win **49.5%**.  
Across 1,218 matches, this is indistinguishable from random chance.

### Chart 2 — Phase Runs (Winners vs Losers)
| Phase | Winners avg | Losers avg | Gap |
|-------|------------|-----------|-----|
| Powerplay (0–5) | 51.3 | 46.2 | **+5.1** |
| Middle overs (6–14) | 74.3 | 67.4 | **+6.9** ← biggest |
| Death overs (15–19) | 47.2 | 44.3 | +2.9 |

### Top 5 Batters (all-time runs)
1. V Kohli — 9,050
2. RG Sharma — 7,269
3. S Dhawan — 6,769
4. DA Warner — 6,567
5. KL Rahul — 5,680

### Top 5 Bowlers (wickets from bowled/caught/lbw/stumped)
1. YS Chahal — 229
2. B Kumar — 215
3. SP Narine — 203
4. PP Chawla — 192
5. JJ Bumrah — 189

## Surprising Finding

> **The toss is theater.** A 50.5% win rate across 1,218 matches means captains' elaborate pre-match calculations about "reading the conditions" have zero measurable impact on outcomes. The coin flip is the most honest part of the strategy.

## Requirements

- Python 3.8+
- pandas, matplotlib, seaborn, numpy, jupyter (see `requirements.txt`)

## License

Data © cricsheet.org (CC BY-SA 4.0). Analysis code MIT.
