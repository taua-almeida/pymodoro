# pymodoro

## Overview
pymodoro is a command-line interface (CLI) tool designed to help manage your time effectively using the Pomodoro Technique. This tool allows you to set work periods, short breaks, long breaks, and the number of cycles you wish to complete. Optionally, you can enable sound notifications to alert you when a timer starts or finishes. pymodoro is built with productivity in mind, making it easier for you to focus on work and rest adequately.

### Why?
Well, there are a bunch of other Pomodoro CLI tools and applications out there, but none satisfied my needs in the way I wanted. I was tired of using Pomodoro timers on my phone or through browser extensions. As a developer—and a good one at that—I love to create custom solutions and to use the terminal to show off my hacker skills. This project is born out of the desire to blend productivity with my love for the command line, creating a tool that feels right at home for developers and terminal enthusiasts alike.


## Features
Customizable work, short rest, and long rest durations
Option to set the number of cycles
Sound notifications at the start and end of each timer
Simple CLI for easy use

## Installation
pymodoro requires Python 3.11 or higher. It is recommended to install pymodoro using Poetry to handle dependencies easily.

1. __Install Poetry:__ If you don't have Poetry installed, you can install it by following the instructions on the [Poetry documentation](https://python-poetry.org/docs/#installation).
2. __Clone the pymodoro repository:__ Clone the pymodoro repository to your local machine.
3. __Install pymodoro:__ Run the following command:

```bash
poetry install
```

This command installs pymodoro along with its dependencies.

## Usage
To use pymodoro, you can run the pymodoro command followed by various options to customize your Pomodoro session

```bash
pymodoro --start
```

This command starts the Pomodoro timer with default settings (25 minutes of work, 5 minutes of short rest, 15 minutes of long rest, and 5 cycles).

### Customizing Your Session
You can customize your Pomodoro session using the following options:

- `--cycle` or `-c`: Set the number of cycles (default is 5)
- `--long-rest` or `-lr`: Set the length of long rest in minutes (default is 15)
- `--short-rest` or `-sr`: Set the length of short rest in minutes (default is 5)
- `--work` or `-w`: Set the length of work period in minutes (default is 25)
- `--play-sound` or `-ps`: Enable or disable sound notifications (enabled by default)

#### Example
To start a Pomodoro session with 4 cycles, 20 minutes of work, 3 minutes of short rest, 10 minutes of long rest, and sound notifications enabled:

```bash
pymodoro --start --cycle 4 --work 20 --short-rest 3 --long-rest 10
```

