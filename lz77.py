def lz77_compress(data: str, search_window: int = 20, lookahead_window: int = 15) -> list:
    i = 0
    compressed = []
    while i < len(data):
        match_length = 0
        match_distance = 0
        start_window = max(0, i - search_window)
        end_lookahead = min(len(data), i + lookahead_window)

        for j in range(start_window, i):
            length = 0
            while (i + length < end_lookahead) and (data[j + length] == data[i + length]):
                length += 1
            if length > match_length:
                match_length = length
                match_distance = i - j

        next_char = data[i + match_length] if i + match_length < len(data) else ""
        compressed.append((match_distance, match_length, next_char))
        i += match_length + 1
    return compressed

def lz77_decompress(compressed: list) -> str:
    decompressed = ""
    for distance, length, next_char in compressed:
        if distance == 0 and length == 0:
            decompressed += next_char
        else:
            start_pos = len(decompressed) - distance
            for _ in range(length):
                decompressed += decompressed[start_pos]
                start_pos += 1
            decompressed += next_char
    return decompressed