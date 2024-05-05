
import string
def fun1(massage,shift):
    alpha=string.ascii_lowercase
    new_word=""
    for x in massage:
        if x.lower() in alpha:
            old_index=alpha.index(x.lower())
            new_index=(old_index-shift)%26
            let=alpha[new_index]
            if x.isupper(): 
                let=let.upper()
                new_word=new_word+let
            else:
                
                new_word=new_word+let
        else:
            new_word=new_word+x
    print(f"your massage is {new_word}")            
massage1=input("please input you massage  ")
shift1=int(input("please input the namper you want to shift  "))

fun1(massage1,shift1)
            
