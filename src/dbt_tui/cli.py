"""Console script for dbt_tui."""
import dbt_tui

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for dbt_tui."""
    console.print("Replace this message by putting your code into "
               "dbt_tui.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
