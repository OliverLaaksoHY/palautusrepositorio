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
    season = Prompt.ask("Select season", choices=SEASONS, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    nationalities = sorted({p.nationality for p in stats.players})

    while True:
        nationality = Prompt.ask(
            f"Select nationality ({'/'.join(nationalities)}, empty to quit)",
            default="",
        ).upper()

        if nationality == "":
            break
        if nationality not in nationalities:
            console.print("[red]Unknown nationality.[/red]")
            continue

        table = Table(title=f"Season {season} players from {nationality}")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Points", justify="right", style="bold green")

        for player in stats.top_scorers_by_nationality(nationality):
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.goals + player.assists),
            )

        console.print(table)


main()
