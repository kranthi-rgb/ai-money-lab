import argparse
from ai_money_lab.hello_ai import main as hello_main
from ai_money_lab import __version__


def main():
    """AI Money Lab CLI"""

    parser = argparse.ArgumentParser(
        prog="ai-money",
        description="AI Money Lab Command Line Interface"
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show application version"
    )

    args = parser.parse_args()

    if args.version:
        print(f"AI Money Lab Version: {__version__}")
    else:
        hello_main()


if __name__ == "__main__":
    main()