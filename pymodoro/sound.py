import platform
import subprocess


def sound_player(sound_file_path: str) -> None:
    try:
        os_name = platform.system()

        if os_name == "Darwin":
            # macOS
            subprocess.run(["afplay", sound_file_path])
        elif os_name == "Linux":
            # Linux
            subprocess.run(["aplay", sound_file_path])
        elif os_name == "Windows":
            # Windows
            subprocess.run(
                [
                    "powershell",
                    "(New-Object Media.SoundPlayer '{}').PlaySync()".format(
                        sound_file_path
                    ),
                ]
            )
        else:
            print(f"Unsupported OS: {os_name}")
            return
    except Exception as e:
        print(f"Failed to play audio: {e}")
