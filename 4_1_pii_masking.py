"""Task 4.1: Mask common PII before sharing complaint text with an external AI API."""
import re

def mask_pii(text: str) -> str:
    # Aadhaar-like 12-digit number (optional spaces/hyphens)
    text = re.sub(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b", "[AADHAAR REDACTED]", text)
    # Indian mobile number: optional +91/91 and 10 digits
    text = re.sub(r"(?<!\d)(?:\+?91[\s-]?)?[6-9]\d{9}(?!\d)", "[PHONE REDACTED]", text)
    # Basic email address
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[EMAIL REDACTED]", text)
    return text

if __name__ == "__main__":
    complaint = "My Aadhaar is 1234 5678 9012. Call me at 9876543210 or email citizen@example.com."
    print("Original:", complaint)
    print("Masked:  ", mask_pii(complaint))
