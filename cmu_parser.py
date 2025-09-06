import pandas as pd

def parse_cmu_dict():
    """
    Parses the CMU Pronouncing Dictionary and returns a pandas DataFrame
    with columns for word, phonemes, syllable_count, stress_pattern, rhyme,
    alliteration, assonance, and consonance.
    """
    cmu_file = 'CMU Pronouncing Dictionary.txt'
    data = []
    with open(cmu_file, 'r', encoding='latin-1') as f:
        for line in f:
            if line.startswith(';;;'):
                continue
            parts = line.strip().split('  ')
            word = parts[0]
            phonemes = parts[1].split(' ')
            
            syllable_count = 0
            stress_pattern = ''
            rhyme = ''
            alliteration = ''
            assonance = []
            consonance = []

            is_first_consonant = True
            for i, phoneme in enumerate(phonemes):
                if any(char.isdigit() for char in phoneme):
                    syllable_count += 1
                    stress = ''.join(filter(str.isdigit, phoneme))
                    stress_pattern += stress
                    assonance.append(phoneme)
                    if stress == '1':
                        rhyme = ' '.join(phonemes[i:])
                else:
                    consonance.append(phoneme)
                    if is_first_consonant:
                        alliteration = phoneme
                        is_first_consonant = False

            data.append({
                'word': word,
                'phonemes': ' '.join(phonemes),
                'syllable_count': syllable_count,
                'stress_pattern': stress_pattern,
                'rhyme': rhyme,
                'alliteration': alliteration,
                'assonance': ' '.join(assonance),
                'consonance': ' '.join(consonance)
            })
            
    return pd.DataFrame(data)

if __name__ == '__main__':
    df = parse_cmu_dict()
    output_path = 'cmu_dict.csv'
    df.to_csv(output_path, index=False)
    print(f"DataFrame saved to {output_path}")
