"""placeholder"""
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from reader import PlayerReader
from stats import PlayerStats

SEASONS = [
    "2018-19", "2019-20", "2020-21", "2021-22",
    "2022-23", "2023-24", "2024-25", "2025-26",
]

console = Console()


def main():
    """placeholder"""
    season = Prompt.ask("Select season", choices=SEASONS, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    filter_by = Prompt.ask(
        "Filter by",
        choices=["team", "nationality"],
        default="team",
    )
    if filter_by == "team":
        choices = sorted({p.team for p in stats.players})
        selection_label = "team"
    else:
        choices = sorted({p.nationality for p in stats.players})
        selection_label = "nationality"

    while True:
        selection = Prompt.ask(
            f"Select {selection_label} ({'/'.join(choices)}, empty to quit)",
            default="",
        ).upper()

        if selection == "":
            break
        if selection not in choices:
            console.print(f"[red]Unknown {selection_label}.[/red]")
            continue

        table = Table(title=f"Season {season} players from {selection}")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="bold green")

        players = (
            stats.top_scorers_by_team(selection)
            if filter_by == "team"
            else stats.top_scorers_by_nationality(selection)
        )
        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.goals + player.assists),
            )

        console.print(table)


main()
