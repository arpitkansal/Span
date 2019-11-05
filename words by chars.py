words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin","ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb","ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl","boygirdlggnh","xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx","nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop","hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx","juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr","lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo","oxgaskztzroxuntiwlfyufddl","tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp","qnagrpfzlyrouolqquytwnwnsqnmuzphne","eeilfdaookieawrrbvtnqfzcricvhpiv","sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz","yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue","hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv","cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob","qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs","qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
chars_dict = dict()
for i in chars:
    if i in chars_dict:
        chars_dict[i] += 1
    else:
        chars_dict[i]= 1

words_list_of_dict = []
for i in range(len(words)):
    dict_app = dict()
    for j in words[i]:
        if j in dict_app:
            dict_app[j] += 1
        else:
            dict_app[j] = 1
    words_list_of_dict.append(dict_app)

print(chars_dict)
print(words_list_of_dict[8])
final_len = 0
for i in range(len(words)):
    leng = 0
    flag = 0
    for key in words_list_of_dict[i]:
        r = chars_dict.get(key,-1)
        if r == -1:
            flag = 1
            break
        elif r<words_list_of_dict[i][key]:
            flag = 1
            break
        else:
            leng += words_list_of_dict[i][key]
    if flag==0 :
        print(i)
        final_len += leng

print(final_len)