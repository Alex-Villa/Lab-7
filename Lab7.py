def edit_distance(str1, str2, len_str1, len_str2):
    m = [[0 for x in range(len_str2 + 1)] for x in range(len_str1 + 1)]
    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            if i == 0:
                m[i][j] = j

            elif j == 0:
                m[i][j] = i

            elif str1[i-1] == str2[j-1]:
                m[i][j] = m[i-1][j-1]

            else:
                m[i][j] = 1 + min(m[i][j-1],
                                  m[i-1][j],
                                  m[i-1][j-1])

    return m[len_str1][len_str2]

def main():
    print("-_-_-_-_-_-_-_-_-_Given hardcoded strings-_-_-_-_-_-_-_-_-_")
    given_str1 = "money"
    given_str2 = "miners"
    print("First hardcoded word: " + given_str1 + "\nSecond hardcoded word: " + given_str2)
    print("\nEdit distance for hardcoded strings: " + str(edit_distance(given_str1, given_str2, len(given_str1), len(given_str2))))
    print("\n-_-_-_-_-_-_-_-_-_Given custom strings-_-_-_-_-_-_-_-_-_")
    user_str1 = input("Please type in a string to compare: ")
    user_str2 = input("Please type in another string to compare: ")
    print("Your first string: " + user_str1 + "\nYour second string: " + user_str2)
    print("\nEdit distance for user strings: " + str(edit_distance(user_str1, user_str2, len(user_str1), len(user_str2))))


main()