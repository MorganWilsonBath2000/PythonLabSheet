import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", type=str, help="Enter your name")
    parser.add_argument("-d", "--destination", type=str, default="", help="Enter your destination")

    args = parser.parse_args()

    print(f"Hello, {args.name}! How are you my gwee")
    print(f"You are going to {args.destination}! Have fun!")

if __name__ == "__main__":
    main()