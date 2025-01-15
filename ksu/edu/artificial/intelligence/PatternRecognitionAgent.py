class PatternRecognitionAgent:
    """
    This class detects the pattern occurrences in the input string with option for overlapping matches.
    Each pattern match ends with '1' at its end position.
    """

    def __init__(self, input_str, pattern, allow_overlap=False):
        self.input_str = input_str
        self.pattern = pattern
        self.allow_overlap = allow_overlap
        self.output = '0' * len(input_str)
        self.match_positions = []

    def detect_pattern(self):
        # Input validation
        if not set(self.input_str).issubset({'0', '1'}):
            raise ValueError("Input string must contain only '0's and '1's")
        if not set(self.pattern).issubset({'0', '1'}):
            raise ValueError("Pattern must contain only '0's and '1's")
        if not self.pattern:
            raise ValueError("Pattern cannot be empty")
        if len(self.pattern) > len(self.input_str):
            # If pattern is longer than input, no matches possible
            return

        # Initialize output array
        output = ['0'] * len(self.input_str)
        match_positions = []

        # Search for pattern occurrences
        i = 0
        pattern_length = len(self.pattern)
        while i <= len(self.input_str) - pattern_length:
            # Extract the substring to compare
            current_substring = self.input_str[i:i + pattern_length]
            if current_substring == self.pattern:
                # Mark the end position of the pattern match
                end_pos = i + pattern_length - 1
                output[end_pos] = '1'
                match_positions.append(end_pos + 1)  # 1-based indexing

                # Move past the pattern based on overlap setting
                if self.allow_overlap:
                    # Move only one position for overlapping matches
                    i += 1
                else:
                    # Move past the entire pattern for non-overlapping matches
                    i += pattern_length
            else:
                i += 1

        # Update the output string and match positions
        self.output = ''.join(output)
        self.match_positions = match_positions

    def run_test_case(self):
        """
        Executes the pattern detection for the current test case.

        Returns:
            dict: A dictionary containing input details and results.
        """
        self.detect_pattern()
        return {
            "Input String": self.input_str,
            "Pattern": self.pattern,
            "Allow Overlap": self.allow_overlap,
            "Output": self.output,
            "Match Ends At Positions": self.match_positions
        }


# running couple of different use cases to test.
# detail testing will be under unit test class.
def run_tests():
    test_cases = [
        ("010001001001", "1001"),
        ("1001001", "1001"),
        ("1111111", "1001"),
        ("1001001001", "1001"),
        ("001110111101", "01110"),
        ("1001100110001111001001010010", "1001")
    ]

    for input_str, pattern in test_cases:
        # Test with both overlap settings
        for allow_overlap in [False, True]:
            agent = PatternRecognitionAgent(input_str, pattern, allow_overlap)
            result = agent.run_test_case()
            print(f"\n---\nTest Case:")
            print(f"Input String:         {result['Input String']}")
            print(f"Pattern:              {result['Pattern']}")
            print(f"Allow Overlap:        {result['Allow Overlap']}")
            print(f"Output String:        {result['Output']}")
            print(f"Match Ends At Positions: {result['Match Ends At Positions']}")


def test_overlapping_cases():
    print("\nSpecific overlapping pattern tests:")

    # Test case with potential overlaps
    input_str = "11010110"
    pattern = "101"

    # Test without overlap
    agent_no_overlap = PatternRecognitionAgent(input_str, pattern, allow_overlap=False)
    result_no_overlap = agent_no_overlap.run_test_case()
    print(f"\n---\nTest Case: Overlapping Patterns Allowed = False")
    print(f"Input String:         {result_no_overlap['Input String']}")
    print(f"Pattern:              {result_no_overlap['Pattern']}")
    print(f"Allow Overlap:        {result_no_overlap['Allow Overlap']}")
    print(f"Output String:        {result_no_overlap['Output']}")
    print(f"Match Ends At Positions: {result_no_overlap['Match Ends At Positions']}")

    # Test with overlap
    agent_with_overlap = PatternRecognitionAgent(input_str, pattern, allow_overlap=True)
    result_with_overlap = agent_with_overlap.run_test_case()
    print(f"\nTest Case: Overlapping Patterns Allowed = True")
    print(f"Input String:         {result_with_overlap['Input String']}")
    print(f"Pattern:              {result_with_overlap['Pattern']}")
    print(f"Allow Overlap:        {result_with_overlap['Allow Overlap']}")
    print(f"Output String:        {result_with_overlap['Output']}")
    print(f"Match Ends At Positions: {result_with_overlap['Match Ends At Positions']}")


if __name__ == "__main__":
    run_tests()
    test_overlapping_cases()
