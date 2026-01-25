# https://usaco.org/index.php?page=viewproblem2&cpid=1324

from collections import defaultdict

number_of_instances = int(input())

for instance_number in range(1,number_of_instances+1):

    n,c,p = map(int, input().split(' '))
    the_strings = defaultdict(list)

    noun_count = 0
    transitive_verb_count = 0
    intransitive_verb_count = 0
    conjunction_count = 0

    verbs_left = p + min(p, len(the_strings["conjunction"]))

    for string_number in range(1,n+1):

        inputted_string = input().split(' ')
        the_strings[inputted_string[1]].append(inputted_string[0])

        if inputted_string[1] == 'noun':
            noun_count += 1

        elif inputted_string[1] == 'transitive-verb':
            transitive_verb_count += 1

        elif inputted_string[1] == 'intransitive-verb':
            intransitive_verb_count += 1
        
        else:
            conjunction_count += 1
            
    
    the_strings = dict(the_strings)

    number_of_words = 0

    list_of_sentences = []

    for _ in range(intransitive_verb_count):
        if verbs_left == 1 and transitive_verb_count > 0 and noun_count > 1:
            break
        if verbs_left == 0 or noun_count == 0:
            break
        number_of_words += 2
        list_of_sentences.append(the_strings['noun'][0] + ' ' + the_strings['intransitive-verb'][0])
        noun_count -= 1
        intransitive_verb_count -= 1
        the_strings['noun'].pop(0)
        the_strings['intransitive-verb'].pop(0)
        verbs_left -= 1

    for _ in range(transitive_verb_count):
        if verbs_left == 1:
            transitive_verb_count = 1
        if transitive_verb_count == 1 or noun_count < 2:
            break
        number_of_words += 3
        list_of_sentences.append(the_strings['noun'][0] + ' ' + the_strings['transitive-verb'][0] + ' ' + the_strings['noun'][1])
        noun_count -= 2
        transitive_verb_count -= 1
        the_strings['noun'].pop(0)
        the_strings['noun'].pop(0)
        the_strings['transitive-verb'].pop(0)
        verbs_left -= 1

    if transitive_verb_count == 1 and noun_count > 1 and verbs_left > 0:
        to_add = ''

        to_add += the_strings['noun'][0] + ' '
        the_strings['noun'].pop(0)
        noun_count -= 1

        to_add += the_strings['transitive-verb'][0] + ' '
        the_strings['transitive-verb'].pop(0)
        transitive_verb_count -= 1

        number_of_words += 2

        for _ in range(noun_count):
            if _ > 0:
                to_add += ', '
            to_add += the_strings['noun'][0]
            the_strings['noun'].pop(0)
            noun_count -= 1
            number_of_words += 1
        
        list_of_sentences.append(to_add)
    
    print(list_of_sentences,the_strings,conjunction_count,number_of_words)