import unittest
from PatternRecognitionAgent import PatternRecognitionAgent


class TestPatternRecognitionAgent(unittest.TestCase):

    def test_no_overlap(self):
        agent = PatternRecognitionAgent("001110111101", "01110", allow_overlap=False)
        agent.detect_pattern()
        self.assertEqual(agent.output, "000001000000")
        self.assertEqual(agent.match_positions, [6])

    def test_with_overlap(self):
        agent = PatternRecognitionAgent("11010110", "101", allow_overlap=True)
        agent.detect_pattern()
        self.assertEqual("00010100", agent.output)
        self.assertEqual(agent.match_positions, [4, 6])

    def test_no_matches(self):
        agent = PatternRecognitionAgent("1111111", "1001")
        agent.detect_pattern()
        self.assertEqual("0000000", agent.output)
        self.assertEqual(agent.match_positions, [])

    def test_multiple_matches_no_overlap(self):
        agent = PatternRecognitionAgent("1001001001", "1001", allow_overlap=False)
        agent.detect_pattern()
        self.assertEqual("0001000001", agent.output)
        self.assertEqual(agent.match_positions, [4, 10])

    def test_multiple_matches_with_overlap(self):
        agent = PatternRecognitionAgent("1001001001", "1001", allow_overlap=True)
        agent.detect_pattern()
        self.assertEqual("0001001001", agent.output)
        self.assertEqual(agent.match_positions, [4, 7, 10])

    def test_pattern_longer_than_input(self):
        agent = PatternRecognitionAgent("101", "1010")
        agent.detect_pattern()
        self.assertEqual(agent.output, "000")
        self.assertEqual(agent.match_positions, [])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            agent = PatternRecognitionAgent("10102", "101")
            agent.detect_pattern()

    def test_invalid_pattern(self):
        with self.assertRaises(ValueError):
            agent = PatternRecognitionAgent("10101", "10a1")
            agent.detect_pattern()

    def test_empty_pattern(self):
        with self.assertRaises(ValueError):
            agent = PatternRecognitionAgent("10101", "")
            agent.detect_pattern()


if __name__ == "__main__":
    unittest.main()
