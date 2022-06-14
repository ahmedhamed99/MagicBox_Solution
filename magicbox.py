def find_structure(operation,length):
    valid_input = ['1', '5', '10', '20', '50', '100']
    input = []
    output = []
    result = ""
    possible_stack = 0
    length = int(int(length)/2)

    for i in operation[:length]:
        if i[0] == '1' and i[2:] in valid_input:
            input.append(i[2:])

    for i in operation[length:length+len(input)]:
        if i[0] == '2' and i[2:] in valid_input:
            output.append(i[2:])
            
    reversed_output = output[::-1]
    
    if len(output) == 0:
        return
    
    if input == output:
        possible_stack += 1
        result = 'q'

    elif input == reversed_output:
        possible_stack += 1
        result = 's'

    else:
        result = "!"

    input.sort(reverse=True,key=int)
    if input == output:
        possible_stack += 1
        result = 'p'

    if possible_stack > 1:
        result = '?'

    return result

if __name__ == "__main__":
    lines = []
    answer = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    for index, element in enumerate(lines):
        if not element.__contains__(' '):
            answer.append(find_structure(lines[index+1:],element))


    with open('Reults.txt','w') as file:
        for result in answer:
            file.write(result + '\n')
        