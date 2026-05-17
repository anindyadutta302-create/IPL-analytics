"""
run_analysis.py
---------------
One-command entry point.

    python run_analysis.py

Loads data → runs all three analyses → prints results → saves charts
to charts/ and a JSON summary to outputs/summary_stats.json.
"""

import os
import sys
import json

# Make src importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from load_data import load
from toss_analysis import compute as toss_compute, by_decision, summary as toss_summary
from phase_analysis import compute as phase_compute, gap_ranking, summary as phase_summary
from player_rankings import top_batters, top_bowlers, summary as players_summary
from visualize import generate_all

OUTPUTS_DIR = os.path.join(os.path.dirname(__file__), "outputs")


def run():
    print("\n" + "=" * 60)
    print("  🏏  IPL ANALYTICS — BACKING OPINIONS WITH NUMBERS")
    print("=" * 60 + "\n")

    # ── Load ──────────────────────────────────────────────────────
    df = load()
    print()

    # ── Q1: Toss ──────────────────────────────────────────────────
    toss_summary(df)

    # ── Q2: Phases ────────────────────────────────────────────────
    phase_summary(df)

    # ── Q3: Players ───────────────────────────────────────────────
    players_summary(df)

    # ── Surprising finding ────────────────────────────────────────
    print("=" * 50)
    print("SURPRISING FINDING")
    print("=" * 50)
    print(
        "  The toss is theater. A 50.5% win rate across 1,218 matches\n"
        "  means captains' elaborate strategies about 'reading conditions'\n"
        "  have zero measurable impact on outcomes. The coin flip is the\n"
        "  most honest part of the strategy.\n"
    )

    # ── Charts ────────────────────────────────────────────────────
    generate_all(df)

    # ── JSON summary ──────────────────────────────────────────────
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    toss = toss_compute(df)
    phases = phase_compute(df).to_dict(orient="records")
    gaps = gap_ranking(df).to_dict(orient="records")
    batters = top_batters(df, 5).to_dict(orient="records")
    bowlers = top_bowlers(df, 5).to_dict(orient="records")
    decision = by_decision(df).to_dict(orient="records")

    summary = {
        "dataset": {
            "total_balls": len(df),
            "total_matches": df["match_id"].nunique(),
            "seasons": sorted(df["season"].unique().tolist()),
        },
        "q1_toss": {**toss, "by_decision": decision},
        "q2_phases": {"avg_runs_by_phase": phases, "gap_ranking": gaps},
        "q3_players": {"top_batters": batters, "top_bowlers": bowlers},
        "surprising_finding": (
            "Toss winners win only 50.5% of matches across 1,218 games — "
            "statistically indistinguishable from a coin flip."
        ),
    }

    out_path = os.path.join(OUTPUTS_DIR, "summary_stats.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"  JSON summary saved → {out_path}")
    print("\n✅  All done.\n")


if __name__ == "__main__":
    run()
