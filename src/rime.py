#!/Users/johnfiocca/Documents/Developer/rime/venv/bin/python3
import click
import pandas as pd

def find_words(df, word, key_column, fields, output_format):
    """Helper function to find words based on a key and return specified fields."""
    try:
        key_value = df[df['word'] == word.upper()].iloc[0][key_column]
        found_words_df = df[(df[key_column] == key_value) & (df['word'] != word.upper())]

        if found_words_df.empty:
            return

        if fields == '*':
            selected_fields = df.columns.tolist()
        else:
            selected_fields = fields.split('|')
            if 'word' not in selected_fields:
                selected_fields.insert(0, 'word')

        if output_format == 'csv':
            print(found_words_df[selected_fields].to_csv(index=False))
        elif output_format == 'json':
            print(found_words_df[selected_fields].to_json(orient='records'))
        else:
            if len(selected_fields) == 1 and selected_fields[0] == 'word':
                for w in found_words_df['word']:
                    print(w)
            else:
                print(found_words_df[selected_fields].to_string(index=False))

    except IndexError:
        print(f"Word '{word}' not found in the dictionary.")

@click.group()
def cli():
    pass

@cli.command()
def info():
    """Prints information about the dictionary."""
    df = pd.read_csv('data/cmu_dict.csv')
    print(f"Number of words: {len(df)}")
    print("Columns:", ", ".join(df.columns))
    print("First 5 rows:")
    print(df.head())

@cli.command()
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
def rhyme(word, fields, output_format):
    """Finds words that rhyme with the given word."""
    df = pd.read_csv('data/cmu_dict.csv')
    find_words(df, word, 'rhyme', fields, output_format)

@cli.command()
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
def consonance(word, fields, output_format):
    """Finds words with the same consonance as the given word."""
    df = pd.read_csv('data/cmu_dict.csv')
    find_words(df, word, 'consonance', fields, output_format)

@cli.command()
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
def alliteration(word, fields, output_format):
    """Finds words with the same alliteration as the given word."""
    df = pd.read_csv('data/cmu_dict.csv')
    find_words(df, word, 'alliteration', fields, output_format)

@cli.command()
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
def assonance(word, fields, output_format):
    """Finds words with the same assonance as the given word."""
    df = pd.read_csv('data/cmu_dict.csv')
    find_words(df, word, 'assonance', fields, output_format)

@cli.command(name='syllable-count')
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
def syllable_count(word, fields, output_format):
    """Finds words with the same syllable count as the given word."""
    df = pd.read_csv('data/cmu_dict.csv')
    find_words(df, word, 'syllable_count', fields, output_format)

@cli.command(name='stress-pattern')
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
def stress_pattern(word, fields, output_format):
    """Finds words with the same stress pattern as the given word."""
    df = pd.read_csv('data/cmu_dict.csv')
    find_words(df, word, 'stress_pattern', fields, output_format)

if __name__ == '__main__':
    cli()
