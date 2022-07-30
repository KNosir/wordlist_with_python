import itertools
wordlist_name = input('Input your wordlist name: ')
symbol_input = input('Write your symbols (space is also symbol): ')
max_len = int(input('Input maximum lentgh of wordlist: '))
min_len = int(input('Input minimum lentgh of wordlist: '))


for i in range(min_len, max_len+1):
    for k in itertools.product(symbol_input, repeat=i):
        with open(f'{wordlist_name}.txt', 'a') as wordlist:
            words = ''.join(k) + '\n'
            wordlist.write(words)
        
else:
    print('Your wordlist is ready!')
