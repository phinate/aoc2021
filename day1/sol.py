def main():
    with open("input") as f:
        data = [int(x) for x in f.read().split()]

    lst = [one for one, two in zip(data, data[1:]) if two - one > 0]
    print(f"answer: {len(lst)} instances of increasing")

    # part 2
    window = list(zip(data, data[1:], data[2:]))
    lst = [sum(two) - sum(one) > 0 for one, two in zip(window, window[1:])]
    print(f"sliding window comparisons: {sum(lst)} increasing instances")


if __name__ == "__main__":
    main()
