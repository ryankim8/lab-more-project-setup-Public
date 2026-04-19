import subprocess
import os


def test_debug_flag():
    env = os.environ.copy()
    env["GROQ_API_KEY"] = "test"
    proc = subprocess.run(
        ["python3", "chat.py", "--debug"],
        input="/ls .github\n",
        text=True,
        capture_output=True,
        env=env,
    )
    assert "[tool] /ls" in proc.stdout


def test_no_debug_flag():
    env = os.environ.copy()
    env["GROQ_API_KEY"] = "test"
    proc = subprocess.run(
        ["python3", "chat.py"],
        input="/ls .github\n",
        text=True,
        capture_output=True,
        env=env,
    )
    assert "[tool]" not in proc.stdout
    assert "workflows" in proc.stdout


def test_empty_input():
    proc = subprocess.run(
        ["python3", "chat.py"],
        input="\n",
        text=True,
        capture_output=True,
    )
    assert proc.returncode == 0
