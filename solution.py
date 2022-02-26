class solution:
    @staticmethod
    def solution2(s):
        # Your code here

        # braille doesn't really "follow" unicode rules,
        # but it does follow ASCII hex rules. Probably
        # one of the simpler ways to do this is a dictionary lookup table
        letter_to_braille = {
            "a": "100000",
            "b": "110000",
            "c": "100100",
            "d": "100110",
            "e": "100010",
            "f": "110100",
            "g": "110110",
            "h": "110010",
            "i": "010100",
            "j": "010110",
            "k": "101000",
            "l": "111000",
            "m": "101100",
            "n": "101110",
            "o": "101010",
            "p": "111100",
            "q": "111110",
            "r": "111010",
            "s": "011100",
            "t": "011110",
            "u": "101001",
            "v": "111001",
            "w": "101101",
            "x": "010111",
            "y": "101111",
            "z": "101011",
            "CAP": "000001",
            " ": "000000"
        }

        # split word(s) into list of individual letters
        def split(word):
            return [char for char in word]

        list1 = split(s)

        def letter_to_ord(list):
            # this function will translate letters in a list
            # into braille values, inserting capitalization
            # marks as necessary and correctly interpreting spaces
            bin_list = []
            for letter in list:
                # ord returns the unicode value of the letter
                # https://en.wikipedia.org/wiki/List_of_Unicode_characters
                # ord(letter) == 32 when letter = ' ' (space)
                if ord(letter) == 32:
                    # if letter is space, final value needs to be 000000
                    bin_list.append(letter_to_braille.get(" "))
                    # continue stops the rest of the logic below and moves the for loop onto the next iteration
                    continue
                # if condition checks if letter is capitalized
                if ord(letter) < 91 and ord(letter) > 64:
                    # unicode values between 64 & 91 represent capital letters
                    bin_list.append(letter_to_braille.get("CAP"))
                    # then change the uppercase letter to lowercase
                    letter = letter.lower()
                    # the letter is now stored as lowercase
                bin_list.append(letter_to_braille.get(letter))

            return bin_list

        list2 = letter_to_ord(list1)
        # print(list2)

        str = ''

        for braille_string in list2:
            str += braille_string
        # print(str)
        return str