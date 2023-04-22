def cut_text(text: str, prev_len: int) -> str:
    return text[:prev_len] + '...' if len(text) > prev_len else text
