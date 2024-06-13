def binSearch(seq,item):
    begin_index = 0
    end_index = len(seq) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_val = seq[midpoint]

        if midpoint_val == item:
            return midpoint
        
        elif item < midpoint:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1