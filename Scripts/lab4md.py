# Sample: 5 columns (with hall between 2nd and 3rd columns) and 8 raws
for i in range(8):
    print('|', end='')
    numeros = [str(1+5*i+j) for j in range(5)]
    links = [f'[{k}]({k}/README.md)' for k in numeros]
    links.insert(2, '')
    numeros.insert(2, '')
    print('|'.join(links), end='')
    print('|')
