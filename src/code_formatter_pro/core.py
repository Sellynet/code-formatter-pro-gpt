"""
Code Formatter Pro GPT – v0.1.0
"""
import subprocess
import tempfile


def format_code(code: str, line_length: int = 88) -> str:
    """Return code formatted by Black."""
    with tempfile.NamedTemporaryFile('w+', delete=False, suffix='.py') as tmp:
        tmp.write(code)
        tmp.flush()
        subprocess.run(
            ['black', '--line-length', str(line_length), tmp.name],
            check=True,
            capture_output=True,
        )
        tmp.seek(0)
        return tmp.read()
