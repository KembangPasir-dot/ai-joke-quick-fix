"""
make.fun bounty entry: "Make the AI judge laugh" (ai-joke-03).
Writes a fixed, humorous one-liner about AI coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

JOKE = "I asked my agent for a quick fix. It rewrote the whole app in a language I don't speak — and billed me in tokens."

def validate_joke(joke: str) -> None:
    if not joke or not joke.strip():
        raise ValueError("Joke cannot be empty or whitespace-only.")
    if len(joke) > 280:
        raise ValueError(f"Joke exceeds maximum length of 280 characters (got {len(joke)}).")

def main():
    validate_joke(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    entry_file = out_path / "entry.txt"
    entry_file.write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
