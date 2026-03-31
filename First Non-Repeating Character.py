# Find the first non-repeating character in a string

def first_non_repeating(s):
    char_count = {}

    # Count frequency of each character
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    # Find first character with count = 1
    for ch in s:
        if char_count[ch] == 1:
            return ch

    return None


# Input
string = "aabbcdeff"

# Function call
result = first_non_repeating(string)

# Output
if result:
    print("First non-repeating character is:", result)
else:
    print("No non-repeating character found")
