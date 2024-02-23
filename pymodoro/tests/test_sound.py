from unittest.mock import patch

import pytest

from pymodoro.sound import sound_player


@pytest.mark.parametrize(
    "os_name,expected_call",
    [
        ("Darwin", ["afplay", "path/to/sound.wav"]),
        ("Linux", ["aplay", "path/to/sound.wav"]),
        (
            "Windows",
            [
                "powershell",
                "(New-Object Media.SoundPlayer 'path/to/sound.wav').PlaySync()",
            ],
        ),
    ],
)
def test_sound_player(os_name, expected_call):
    with patch("pymodoro.sound.platform.system", return_value=os_name), patch(
        "pymodoro.sound.subprocess.run"
    ) as mock_run:
        sound_player("path/to/sound.wav")
        mock_run.assert_called_once_with(expected_call)


def test_sound_player_unsupported_os(capfd):
    with patch("pymodoro.sound.platform.system", return_value="Unsupported_OS"):
        sound_player("path/to/sound.wav")
        out, err = capfd.readouterr()
        assert "Unsupported OS: Unsupported_OS" in out


def test_sound_player_exception(capfd):
    exception_message = "Test exception"
    with patch("pymodoro.sound.platform.system", return_value="Linux"), patch(
        "pymodoro.sound.subprocess.run", side_effect=Exception(exception_message)
    ):
        sound_player("path/to/sound.wav")
        out, err = capfd.readouterr()
        assert f"Failed to play audio: {exception_message}" in out
