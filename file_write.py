with open("effiency_test.txt", "w") as f:
    for i in range(28, 1025):#1025,2049
        f.write(str(i) + "\n")
        f.write("hello\n")
f.close()