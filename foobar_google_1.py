def solution(s):
    example_sentence = "the quick brown fox jumps over the lazy dog"
    example_bit = '011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
    translation = dict()
    translation[' '] = '000000'
    translation['cap'] = '000001'
    for element in example_sentence:
        if element == ' ':
            example_bit = remove_first_n_characters(example_bit,6)
        else:
            translation[element] = example_bit[:6]
            example_bit = remove_first_n_characters(example_bit,6)
    toReturn = ''
    for element in s:
        if element.isupper():
            toReturn += translation['cap'] + translation[element.lower()]
        else:
            toReturn += translation[element]
    # Your code here
    return toReturn
    
def remove_first_n_characters(a_string, number_to_remove):
    return a_string[number_to_remove:]

print(solution("Braille"))
print(solution("Braille") == '000001110000111010100000010100111000111000100010')
print(solution("The quick brown fox jumps over the lazy dog") == '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110')