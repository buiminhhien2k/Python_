def calculate_1(b):
    c=list(b)
    num_list=[]
    a=''
    for i in range(len(c)):
        a+=c[i]
        if c[i] in ('*','/'):
            num_list.append(a)
            a=''
        elif c[i] in ('+','-'):
            if c[i-1] in ('*','/'):
                continue
            else:
                num_list.append(a[:-1])
                a=c[i]
    for i in range(1,len(b)):
        if b[-i] in ('+','-'):
            num_list.append(b[-i:])
            break
        elif b[-i] in ('*','/'):
            num_list.append(b[-i+1:])
            break
    if num_list[0]=='':
        del(num_list[0])
    for i in range(len(num_list)-1):
        if num_list[i][-1] in ('*','/'):
            last=num_list[i][-1]
            num_list[i]=num_list[i][:-1]
            num_list[i+1]=last+num_list[i+1]
    numero_list=[]
    for i in num_list:
        if '*' in i:
            numero_list[-1]*=float(i[1:])
        elif '/' in i:
            numero_list[-1]/=float(i[1:])
        else:
            numero_list.append(float(i))
    return str(sum(numero_list))

'''the function above convert 
the equation without bracket in string-type 
into its final result'''

while True:
    equation_input=input('type your equation: ')
    if '/-(' in equation_input or '/+(' in equation_input:
        print("\tError: Please close the formula in denominator \
completely with the brackets\n\t\
Advise: Problem near index {} of your formula".format(equation_input.index('/-(')))
        continue
    elif equation_input.count('(') != equation_input.count(')'):
        print('\tError: Number of open brackets must \
be equal to number of close brackets\n\t\
Advise: Close your formulas carefully')
        continue
    else:
        break

'''The loop above is to test the string 
input with correct mathematic systax, 
so the steps below work fluently'''

eval_test=eval(equation_input)
er=equation_input
er=er.replace('-(','-1*(')
er=er.replace('+(','+1*(')
first=0
last=0
while True:
    if ')' in er:
        for i in range(len(er)):
            if er[i]=='(':
                first=i
            elif er[i]==')':
                last=i+1
                er=er.replace(er[first:last],calculate_1(er[first+1:last-1]))
                break
    else:
        print('your result is:',calculate_1(er))
        print('check with "eval()" function:',float(calculate_1(er))==float(eval_test))
        break