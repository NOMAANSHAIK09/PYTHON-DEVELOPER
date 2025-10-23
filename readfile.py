# sd = open("sample.txt","r")
# conts = sd.read()
# print(len(conts))
# lst=conts.split(" ")
# lst=conts.split(" ,")
# print(lst)

# setw=set(lst)

# print(len(setw))
# print(setw)

# sd.close()
filename = input("entet file name:")

try:
    with open(filename,'r') as file:
        words = file.read().split()
        a=len(words)
        print(len(words))
        unique_words=sorted(set(words))
        print(len(unique_words))
        b = len(unique_words)
        z=a-b
        print("unique words :")
        
        print(z)
        for word in unique_words:
            print(word)
        
except FileNotFoundError:
    print("file not found")
