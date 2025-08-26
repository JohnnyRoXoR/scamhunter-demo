import json
import argparse


def load_scammers(path: str) -> set:
    with open(path, 'r') as f:
        return set(json.load(f))


def main():
    parser = argparse.ArgumentParser(description='Check if an address is in the scam database.')
    parser.add_argument('--address', required=True, help='The address to check')
    parser.add_argument('--database', default='scammers.json', help='Path to scammer database file')
    args = parser.parse_args()

    scammers = load_scammers(args.database)
    if args.address in scammers:
        print(f"WARNING: Address {args.address} is flagged as a scammer!")
    else:
        print(f"Address {args.address} is not in the database.")


if __name__ == '__main__':
    main()
