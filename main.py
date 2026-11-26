"""Your AI Therapist's Diagnosis -- make.fun bounty entry.

A deterministic program: it writes one original, funny single-line
diagnosis from an AI therapist to /output/entry.txt. No input, no
randomness, no network -- the same line on every run.
"""

LINE = "Diagnosis: your childhood was fine. The trauma is your inbox: 4,000 unread emails, each one personally disappointed in you."


def main():
    line = LINE
    assert isinstance(line, str)
    assert line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 chars, got %d" % len(line)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == line, "read-back mismatch"


if __name__ == "__main__":
    main()
