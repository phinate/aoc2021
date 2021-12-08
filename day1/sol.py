from typing import Counter

Counter


def main():
    with open("input") as f:
        data = [int(x) for x in f.read().split()]

    lst = [one for one, two in zip(data, data[1:]) if one - two > 0]
    print(f"answer: {len(lst)} instances of increasing")


if __name__ == "__main__":
    main()
