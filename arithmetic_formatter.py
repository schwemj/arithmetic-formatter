def arithmetic_formatter(problems: list[str], display_answers=False):

    if problems != list(problems): # error
        raise TypeError('Error: First argument has to be a list.')

    if len(problems) > 5:  # error
        raise Exception('Error: Too many problems entered.')


    # lists collecting the components of each line that will be displayed
    line_1 = []
    line_2 = []
    line_3 = []
    if display_answers:
        line_4 = []


    # start loop
    for problem in problems:

        parts = problem.split()

        if len(parts) != 3:  # error
            raise Exception('Error: Please enter two operands per problem.')

        try:
            nums = (int(parts[0]), int(parts[2]))
        except:  # error
            raise TypeError('Error: Numbers must only contain digits.')

        if nums[0] > 9999:  # error
            raise OverflowError('Error: Numbers cannot be more than four digits.')
        if nums[1] > 9999:  # error
            raise OverflowError('Error: Numbers cannot be more than four digits.')


        # assigning variables
        str_nums = (parts[0], parts[2])  # numbers as strings
        n1, n2 = len(str_nums[0]), len(str_nums[1])  # digit count of each number
        minuses = len(str(max(nums))) + 2  # determines number of dashes
        operator = parts[1]

        # calculate result
        if operator == '+':
            cal_result = sum(nums)
        elif operator == '-':
            cal_result = nums[0] - nums[1]
        else:  # error
            raise ValueError('Error: Operator must be \'+\' or \'-\'.')


        # appending values to each lines list
        if n1 > n2:  # determines whether 1st or 2nd value gets more padding
            line_1.append(' ' * 2 + str_nums[0])
            line_2.append(operator + ' ' + ' ' * (n1 - n2) + str_nums[1])
        elif n2 > n1:
            line_1.append(' ' * 2 + ' ' * (n2 - n1) + str_nums[0])
            line_2.append(operator + ' ' + str_nums[1])
        else:  # no additional padding for equal amount of digits
            line_1.append(' ' * 2 + str_nums[0])
            line_2.append(operator + ' ' + str_nums[1])

        line_3.append('-' * minuses)

        if display_answers:
            # calculate results
            if operator == '+':
                cal_result = sum(nums)
            elif operator == '-':
                cal_result = nums[0] - nums[1]
            else:  # error
                raise ValueError('Error: Operator must be \'+\' or \'-\'.')

            buffer = minuses - len(str(cal_result))
            line_4.append(' ' * buffer + str(cal_result))


    # empty result string variable
    arranged_problems = ''

    # separate loops for each list, arranging separate items into a single string
    for l1 in line_1:
        arranged_problems += (l1 + '    ')

    # add newline character after loop completes
    arranged_problems += '\n'

    for l2 in line_2:
        arranged_problems += (l2 + '    ')

    arranged_problems += '\n'

    for l3 in line_3:
        arranged_problems += (l3 + '    ')

    if display_answers:
        arranged_problems += '\n'
        for l4 in line_4:
            arranged_problems += (l4 + '    ')


    return arranged_problems
