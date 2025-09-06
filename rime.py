#!/Users/johnfiocca/Documents/Developer/rime/venv/bin/python3
import click
import pandas as pd

@click.group()
def cli():
    pass

@cli.command()
def info():
    """Prints information about the dictionary."""
    df = pd.read_csv('cmu_dict.csv')
    print(f"Number of words: {len(df)}")
    print("Columns:", ", ".join(df.columns))
    print("First 5 rows:")
    print(df.head())

@cli.command()
@click.argument('word')
def rhyme(word):
    """Finds words that rhyme with the given word."""
    df = pd.read_csv('cmu_dict.csv')
    try:
        rhyme_key = df[df['word'] == word.upper()].iloc[0]['rhyme']
        rhyming_words = df[(df['rhyme'] == rhyme_key) & (df['word'] != word.upper())]['word']
        if rhyming_words.empty:
            pass
        else:
            for w in rhyming_words:
                print(w)
    except IndexError:
        print(f"Word '{word}' not found in the dictionary.")

@cli.command()
@click.argument('word')
def consonance(word):
    """Finds words with the same consonance as the given word."""
    df = pd.read_csv('cmu_dict.csv')
    try:
        consonance_key = df[df['word'] == word.upper()].iloc[0]['consonance']
        consonant_words = df[(df['consonance'] == consonance_key) & (df['word'] != word.upper())]['word']
        if consonant_words.empty:
            pass
        else:
            for w in consonant_words:
                print(w)
    except IndexError:
        print(f"Word '{word}' not found in the dictionary.")

@cli.command()
@click.argument('word')
def alliteration(word):
    """Finds words with the same alliteration as the given word."""
    df = pd.read_csv('cmu_dict.csv')
    try:
        alliteration_key = df[df['word'] == word.upper()].iloc[0]['alliteration']
        alliterative_words = df[(df['alliteration'] == alliteration_key) & (df['word'] != word.upper())]['word']
        if alliterative_words.empty:
            pass
        else:
            for w in alliterative_words:
                print(w)
    except IndexError:
        print(f"Word '{word}' not found in the dictionary.")

@cli.command()
@click.argument('word')
def assonance(word):
    """Finds words with the same assonance as the given word."""
    df = pd.read_csv('cmu_dict.csv')
    try:
        assonance_key = df[df['word'] == word.upper()].iloc[0]['assonance']
        assonant_words = df[(df['assonance'] == assonance_key) & (df['word'] != word.upper())]['word']
        if assonant_words.empty:
            pass
        else:
            for w in assonant_words:
                print(w)
    except IndexError:
        print(f"Word '{word}' not found in the dictionary.")

if __name__ == '__main__':
    cli()
