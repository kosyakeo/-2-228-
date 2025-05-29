def cout_it (sequence) :
    dict_ cout = {}
    for i in sequence:
        i = int(i)
        if i in dict_cout:
            dict_cout[i] += 1
        else:
            dict_cout[i] = 1
    sort_nums = sorted(dict_cout.items(), key=lambda x: x[1], reverse=True)
    top_nums = sort_nums
    return top_nums
sequence = ('12345678435349536859683409483049')
print(cout_it(sequence))
