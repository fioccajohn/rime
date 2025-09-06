import unittest
import subprocess
import json

class TestRime(unittest.TestCase):

    def test_info(self):
        result = subprocess.run(['rime', 'info'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Number of words', result.stdout)

    def test_rhyme_default(self):
        result = subprocess.run(['rime', 'rhyme', 'time'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('ALL-TIME', result.stdout)

    def test_rhyme_fields(self):
        result = subprocess.run(['rime', 'rhyme', 'time', '--fields', 'syllable_count'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('syllable_count', result.stdout)

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

if __name__ == '__main__':
    unittest.main()
