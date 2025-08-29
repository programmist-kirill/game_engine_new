import subprocess

file_path = "/home/kirill/game_engine_new/module_start_session.py"

subprocess.Popen(["gnome-terminal", "--", "python3" , file_path])