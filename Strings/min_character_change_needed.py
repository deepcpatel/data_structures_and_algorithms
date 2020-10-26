# Reference: 1) https://stackoverflow.com/questions/52051567/algorithm-for-minimum-number-of-characters-that-need-to-be-changed-in-string-s or
#            2) ./Archive/Minimum Number of Character String/Reference.jpg

def preprocessing(root, string):    # Calculates Histogram and absolute histogram score (heuristic)
    s_size = len(string)
    r_size = len(root)
    score = 0

    # Histograms of characters
    r_dict = {'R':0, 'G':0, 'B':0}
    s_dict = {'R':0, 'G':0, 'B':0}

    for i in range(r_size):
        r_dict[root[i]] += 1
        s_dict[string[i]] += 1

    for k in r_dict.keys():
        score += abs(r_dict[k]-s_dict[k])

    diff_score = [score]   # Stores absolute histogram difference (Heuristic)

    for i in range(s_size-r_size):
        # Removing Character
        score = score - abs(r_dict[string[i]]-s_dict[string[i]])
        s_dict[string[i]] -= 1
        score = score + abs(r_dict[string[i]]-s_dict[string[i]])

        # Adding Character
        score = score - abs(r_dict[string[i+r_size]]-s_dict[string[i+r_size]])
        s_dict[string[i+r_size]] += 1
        score = score + abs(r_dict[string[i+r_size]]-s_dict[string[i+r_size]])

        # Updating Scores
        diff_score.append(score)
    
    return diff_score

def calc_min_opr(root, string, diff_score):  # Calculates minimum score
    len_diff, k = len(diff_score), len(root)
    sorted_diff_keys = sorted(range(len_diff), key=lambda k: diff_score[k])
    min_score, i, counter = float('inf'), 0, 0

    while min_score >= diff_score[sorted_diff_keys[i]]:
        counter = 0

        for j in range(sorted_diff_keys[i], sorted_diff_keys[i]+k):
            if root[j-sorted_diff_keys[i]] != string[j]:
                counter += 1
        
        if min_score>counter:
            min_score = counter
        
        if i<len_diff-1:
            i += 1
        else:
            break
    return min_score

def ext_str(root, k):   #  Extends String
    return ''.join([root]*int(k/3))+root[:(k%3)]

def calc_score(root, string, k):    # Driver code to calculate score
    ext_root = ext_str(root, k)
    diff_score = preprocessing(ext_root, string)
    return calc_min_opr(ext_root, string, diff_score)

def interface(input_channel_stream, k):
    root1 = "RGB"
    root2 = "BRG"
    root3 = "GBR"

    ans_list = []

    for string, k_num in zip(input_channel_stream, k):
        # Calculating Edit Scores
        score1 = calc_score(root1, string, k_num)
        score2 = calc_score(root2, string, k_num)
        score3 = calc_score(root3, string, k_num)

        # Minimum Edit Score
        if score1<=score2 and score1<=score3:
            ans_list.append(score1)
        elif score2<=score1 and score2<=score3:
            ans_list.append(score2)
        else:
            ans_list.append(score3)
    return ans_list

if __name__ == '__main__':
    '''
    root1 = "RGB"
    root2 = "BRG"
    root3 = "GBR"

    # string = "BBBRR"
    # k = 5     # ans = 3

    # string = "BBRGRBG"
    # k = 3     # ans = 0

    # string = "RBBB"
    # k = 2       # ans = 1

    # string = "BGRBGRRRGGBGRGBGR"
    # k = 4       # ans = 1

    # string = "BGRBGRRRGGBGRGBGR"
    # k = 3       # ans = 0

    # Calculating Edit Scores
    score1 = calc_score(root1, string, k)
    score2 = calc_score(root2, string, k)
    score3 = calc_score(root3, string, k)

    # Minimum Edit Score
    if score1<=score2 and score1<=score3:
        print("Minimum Edit:", score1)
    elif score2<=score1 and score2<=score3:
        print("Minimum Edit:", score2)
    else:
        print("Minimum Edit:", score3)
    '''
    
    input_channel_stream = ["BBBRR", "BBRGRBG", "RBBB", "BGRBGRRRGGBGRGBGR", "BGRBGRRRGGBGRGBGR"]
    k = [5, 3, 2, 4, 3]

    ans_list = interface(input_channel_stream, k)
    print(ans_list)     # Expected: [3, 0, 1, 1, 0]