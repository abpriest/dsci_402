# Alexander Priest

def word_breaks(word, word_list):
        substring = ''
        for i in range(len(word)):
                #print(str(i) + ': ' + word[i])
                substring += word[i]
                if substring in word_list:
                        print(substring)
                        word_breaks(word[i+1:], word_list)
        return
