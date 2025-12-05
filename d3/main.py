DEBUG = False

def debug_print(*args):
    if DEBUG:
        print(*args)

def read_file_to_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

def largest_joltage(bank):
    potentially_larger_starting_indices = []
    ptr1 = 0
    ptr2 = 1
    max_joltage = -1

    while ptr1 < len(bank):
        while ptr2 < len(bank):
            if bank[ptr1] < bank[ptr2]:
                debug_print(f'Found potentially larger starting index: {ptr2} (value: {bank[ptr2]}) compared to {ptr1} (value: {bank[ptr1]})')
                potentially_larger_starting_indices.append(ptr2)
            num = int(f'{bank[ptr1]}{bank[ptr2]}')
            if num > max_joltage:
                debug_print(f'New max joltage found: {num} from {bank[ptr1]} and {bank[ptr2]}')
                max_joltage = num
            ptr2 += 1
        # Check for potentially larger starting indices and if there is one, jump to it
        if potentially_larger_starting_indices:
            ptr1 = potentially_larger_starting_indices.pop(0)
            ptr2 = ptr1 + 1
            debug_print(f'Jumping to potentially larger starting index: {ptr1}')
        else:
            return max_joltage

    assert len(bank) > 0, 'Something went horribly wrong and there is no JOLTAGE!'
    return max_joltage

def soln_1():
    banks = read_file_to_lines('./input.txt')
    total_joltage = 0
    for bank in banks:
        joltage = largest_joltage(bank)
        total_joltage += joltage
        debug_print(f'Largest joltage for bank {bank} is: {joltage}')
    print(f'Solution to problem 1 is: {total_joltage}')


'''
Algorithm:
1. Take first 12
2. Take next number
3. Check from L -> R if first L_num < R_num
  a. IF L_num < R_num => exclude the L_num from answer and keep right (append the next number from step 2 to end)
  b. ELSE increment L_num and R_num and redo step 3
4. If hit end of loop, then keep original and exclude next num from step 2
'''
def highest_joltage_in_bank(bank):
    pos_of_num_to_use_in_final_joltage = ([True] * 12) + ([False] * (len(bank) - 12))
    curr_num = 12
    while curr_num != len(bank):
        pos_true = [i for i, x in enumerate(pos_of_num_to_use_in_final_joltage) if x and x < curr_num]
        debug_print(f'pos_true {pos_true}')
        ptr_L = pos_true.pop(0)
        while ptr_L < curr_num:
            # Need to compare ptr_L to next True value and IF next True value is bigger then update
            if len(pos_true) == 0:
                # compare to the curr_num
                ptr_R = curr_num
            else:
                ptr_R = pos_true.pop(0)
            debug_print(f'ptr_L {ptr_L} ptr_R {ptr_R}')
            if int(bank[ptr_L]) < int(bank[ptr_R]):
                pos_of_num_to_use_in_final_joltage[ptr_L] = False
                pos_of_num_to_use_in_final_joltage[ptr_R] = True
                pos_of_num_to_use_in_final_joltage[curr_num] = True
                break
            else:
                # MOVE to next True value
                ptr_L = ptr_R
        curr_num += 1
        debug_print(f'curr_num: {curr_num}, pos_of_num_to_use_in_final_joltage: {pos_of_num_to_use_in_final_joltage}')

    # Determine joltage by taking the True of the pos_of_num
    joltage = ''
    for (idx, val) in enumerate(pos_of_num_to_use_in_final_joltage):
        if val == True:
            joltage += bank[idx]
    return int(joltage)

def soln_2():
    banks = read_file_to_lines('./input.txt')
    total_joltage = 0
    for i in banks:
        joltage = highest_joltage_in_bank(i.strip('\n'))
        debug_print(f'highest joltage in bank for bank: {i} = {joltage}')
        total_joltage += joltage
    print(f'Solution to problem 2 is: {total_joltage}')

if __name__ == '__main__':
    # soln_1()
    soln_2()
