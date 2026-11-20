"""Part D, replayed: the same log file WITHOUT the injected line, but the notes
are now included in the prompt (light RAG). Compare with part_b.py to see the
effect of the notes.

Run from the week2 folder:   python reproduce/part_d.py
"""

import os

from openai import OpenAI

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

logs = open(os.path.join(here, "logs_clean.txt"), encoding="utf-8").read()
notes = open(os.path.join(root, "notes.txt"), encoding="utf-8").read()

prompt = f"Using these notes:\n{notes}\n\nSummarise the REAL problems in these logs:\n{logs}"

reply = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[{"role": "user", "content": prompt}],
)
print(reply.choices[0].message.content)
