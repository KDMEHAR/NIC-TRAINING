"""Task 3.2: Mini-RAG simulation using a fictional SOP as the only knowledge source.

This offline demonstration retrieves the relevant SOP paragraph by keyword overlap.
It then builds a grounded answer prompt. No external LLM/API is called.
"""
from pathlib import Path
import re

SOP = [
    "Pension grievance: The applicant should provide the pension reference number and the month for which payment is missing. The grievance cell acknowledges receipt within three working days.",
    "Ration grievance: The applicant should provide the ration card number, fair price shop location, and month of the denied or short supply.",
    "Electricity grievance: The applicant should provide the consumer number, service address, and approximate date of the supply interruption."
]
STOP = {"the", "a", "an", "is", "for", "and", "to", "of", "my", "what", "how", "i", "was"}
def tokens(text):
    return {w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOP}
def retrieve(query):
    q = tokens(query)
    ranked = sorted(SOP, key=lambda p: len(q & tokens(p)), reverse=True)
    return ranked[0] if ranked and q & tokens(ranked[0]) else None

question = "My pension payment has not arrived. What details should I submit and when will I get an acknowledgment?"
context = retrieve(question)
print("Citizen query:", question)
print("\nRetrieved SOP context:\n", context or "No relevant SOP section found.")
if context:
    print("\nGrounded answer:\n"
          "According to the provided SOP, submit your pension reference number and the month for which payment is missing. "
          "The grievance cell acknowledges receipt within three working days.")
else:
    print("\nGrounded answer: The provided SOP does not contain enough information to answer.")
print("\nRAG note: In a production system, pass only the retrieved passage as context to the LLM and require citations to that passage.")
