import random
import string

""" 
Create an algorithm that generates the following random ID pattern: XXXX-AAAA-BBBB-CCCC
Where XXXX, AAAA, BBBB and CCCC patterns are random alphanumeric
The default is a string: "XXXX-AAAA-BBBB-CCCC"
The result must be stored in a variable. For example:
$id = generarId()
id is ~ abc1-bb12-234a-bcc2
Send the repository to: join-us@lexartlabs.com with the subject: "Name of the candidate - FrontEnd Test - Algorithms"
 """


def map_array(arr: list):
    mapped_array = {'letters': [], 'numbers': [], 'highestNumber': None}
    for element in arr:
        if (type(element) is str):
            mapped_array['letters'].append(element)
        if (type(element) is int):
            mapped_array['numbers'].append(element)
            if (mapped_array['highestNumber'] is None):
                mapped_array['highestNumber'] = element
            elif (mapped_array['highestNumber'] is not None and element > mapped_array['highestNumber']):
                mapped_array['highestNumber'] = element
    return mapped_array


""" 
Create an algorithm that runs through a one-dimensional array containing letters and numbers: [ “a”, 10, “b”, “hola”, 122, 15]
Get an array containing just the letters
Get an array containing just the numbers
Get the highest number from the array above
"""


def get_random_index():
    alphabet = string.ascii_uppercase
    chunks = 4
    id = ''
    for chunk in range(chunks):
        random_index = random.randint(0, len(alphabet) - 1)
        id += chunks*alphabet[random_index]
        if (chunk is not chunks - 1):
            id += '-'
    return id


if __name__ == "__main__":
    print(map_array(['a', 10, 'b', 'hola', 122, 15]))
    print(get_random_index())
