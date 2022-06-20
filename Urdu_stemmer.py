f = open("urdufile.txt", "r", encoding="utf-8")      # Open given file of urdu
f1 = open("output.txt", "w", encoding="utf-8")      # Open file to present output
f2 = open("testfile.txt", "r", encoding="utf-8")    # Open testfile to calculate accuracy of words

data = f.read()
dictionary = {}  # For storing urdufile content
dictionary1 = {}  # For storing outputfile content
dictionary2 = {} # For storing testfile content
dictionary3 = {}
accuracy = int(0)
words = data.split(" ")
for word in words:  # Storing urdu file content to dictionary
    dictionary[word] = 1


def stem(act_word):  # Rules of stemming
    mystr = str(act_word)

    if mystr.endswith("یاں"):
        stem = mystr.removesuffix("یاں")
        dictionary1[mystr] = stem

    elif mystr.endswith("اں"):
        stem = mystr.removesuffix("اں")
        dictionary1[mystr] = stem

    elif mystr.endswith("ناک"):
        stem = mystr.removesuffix("ناک")
        dictionary1[mystr] = stem

    elif mystr.endswith("ک"):
        stem = mystr.removesuffix("ک")
        dictionary1[mystr] = stem

    elif mystr.endswith("یں"):
        stem = mystr.removesuffix("یں")
        dictionary1[mystr] = stem

    elif mystr.startswith("نا"):
        stem = mystr.removeprefix("نا")
        dictionary1[mystr] = stem

    elif mystr.endswith("نے"):
        stem = mystr.removesuffix("نے")
        dictionary1[mystr] = stem

    elif mystr.endswith("تے"):
        stem = mystr.removesuffix("تے")
        dictionary1[mystr] = stem

    elif mystr.endswith("ۓ"):
        stem = mystr.removesuffix("ۓ")
        dictionary1[mystr] = stem

    elif mystr.endswith("ے"):
        stem = mystr.removesuffix("ے")
        dictionary1[mystr] = stem

    elif mystr.endswith("وانا"):
        stem = mystr.removesuffix("وانا")
        dictionary1[mystr] = stem

    elif mystr.endswith("نا"):
        stem = mystr.removesuffix("نا")
        dictionary1[mystr] = stem

    elif mystr.endswith("یا"):
        stem = mystr.removesuffix("یا")
        dictionary1[mystr] = stem

    elif mystr.endswith("یا"):
        stem = mystr.removesuffix("یا")
        dictionary1[mystr] = stem

    elif mystr.endswith("وا"):
        stem = mystr.removesuffix("وا")
        dictionary1[mystr] = stem

    elif mystr.endswith("تا"):
        stem = mystr.removesuffix("تا")
        dictionary1[mystr] = stem

    elif mystr.endswith("ا"):
        stem = mystr.removesuffix("ا")
        dictionary1[mystr] = stem

    elif mystr.endswith("تی"):
        stem = mystr.removesuffix("تی")
        dictionary1[mystr] = stem

    elif mystr.endswith("ی"):
        stem = mystr.removesuffix("ی")
        dictionary1[mystr] = stem

    elif mystr.startswith("بد"):
        stem = mystr.removeprefix("بد")
        dictionary1[mystr] = stem

    elif mystr.endswith("دان"):
        stem = mystr.removesuffix("دان")
        dictionary1[mystr] = stem

    elif mystr.endswith("وں"):
        stem = mystr.removesuffix("وں")
        dictionary1[mystr] = stem

    elif mystr.endswith("ؤں"):
        stem = mystr.removesuffix("ؤں")
        dictionary1[mystr] = stem

    elif mystr.endswith("و"):
        stem = mystr.removesuffix("و")
        dictionary1[mystr] = stem

    else:
        dictionary1[mystr] = mystr


for i in dictionary.keys():
    if(len(i) > 2):  # Words less than length of 2 doesnot stem
        stem(i)
    else:
        dictionary1[i] = i  # Words less than length 2 will apear as they are
f1.write(f"WORDS AND STEMS OF URDU FILE AND THEIR ACCURACY\n")
f1.write(f"Stems\tWords")
for key, value in dictionary1.items():
    # Words and their stems are written tab separated
    f1.write('%s\t%s\n' % (value, key))

for line in f2:
    key, value = line.split()
    dictionary2[key] = value

total_words = int(0) 

#If testfile and output file contains same words then compare generated stem with testfile stem and if the stems are same increment accuracy value
for key, value in dictionary1.items():
    if key in dictionary2.keys():
        total_words+=1
        if value == dictionary2[key]:
            accuracy+=1

acc=accuracy*100/total_words


f1.write(f"Accurate words are: {accuracy} out of {total_words} words\n")
f1.write(f"Accuracy percentage is {acc}\n\n")

for i in dictionary2.keys():
    if(len(i) > 2):  # Words less than length of 2 doesnot stem
        stem(i)
    else:
        dictionary1[i] = i  # Words less than length 2 will apear as they are
f1.write(f"WORDS AND STEMS OF STEM FILE WORDS\n")
f1.write(f"Stems\tWords")
for key, value in dictionary1.items():
    # Words and their stems are written tab separated
    f1.write('%s\t%s\n' % (value, key))

total_words1=int(0)
accuracy1=int(0)
for key, value in dictionary1.items():
    if key in dictionary2.keys():
        total_words1+=1
        if value == dictionary2[key]:
            accuracy1+=1

acc1=accuracy1*100/total_words1
f1.write(f"Accuracy of Stem file words\n")
f1.write(f"Accurate words are: {accuracy1} out of {total_words1} words\n")
f1.write(f"Accuracy percentage is {acc1}\n")


