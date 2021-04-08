
def english_to_persian():
    f=open('Assignment5\Translate_sharifi\Translate.txt')
    big_text=f.read()
    parts=big_text.split('\n')
    

    words=[]
    i=0
    while i<len(parts):
        my_dict={'english':parts[i],'persian':parts[i+1]}
        words.append(my_dict)
        i+=2


    print('data loaded')
    print('welcome dear user, please enter your text')

    user_string=input()
    user_words=user_string.split(' ')

    for j in range (len(user_words)):
        for i in range(len(words)):
            if words[i]['english']==user_words[j]:
                print(words[i]['persian'])
                break
        else:
            print(user_words[j],end=' ')

def persian_to_english():
    f=open('Assignment5\Translate_sharifi\Translate.txt')
    big_text=f.read()
    parts=big_text.split('\n')

    words=[]
    i=0
    while i<len(parts):
        my_dict={'english':parts[i],'persian':parts[i+1]}
        words.append(my_dict)
        i+=2


    print('data loaded')
    print('welcome dear user, please enter your text')
    
    
    user_string=input()
    user_words=user_string.split(' ')

    for j in range (len(user_words)):
        for i in range(len(words)):
            if words[i]['persian']==user_words[j]:
                print(words[i]['english'])
                break
        else:
            print(user_words[j],end=' ')

def add_new_word():
    f=open('Assignment5\Translate_sharifi\Translate.txt',"a")
    f.write('\n')
    english=input('please enter your english word\n')
    f.write(english)
    f.write('\n')
    persian=input('please enter your persian word\n')
    f.write(persian)
    f.close


mode=int(input('select mode: 1-english_to_persian, 2-persian_to_english, 3-add_new_word, 4-exit\n'))
if   mode==1:
    english_to_persian()
elif mode==2:
    persian_to_english()
elif mode==3:
    add_new_word()
else:
    exit()