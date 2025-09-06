import unittest
import subprocess
import json

class TestRime(unittest.TestCase):

    def test_info(self):
        result = subprocess.run(['rime', 'info'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Number of words', result.stdout)

    def test_rhyme_default_fields(self):
        result = subprocess.run(['rime', 'rhyme', 'time'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('word', result.stdout)
        self.assertIn('phonemes', result.stdout)
        self.assertIn('syllable_count', result.stdout)

    def test_rhyme_fields(self):
        result = subprocess.run(['rime', 'rhyme', 'time', '--fields', 'syllable_count'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('syllable_count', result.stdout)
        self.assertNotIn('phonemes', result.stdout)

    def test_rhyme_format_csv(self):
        result = subprocess.run(['rime', 'rhyme', 'time', '--format', 'csv'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('word,phonemes,syllable_count,stress_pattern,rhyme,alliteration,assonance,consonance', result.stdout)

    def test_rhyme_format_json(self):
        result = subprocess.run(['rime', 'rhyme', 'time', '--format', 'json'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        try:
            json.loads(result.stdout)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_rhyme_format_df(self):
        result = subprocess.run(['rime', 'rhyme', 'time', '--format', 'df'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('word', result.stdout)
        self.assertIn('phonemes', result.stdout)

    def test_rhyme_table_format(self):
        result = subprocess.run(['rime', 'rhyme', 'time', '--table-format', 'grid'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('+', result.stdout) # Check for grid table format

    def test_visidata_flag(self):
        result = subprocess.run(['rime', 'rhyme', 'time', '--visidata'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()
