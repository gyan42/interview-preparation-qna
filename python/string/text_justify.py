"""
https://www.programmersought.com/article/2079221280/

A word is a sequence of characters consisting of non-space characters.
The length of each word is greater than 0, less than or equal to maxWidth.
Enter the word array words to contain at least one word.
example:

Enter:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output:
[
    "This is an",
    "example of text",
    "justification. "
]

Example 2:

Enter:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
output:
[
    "What must be",
    "acknowledgment ",
    "shall be "
]
Explanation: Note that the format of the last line should be "shall be" instead of "shall be".
Because the last line should be left aligned, not left and right.
The second line is also left-justified because this line contains only one word.
Example 3:

Enter:
words = ["Science","is","what","we","understand","well","enough","to","explain",
"to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
output:
[
    "Science is what we",
    "understand well",
    "enough to explain to",
    "a computer. Art is",
    "everything else we",
    "do "
]

"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line = []
        lines = []
        length_used = 0

        for word in words:
            #
            if length_used + len(word) <= maxWidth:
                line.append(word)
                length_used += len(word) + 1
                # When the word can't be taken, put the line into the lines, and empty the line to put the last word into it, start a new round
            else:
                lines.append(line)
                line = [word]
                length_used = len(word) + 1

                # The last line is loaded into the lines
        lines.append(line)

        # Process before the N-1 line
        for line in lines[:-1]:
            l = sum(len(word) for word in line)
            # Special case with only one word
            if len(line) == 1:
                line[0] = line[0] + ' ' * (maxWidth - l)
                # at least two words, insert spaces after N-1 words in order, until the length is equal to the required
            else:
                while l != maxWidth:
                    for i in range(len(line) - 1):
                        line[i] = line[i] + ' '
                        l += 1
                        if l == maxWidth:
                            break
                # Process the last line separately
        s = ' '.join(lines[-1])
        if len(s) < maxWidth:
            s = s + " " * (maxWidth - len(s))

        return [''.join(line) for line in lines[:-1]] + [s]
    
    
print("\n".join(Solution().fullJustify(words =["Science","is","what","we","understand","well","enough","to","explain",
"to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20)))