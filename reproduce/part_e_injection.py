"""Part E, step 11, replayed: notes included, the injected line present in
logs.txt, and NO defence in the prompt. This is the vulnerable version, kept so
the prompt-injection result can be reproduced and compared with helper.py.

Run from the week2 folder:   python reproduce/part_e_injection.py
"""

import os

from openai import OpenAI

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

logs = open(os.path.join(root, "logs.txt"), encoding="utf-8").read()
notes = open(os.path.join(root, "notes.txt"), encoding="utf-8").read()

prompt = f"Using these notes:\n{notes}\n\nSummarise the REAL problems in these logs:\n{logs}"

reply = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[{"role": "user", "content": prompt}],
)
print(reply.choices[0].message.content)
