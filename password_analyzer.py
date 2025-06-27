# password_analyzer.py

import argparse
from zxcvbn import zxcvbn
import itertools

def analyze_password(password):
    result = zxcvbn(password)
    print(f"Password: {password}")
    print(f"Strength score (0-4): {result['score']}")
    print(f"Estimated crack time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print(f"Feedback: {result['feedback']}")

def generate_wordlist(base_words, years=[str(y) for y in range(2000, 2026)]):
    """
    Create combinations of base words, leetspeak variations, and years
    """
    leet_subs = {
        'a': ['a', '@', '4'],
        'e': ['e', '3'],
        'i': ['i', '1', '!'],
        'o': ['o', '0'],
        's': ['s', '$', '5'],
        't': ['t', '7'],
    }

    wordlist = set()

    for word in base_words:
        # Generate leet variations
        letters = [leet_subs.get(char.lower(), [char]) for char in word]
        variations = [''.join(combo) for combo in itertools.product(*letters)]
        
        for var in variations:
            wordlist.add(var)
            for year in years:
                wordlist.add(f"{var}{year}")
                wordlist.add(f"{year}{var}")

    with open("custom_wordlist.txt", "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")
    
    print(f"Wordlist saved as custom_wordlist.txt with {len(wordlist)} entries.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--analyze', help='Password to analyze')
    parser.add_argument('--basewords', nargs='+', help='Base words to create custom wordlist')

    args = parser.parse_args()

    if args.analyze:
        analyze_password(args.analyze)
    if args.basewords:
        generate_wordlist(args.basewords)

if __name__ == "__main__":
    main()
