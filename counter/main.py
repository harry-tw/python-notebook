import random
from collections import Counter, defaultdict
from typing import Dict, List
from timeit import timeit

random_nums = [random.randrange(1, 10) for _ in range(1000)]


def count_by_dict(random_nums: List[int]) -> Dict:
    result = {}
    for num in random_nums:
        if num not in result:
            result[num] = 1
        else:
            result[num] += 1
    return result


def count_by_defaultdict(random_nums: List[int]) -> Dict:
    result = defaultdict(int)
    for num in random_nums:
        result[num] += 1
    return result


def count_by_counter(random_nums: List[int]) -> Dict:
    counter = Counter()
    for num in random_nums:
        counter[num] += 1
    return counter


def count_by_counter_init(random_nums: List[int]) -> Dict:
    counter = Counter(random_nums)
    return counter


def main():
    print("count_by_dict:",
          timeit("count_by_dict(random_nums)", setup="from __main__ import count_by_dict, random_nums", number=1000))
    print("count_by_defaultdict:",
          timeit("count_by_defaultdict(random_nums)", setup="from __main__ import count_by_defaultdict, random_nums", number=1000))
    print("count_by_counter:",
          timeit("count_by_counter(random_nums)", setup="from __main__ import count_by_counter, random_nums", number=1000))
    print("counter_by_counter_init:",
          timeit("count_by_counter_init(random_nums)", setup="from __main__ import count_by_counter_init, random_nums", number=1000))


if __name__ == "__main__":
    main()
