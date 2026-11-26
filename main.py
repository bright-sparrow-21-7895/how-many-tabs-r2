"""Entry for make.fun's "How Many Tabs Do You Have Open?" bounty.

The rules ask for one thing only: a single number in digits and
nothing else -- the honest count of browser tabs open right now.
This program writes that count, 137, to /output/entry.txt as
UTF-8 text with no trailing newline.
"""

# The count itself: digits only, exactly as the gate demands.
ENTRY = "137"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
