import json
import matplotlib.pyplot as plt


def main():
    with open("numbers.json", "r") as jf:
        numbers = json.load(jf)
        plt.bar(numbers.keys(), numbers.values())
        plt.show()


if __name__ == "__main__":
    main()
