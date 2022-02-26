def solution(s):
    # Your code here
    def split(word):
        return [char for char in word]

    list1 = split(s)
    # print(list1)

    def letter_to_ord(list):
        int_corr_list = []
        for letter in list:
            # ord returns the unicode value of the letter
            # https://en.wikipedia.org/wiki/List_of_Unicode_characters
            # ord(letter) == 32 when letter = ' ' (space)
            if ord(letter) == 32:
                # if letter is space, final value needs to be 000000
                int_corr_list.append(0)
                # continue stops the rest of the logic below and moves the for loop onto the next iteration
                continue
            # if condition checks if letter is capitalized
            if ord(letter) < 91 and ord(letter) > 64:
                # 32 is the int value of binary number{100000} 
                # in braille notation capital mark is:
                # 00
                # 00
                # 01
                # in this algorithm, that value = 32
                # we'll insert 32 into int_corr_list to insert a capitalization mark in the final braille
                int_corr_list.append(32)
                # then change the uppercase letter to lowercase
                letter = letter.lower()
                # and the for loop continues on, with the letter treated as lowercase
            unicode = ord(letter)-96
            pow2 = 1
            fin = False
            while fin == False: 
                if unicode >= 2**pow2:
                    # offset the unicode value by one, incrementing past the 2**x values
                    unicode += 1
                    # increase pow2 by 1 so it will be checked next loop
                    pow2 += 1
                else:
                    fin = True
            # add unicode value to list2
            int_corr_list.append(unicode)
            
        return int_corr_list

    list2 = letter_to_ord(list1)
    # print(list2)

    def dec_to_bin(list):
        return [bin(dec) for dec in list]

    list3 = dec_to_bin(list2)

    # print(list3)

    def slice_0b(list):
        return [num[2:] for num in list]

    list4 = slice_0b(list3)

    # print(list4)

    def bin_str_to_int(list):
        return [int(str) for str in list]

    list5 = bin_str_to_int(list4)
    # print(list5)

    def add_leading_zeroes(list):
        leading_zero_list = []
        for number in list:
            number_str = str(number)
            leading_zero_str = number_str.zfill(6)
            leading_zero_list.append(leading_zero_str)
        return leading_zero_list

    list6 = add_leading_zeroes(list5)
    print(list6)

    # def reverse_str(list):
    #     reversed_list = []
    #     for str in list:


solution('A ab cdefghijklmnopqrstuvwxyz')

# capital mark: 100000
# space: 000000
# letters: a 000001 // 1
# b 000011 // 3
# c 000101 // 5
# d 000110 // 6
# e 000111 // 7
# f 001001 // 9 it skips the power of 2s
# g 001010 // 10
# h 001011 // 11
# i 001100 // 12
# j 001101 // 13
# k 001110 // 14
# l 001111 // 15
# m 010001 // 17
