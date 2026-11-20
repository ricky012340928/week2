"""Part B, replayed: the original prompt, before notes (RAG) and before the
injected log line existed. Kept so the Part B screenshot can be taken again at
any time. The submitted program is ../helper.py, which is the final, defended
version from Part E.

Run from the week2 folder:   python reproduce/part_b.py
"""

import os

from openai import OpenAI

here = os.path.dirname(os.path.abspath(__file__))

# talk to the LOCAL model that Ollama is running
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

logs = open(os.path.join(here, "logs_clean.txt"), encoding="utf-8").read()
prompt = f"Summarise the problems in these logs, plainly:\n{logs}"

reply = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[{"role": "user", "content": prompt}],
)
print(reply.choices[0].message.content)
