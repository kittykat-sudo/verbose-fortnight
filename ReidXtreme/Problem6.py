import sys

def tokenize_outside_quotes(s: str):
    tokens = []
    cur = []
    in_quotes = 0
    for ch in s:
        if ch == '"':
            in_quotes ^= 1
            cur.append(ch)
        elif ch == ';' and in_quotes == 0:
            tokens.append(''.join(cur))
            cur = []
        else:
            cur.append(ch)
    tokens.append(''.join(cur))
    return tokens, in_quotes  # in_quotes==1 means unmatched opening quote at end

def is_lower_alpha(s: str) -> bool:
    return len(s) > 0 and s.isalpha() and s.islower()

def validate_pair(tok: str, can_close_missing_last_quote: bool) -> (bool, bool):
    # returns (is_valid, used_append)
    # Split on first '='
    i = tok.find('=')
    if i <= 0:
        return False, False
    key = tok[:i]
    val = tok[i+1:]
    if not is_lower_alpha(key):
        return False, False
    if not val:
        return False, False  # empty only valid if quoted ""
    if val[0] == '"':
        if len(val) >= 2 and val.endswith('"'):
            return True, False
        # Allow appending a closing quote only for the last token (caller controls via can_close_missing_last_quote)
        if can_close_missing_last_quote:
            return True, True
        return False, False
    else:
        # Unquoted value must be non-empty and contain no quotes
        if '"' in val:
            return False, False
        return True, False

def count_pairs(s: str, allow_append: bool):
    tokens, in_quotes = tokenize_outside_quotes(s)
    used_append = False
    pairs = 0
    for idx, tok in enumerate(tokens):
        # Only the last token may use the appended quote
        can_close = allow_append and (idx == len(tokens) - 1) and (in_quotes == 1)
        ok, used = validate_pair(tok, can_close)
        if ok:
            pairs += 1
            used_append = used_append or used
    edits = 1 if used_append else 0
    return pairs, edits

def solve():
    data = sys.stdin.buffer.read().splitlines()
    if not data:
        return
    t = int(data[0])
    out = []
    for i in range(1, t+1):
        s = data[i].decode('utf-8', errors='ignore')
        p0, e0 = count_pairs(s, allow_append=False)
        p1, e1 = count_pairs(s, allow_append=True)
        # Choose max pairs; tie-break by fewer edits
        if p1 > p0 or (p1 == p0 and e1 < e0):
            out.append(f"{p1} {e1}")
        else:
            out.append(f"{p0} {e0}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()