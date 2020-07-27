# python实现boyer-moore算法.py


class last_occurrence(object):
    """Last occurrence functor."""

    def __init__(self, pattern, alphabet):
        """Generate a dictionary with the last occurrence of each alphabet
        letter inside the pattern.

        Note: This function uses str.rfind, which already is a pattern
        matching algorithm. There are more 'basic' ways to generate this
        dictionary."""
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        """Return last position of the specified letter inside the pattern.
        Return -1 if letter not found in pattern."""
        return self.occurrences[letter]


def boyer_moore_match(text, pattern):
    """Find occurrence of pattern in text."""
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1


# TEST FUNCTION
def main():
    def show_match(text, pattern):
        print('Text:  %s' % text)
        p = boyer_moore_match(text, pattern)
        print('Match: %s%s' % ('.' * p, pattern))

    text = 'abacaabadcabacabaabb'
    pattern = 'abacab'
    show_match(text, pattern)
    print()

    text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.'
    pattern = 'dolor'
    show_match(text, pattern)
    show_match(text, pattern + 'e')


if __name__ == '__main__':
    main()
