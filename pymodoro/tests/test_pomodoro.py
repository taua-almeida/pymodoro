import os
from unittest.mock import MagicMock

import pytest

from pymodoro.pomodoro import start_timer


# Fixture to mock time functions
@pytest.fixture
def mock_time(monkeypatch):
    time_mock = MagicMock()
    time_mock.side_effect = lambda: time_mock.current
    time_mock.current = 0
    monkeypatch.setattr("pymodoro.pomodoro.time.time", lambda: time_mock.current)
    return time_mock


# Fixture to mock sleep and control time flow
@pytest.fixture
def control_time_flow(mock_time):
    def advance_time(seconds):
        mock_time.current += seconds

    return advance_time


# Fixture to mock the sound_player
@pytest.fixture
def mock_sound_player(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("pymodoro.pomodoro.sound_player", mock)
    return mock


# Fixture to mock Progress
@pytest.fixture
def mock_progress(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("pymodoro.pomodoro.Progress", mock)
    return mock


"""
    Tests start here
"""


def test_start_timer_with_sound(
    mock_progress, mock_sound_player, control_time_flow, mock_time
):
    # Given
    duration = 1  # 1 minute
    message = "Test Timer"
    play_sound = True

    # Simulate the timer's progress
    control_time_flow(60)  # Advance time by 60 seconds

    # When
    start_timer(duration, message, play_sound)

    # Then
    # Verify sound_player was called correctly
    mock_sound_player.assert_called_once_with(
        f"{os.getcwd()}/pymodoro/assets/timer.wav"
    )

    # Verify Progress was initialized and used
    assert mock_progress.called
    progress_instance = mock_progress.return_value.__enter__.return_value
    progress_instance.add_task.assert_called_once_with(message, total=60)

    # Ensure the timer advances as expected
    assert mock_time.current >= 60, "Timer did not advance to 60 seconds as expected"


def test_start_timer_without_sound(
    mock_progress, mock_sound_player, control_time_flow, mock_time
):
    duration = 1
    message = "Test Timer"
    play_sound = False

    control_time_flow(60)
    start_timer(duration, message, play_sound)
    # Verify sound_player was not called
    mock_sound_player.assert_not_called()

    assert mock_progress.called
    progress_instance = mock_progress.return_value.__enter__.return_value
    progress_instance.add_task.assert_called_once_with(message, total=60)

    assert mock_time.current >= 60, "Timer did not advance to 60 seconds as expected"
