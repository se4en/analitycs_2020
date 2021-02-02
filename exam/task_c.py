def merge_sort(iter_object):
    cur_obj = list(iter_object)
    j = 2
    obj_len = len(cur_obj)

    while (j < obj_len):
        new_obj = []
        i = 0

        while (i+1)*j < obj_len:
            new_obj += list(sorted(cur_obj[j*i: j*(i+1)]))
            i += 1
        new_obj += list(sorted(cur_obj[j*i: obj_len]))

        cur_obj = new_obj
        j = j*2
        yield new_obj

    yield list(sorted(cur_obj))
