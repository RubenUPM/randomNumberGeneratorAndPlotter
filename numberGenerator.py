from json import dumps as jsondumper
from random import randint as randomint


def main():
    with open("numbers.json", "w") as f:
        f.write(jsondumper({i: randomint(1, 100) for i in range(1000)}, indent=4, sort_keys=True))
    print("Successful number generation!!")


if __name__ == "__main__":
    main()
