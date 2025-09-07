#!/Users/johnfiocca/Documents/Developer/rime/venv/bin/python3
import click
import pandas as pd
import subprocess
from tabulate import tabulate

def format_and_print(df, selected_fields, output_format, table_format, visidata):
    """Formats and prints the DataFrame."""
    if visidata:
        csv_output = df[selected_fields].to_csv(index=False)
        subprocess.run(['visidata'], input=csv_output, text=True)
        return

    if output_format == 'csv':
        print(df[selected_fields].to_csv(index=False))
    elif output_format == 'json':
        print(df[selected_fields].to_json(orient='records'))
    else:
        if len(selected_fields) == 1 and selected_fields[0] == 'word':
            for w in df['word']:
                print(w)
        else:
            print(tabulate(df[selected_fields], headers='keys', tablefmt=table_format, stralign='left', showindex=False))

def find_words(df, word, key_column, fields, output_format, table_format, visidata):
    """Helper function to find words based on a key and return specified fields."""
    try:
        key_value = df[df['word'] == word.upper()].iloc[0][key_column]
        found_words_df = df[df[key_column] == key_value]

        if found_words_df.empty:
            return

        if fields == '*':
            selected_fields = df.columns.tolist()
        else:
            selected_fields = fields.split('|')
            if 'word' not in selected_fields:
                selected_fields.insert(0, 'word')
        
        format_and_print(found_words_df, selected_fields, output_format, table_format, visidata)

    except IndexError:
        print(f"Word '{word}' not found in the dictionary.")

def find_words_contain(df, word, key_column, fields, output_format, table_format, visidata):
    """Helper function to find words that contain a set of phonemes."""
    try:
        key_value_str = df[df['word'] == word.upper()].iloc[0][key_column]
        search_phonemes = set(key_value_str.split())

        def contains_all_phonemes(row_phonemes_str):
            row_phonemes = set(row_phonemes_str.split())
            if not search_phonemes:
                return not row_phonemes
            return search_phonemes.issubset(row_phonemes)

        mask = df[key_column].apply(contains_all_phonemes)
        found_words_df = df[mask]

        if found_words_df.empty:
            return

        if fields == '*':
            selected_fields = df.columns.tolist()
        else:
            selected_fields = fields.split('|')
            if 'word' not in selected_fields:
                selected_fields.insert(0, 'word')
        
        format_and_print(found_words_df, selected_fields, output_format, table_format, visidata)

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
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def rhyme(word, fields, output_format, table_format, visidata):
    """Finds words that rhyme with the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words(df, word, 'rhyme', fields, output_format, table_format, visidata)

@cli.command()
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def consonance(word, fields, output_format, table_format, visidata):
    """Finds words with the same consonance as the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words(df, word, 'consonance', fields, output_format, table_format, visidata)

@cli.command(name='consonance-contains')
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def consonance_contains(word, fields, output_format, table_format, visidata):
    """Finds words that contain the same consonants as the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words_contain(df, word, 'consonance', fields, output_format, table_format, visidata)

@cli.command()
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def alliteration(word, fields, output_format, table_format, visidata):
    """Finds words with the same alliteration as the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words(df, word, 'alliteration', fields, output_format, table_format, visidata)

@cli.command()
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def assonance(word, fields, output_format, table_format, visidata):
    """Finds words with the same assonance as the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words(df, word, 'assonance', fields, output_format, table_format, visidata)

@cli.command(name='assonance-contains')
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def assonance_contains(word, fields, output_format, table_format, visidata):
    """Finds words that contain the same assonance as the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words_contain(df, word, 'assonance', fields, output_format, table_format, visidata)

@cli.command(name='syllable-count')
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def syllable_count(word, fields, output_format, table_format, visidata):
    """Finds words with the same syllable count as the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words(df, word, 'syllable_count', fields, output_format, table_format, visidata)

@cli.command(name='stress-pattern')
@click.argument('word')
@click.option('--fields', '-f', default='*', help='Fields to return, e.g. "*" for all, or "col1|col2"')
@click.option('--format', 'output_format', type=click.Choice(['df', 'csv', 'json']), default='df', help='Output format')
@click.option('--table-format', default='simple', help='Table format for df output')
@click.option('--visidata', is_flag=True, help='Send output to visidata')
def stress_pattern(word, fields, output_format, table_format, visidata):
    """Finds words with the same stress pattern as the given word."""
    df = pd.read_csv('data/cmu_dict.csv').fillna('')
    find_words(df, word, 'stress_pattern', fields, output_format, table_format, visidata)

if __name__ == '__main__':
    cli()