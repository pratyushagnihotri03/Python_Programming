def drop_first_last(grades):
    first, *middle, last = grades  #  Store the first element in list in first and last element in last but rest of the elements in middle
    avg = sum(middle) / len(middle)
    print(first)
    print(middle)
    print(last)
    print(avg)

drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])