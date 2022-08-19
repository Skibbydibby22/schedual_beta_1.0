with open('tempc.txt', 'w') as f:
    f.write('hi')
    f.close()
f = open('tempc.txt', 'a')
f.write('\nhellow')
f.close()