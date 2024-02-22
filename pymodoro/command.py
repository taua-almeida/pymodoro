import os
import signal

import click
from click import Context
from rich.console import Console

from .pomodoro import signal_handler, start_timer
from .sound import sound_player

signal.signal(signal.SIGINT, signal_handler)


@click.command("")
@click.option("--start", "-s", is_flag=True, help="Start the Pomodoro timer")
@click.option("--cycle", "-c", default=5, help="Number of cycles to run, default is 5")
@click.option(
    "--long-rest",
    "-lr",
    default=15,
    help="Length of long rest in minutes, default is 15",
)
@click.option(
    "--short-rest",
    "-sr",
    default=5,
    help="Length of short rest in minutes, default is 5",
)
@click.option(
    "--work", "-w", default=25, help="Length of work period in minutes, default is 25"
)
@click.option(
    "--play-sound",
    "-ps",
    help="Play sound when timer will start and when it finishes",
    default=True,
    show_default=True,
)
@click.pass_context
def pomodoro(
    ctx: Context,
    start: bool,
    cycle: int,
    long_rest: int,
    short_rest: int,
    work: int,
    play_sound: bool = True,
) -> None:
    console = Console()
    """Pomodoro timer"""
    if start:
        console.print("\n:tomato: Starting Pomodoro", style="bold blue")
        if play_sound:
            sound_player(f"{os.getcwd()}/pymodoro/assets/timer.wav")
        for c in range(cycle):
            console.print(
                f"\nCycle {c+1} of {cycle} :hourglass_flowing_sand::",
                style="bright_blue",
            )
            start_timer(work, "Work Time! Focus!", play_sound)

            if c == cycle // 2:
                """You get a long rest after half the cycles are complete."""
                start_timer(long_rest, "Long Rest! Take a break!", play_sound)
            else:
                start_timer(short_rest, "Short Rest Time. Take a breather!", play_sound)

        console.print(
            "Pomodoro complete, press [bold yellow]R or r[/bold yellow] to restart the last session or any other key to\
            exit.",
            style="bold blue",
        )
        confirmation = click.prompt(
            "", default="N", show_default=False, prompt_suffix="", type=str
        )
        if confirmation.lower() == "r":
            console.print(
                "\n:recycling_symbol: Restarting last session... :recycling_symbol:\n",
                style="bold blue",
            )
            ctx.invoke(
                pomodoro,
                start=True,
                cycle=cycle,
                long_rest=long_rest,
                short_rest=short_rest,
                work=work,
            )
        else:
            console.print("\nGoodbye! :wave:", style="bold blue")
            return

    else:
        console.print("Use --start to run the Pomodoro timer.", style="bold red")
