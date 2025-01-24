def generate_all_combinations(nums=None):
    if nums is None:
        nums = [str(x) for x in range(1, 6)]

    ans = []
    def helper(cur_val, re_main_set: set, cur_list: list):
        if not re_main_set:
            ans.append(cur_list + ([str(cur_val)] if cur_val > 0 else []))
            return

        tmp_set = set(re_main_set)
        #take
        if cur_val > 0:
            cur_list.append(str(cur_val))
            for v in re_main_set:
                tmp_set.remove(v)
                helper(int(v), tmp_set, cur_list)
                tmp_set.add(v)
            cur_list.pop()

        #not take
        for v in re_main_set:
            tmp_set.remove(v)
            helper(cur_val * 10 + int(v), tmp_set, cur_list)
            tmp_set.add(v)


    helper(0, set(nums), [])
    return ans


print(generate_all_combinations())


