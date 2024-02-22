import os
import time

import click
from rich.console import Console
from rich.progress import BarColumn, Progress, TextColumn, TimeRemainingColumn

from .sound import sound_player


def start_timer(duration: int, message: str, play_sound: bool) -> None:
    console = Console()
    # Define custom progress bar format
    custom_columns = [
        TextColumn("[bold green]{task.description}", justify="right"),
        BarColumn(bar_width=None, style="blue", complete_style="yellow"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%", style="yellow"),
        TimeRemainingColumn(compact=True),
    ]

    with Progress(*custom_columns, console=console) as progress:
        total_seconds = duration * 60  # Convert minutes to seconds
        task = progress.add_task(message, total=total_seconds)
        start_time = time.time()

        while not progress.finished:
            # Calculate elapsed time and update task progress
            elapsed_time = time.time() - start_time
            progress.update(task, completed=elapsed_time)
            time.sleep(1)  # Update every second

    if play_sound:
        sound_player(f"{os.getcwd()}/pymodoro/assets/timer.wav")


def signal_handler(sig, frame):
    console = Console()
    console.print("\n\nPomodoro cancelled. Goodbye!", style="bold red")
    raise click.Abort()
