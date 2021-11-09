def get_denominator(file_name):
    try:
        with open(file_name, 'r') as f:
            for i in f:
                try:
                    if int(i) == 0:
                        print('Value can not be zero.')
                        break
                    else:
                        return int(i)
                except ValueError:
                    print("Value isn't int")
                    break
    except FileNotFoundError:
        print("File doesn't exist")


def get_list_of_numbers(denominator):
    some_list = []
    for i in list(range(1, 101)):
        if i % denominator == 0:
            some_list.append(i)
    return some_list


def get_sum(list_of_numbers):
    return sum(list_of_numbers)


def write_result(number, name_of_result_file):
    with open(name_of_result_file, 'w+') as fp:
        fp.write(str(number))


write_result((get_sum(get_list_of_numbers(get_denominator('d.txt')))), 'final_file.txt')
