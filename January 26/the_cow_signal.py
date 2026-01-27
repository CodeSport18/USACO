# https://usaco.org/index.php?cpid=665&page=viewproblem2

file = open('cowsignal.in','r')

signal_lines = []

for a in file:
    m_n_k = list(map(int,a.strip().split(' ')))
    break

for a in file:
    signal_lines.append(list(a.strip()))

file.close()


the_answer = ''

for signal_line in signal_lines:

    for a in range(m_n_k[2]):
    
        for char in signal_line:
            the_answer += char*m_n_k[2]
        the_answer += '\n'

the_answer = the_answer.strip()

file = open('cowsignal.out','w')
file.write(the_answer)
file.close()