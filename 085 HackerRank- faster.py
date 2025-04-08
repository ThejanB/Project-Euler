import bisect

def precompute_rectangles():
    rectangles = []
    max_possible_total = 2 * 10**6  # Upper bound
    m = 1
    while True:
        m_part = m * (m + 1) // 2
        if m_part > (2 * max_possible_total) ** 0.5 + 2:
            break
        n = 1
        while True:
            n_part = n * (n + 1) // 2
            total = m_part * n_part
            if total > max_possible_total:
                break
            area = m * n
            rectangles.append((total, area))
            n += 1
        m += 1
    rectangles.sort()
    processed = []
    prev_total = None
    max_area = 0
    for total, area in rectangles:
        if total != prev_total:
            if prev_total is not None:
                processed.append((prev_total, max_area))
            prev_total = total
            max_area = area
        else:
            if area > max_area:
                max_area = area
    if prev_total is not None:
        processed.append((prev_total, max_area))
    # Separate into totals and max_areas
    totals = [x[0] for x in processed]
    max_areas = [x[1] for x in processed]
    return totals, max_areas

totals, max_areas = precompute_rectangles()

def solve_query(target):
    pos = bisect.bisect_left(totals, target)
    candidates = []
    if pos > 0:
        candidates.append(pos - 1)
    if pos < len(totals):
        candidates.append(pos)
    if not candidates:
        return 0
    min_diff = min(abs(totals[i] - target) for i in candidates)
    low_total = target - min_diff
    high_total = target + min_diff
    left = bisect.bisect_left(totals, low_total)
    right = bisect.bisect_right(totals, high_total) - 1
    if left > right:
        return 0
    max_area = max(max_areas[i] for i in range(left, right + 1))
    return max_area

T = int(input())
for _ in range(T):
    target = int(input())
    print(solve_query(target))