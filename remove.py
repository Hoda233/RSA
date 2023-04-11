with open('effiency_test.txt', 'w') as f:
    j=32
    while (j<=1024):
            f.write(str(j))
            f.write('\n')
            f.write('hello')
            f.write('\n')
            j+=64

f.close()
