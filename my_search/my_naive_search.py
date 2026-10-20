def naive_search(main_string: str, pattern: str):
    M = len(pattern)
    N = len(main_string)

    for i in range(N - M + 1):
        j = 0

        while j < M:
            if main_string[i + j] != pattern[j]:
                break
            j += 1

        if j == M:
            return i

    return -1

if __name__ == "__main__":
    main_string = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    position = naive_search(main_string, pattern)

    if position != -1:
        print(f"Підрядок знайдено на позиції {position}")
    else:
        print("Підрядок не знайдено в головному рядку.")
