"""
Hangman game max 8 errors

DISCLAIMER :

the textfile 'words.txt' contains words of italian dictionary

"""
import sys,random,re,os,datetime
from EmptyString import EmptyString

from WrongChoose import WrongChoose
class Hangman:
    wrong = 0
    score = 0
    founded = []
    win = False
    filedata = "savedata.txt"
    index = 0
    game_loaded = False
    menu_top_secret = True
    def __init__(self) -> None:
        try:
            self.setup_game()
        except KeyboardInterrupt:
            print("bye bye 😢😢")
            sys.exit(0)

    

    def load_game(self) -> None:
        founded = []
        if os.path.exists(self.filedata) and os.stat(self.filedata).st_size > 0:
            score = [string.strip() for string in open(self.filedata,"r").readlines() if "total score" in string]
            print(score)
            print(open(self.filedata , "r",encoding="utf-8").read())
            index = [string.split(")")[0] for string in open(self.filedata,"r").readlines() if ")" in string]
            words = [string.strip() for string in open(self.filedata,"r").readlines() if "founded" in string]
            self.index =  int(index[len(index)-1])
            print("Which savedata do u wanna load?:")
            try:
                load = input()
                if load in index:
                    #print(load)
                    score = int(score[int(load)-2].split(":")[1])
                    self.score = score
                    words = words[int(load)-1].split(":")[1]
                    if not words == "[' ']":
                        for li in words.split(","):
                            if "]" in li:
                                founded.append(li[2:li.index("]")-1])
                            else:
                                founded.append(li[2:len(li)-1])
                    self.game_loaded = True
                else:
                    with open(self.filedata,"r") as f:
                        self.score = int(f.read().split("\n")[6].split(":")[1])
                        f.close()
            except ValueError :
                print("insert a value not str")

        else:
            self.index = 1
        self.game(0,founded)


    def errors(self,wrong,word) -> int:
        print("\n\n\nmax errors:8")
        print(f"\n\ntot errors:{wrong}")
        if wrong == 1:
            print("""  
                            |___""")
        elif wrong == 2:
            print("""    
                            |      
                            |
                            |___""")
        elif wrong == 3:
            print("""
                            |      
                            |      
                            |   
                            |
                            |___""")
        elif wrong == 4:
            print("""
                            |      
                            |     
                            |      
                            |       
                            |      
                            |
                            |___""")
        elif wrong == 5:
            print("""
                            _______
                            |/      
                            |      
                            |      
                            |      
                            |     
                            |
                            |___""")
        elif wrong == 6:
            print("""
                            _______
                            |/       |
                            |      
                            |      
                            |      
                            |      
                            |
                            |___""")
        elif wrong == 7:
            print("""
                            _______
                        |/       |
                        |       (_)
                        |       \|/
                        |       
                        |    
                        |
                        |___""")
        elif wrong == 8:
            print("""
                        _______
                        |/      |
                        |      (_)
                        |      \|/
                        |       |
                        |      / /
                        |
                        |___""")
            print("u loseeeee🤦" )
            print(f"the word is:{word}")
        return wrong

    def setup_game(self) -> None:
        
        if os.path.exists(self.filedata) and os.stat(self.filedata).st_size > 0:
            print("1)Load Game \n\n2)New Game")
            try:
                scelta = int(input())
                if scelta == 1:
                    self.load_game()
                else:
                    self.game(self.wrong,self.founded)
            except ValueError:
                print("insert value not str")
        else:
            print("New Game:")
            self.game(self.wrong,self.founded)
        


    def game(self,wrong,founded) -> None:
        print("Wanna play? y or yes / n or no")
        try:
            choose = input()
            if not choose: 
                raise EmptyString()
            while(choose == "yes" or choose == "y"):    
                with open("words.txt","r",encoding='utf-8') as f:
                    _found_it = random.choice(f.readlines())
                wrong = 0
                length_unknown_word = len(_found_it)-1
                underscore = (length_unknown_word) * "_"
                print(f"length of secret word: {length_unknown_word} letters")
                print(underscore)
                if self.menu_top_secret:
                    print(f"1)buy letter\n2)choose ur destiny\n3)back to menu\n4)secret menu🌚")
                    insert = int(input())
                else:
                    print(f"1)buy letter\n2)choose ur destiny\n3)back to menu\n")
                    insert = int(input())
                    if insert == 4:
                        raise WrongChoose("incorrect choose")
                
                while(not insert == 3):
                    if(insert == 1):
                        print("insert a char:\n")
                        char = input()
                        if char == " ": 
                            raise EmptyString()
                        print(f"char inserted:'{char}'")
                        occurrences = [occ.start() for occ in re.finditer(char,_found_it)]
                        if(not occurrences):
                            wrong+=1
                            if self.errors(wrong,_found_it) == 8:
                                break
                        if not char in underscore:
                            for occ in occurrences:
                                underscore = underscore[:occ] + char + underscore[occ+1:]
                        else:
                            print(f"the letter:'{char}' has already been writed")
                                
                        print(underscore)
                    elif insert == 2:
                        print("put the word:\n")
                        try:
                            word = input()
                            if word == " ": 
                                raise EmptyString()
                        except ValueError:
                            print("insert str not int or others values")
                        if _found_it.strip() == word.strip():
                            self.win = True
                            founded.append(word if self.win else "")
                            print("you wooonnnnnn🙂🙂🙂🎉🎉")
                            self.score+=1
                            break
                        else:
                            wrong+=1
                            if self.errors(wrong,_found_it) == 8:
                                break
                    elif insert == 4:
                        if self.menu_top_secret:
                            print("DISCLAIMER: THIS IS A SECRET MENU THAT CAN BE USE ONLY 1 TIMES FOR A GAME")
                            self.menu_top_secret= False
                            print("1)unlock the secret word\n2)reset errors to zero")
                            secret_menu = int(input())
                            if secret_menu == " ": 
                                raise EmptyString()
                            if secret_menu == 1:
                                print(f"{_found_it}\n you wooonnnn🙂🙂🙂🎉🎉")
                                self.win = True
                                self.score+=1
                                founded.append(_found_it)
                                break
                            else:
                                print("a little help....")
                                wrong=0
                                print("the errors are set to 0")
                        else:
                            raise WrongChoose("choose another options")
                        
                    else:
                        print("insert one of these three options")
                    if not "_" in underscore:
                        self.win = True
                        founded.append(_found_it if self.win else "")
                        print("you wooonnnn🙂🙂🙂🎉🎉")
                        self.score+=1
                        print(self.score)
                        break
                    if self.menu_top_secret:
                        print("1)buy letter\n2)insert word\n3)exit\n4)Secret Menu🌚")
                    else:
                        print("1)buy letter\n2)insert word\n3)exit")
                    insert = int(input())
                    if insert == " ": 
                        raise EmptyString()
                    
                else:
                    if self.win:
                        print("Save the Game? y or yes/ n or no")
                        save_me = input()
                        if save_me == "y" or save_me == "yes":
                            self.save_game(founded)
                        else:
                            print("\n\nMenu")
                            self.setup_game()
                print("\n\n\n\nWanna play again?: y or yes/n or no/Enter")
                choose = input()
            if self.win:
                print("Save the Game? y or yes/ n or no/Enter")
                save_me = input()
                if save_me == "y" or save_me == "yes":
                    self.save_game(founded)
                else:
                    sys.exit(0)
            sys.exit(0)
        except(ValueError,WrongChoose,EmptyString) as e:
            if e.__class__.__name__ == "ValueError":
                print("insert a number")
            elif e.__class__.__name__ == "WrongChoose":
                print("i gotcha yu\ncheater\n bye bye🙄🙄🙄" )
                sys.exit(0)
            elif e.__class__.__name__ == "EmptyString":
                print(e.__str__())
            else:
                sys.exit(0)
    
    def save_game(self,founded) -> None:
        founded = [p.strip() for p in founded]
        
        if not os.path.exists(self.filedata) or os.stat(self.filedata).st_size == 0:
            with open(self.filedata,"w",encoding='utf-8') as f:
                self.index+=1
                 
                f.write(f"\t\t\t\t\t\t\t\tHangman Game👨\n\n{self.index})Last Game:{datetime.datetime.now().strftime('%Y/%m/%d')}\n\nfounded:{founded}\n\ntotal score:{self.score}")
                f.close()
            sys.exit(0)
        else:
            with open(self.filedata,"a") as f:
                if not self.game_loaded:
                        index = [string.split(")")[0] for string in open(self.filedata,"r").readlines() if ")" in string]
                        self.index =  int(index[len(index)-1])
                        self.index+=1
                        f.write(f"\n\n{self.index})Last Game:{datetime.datetime.now().strftime('%Y/%m/%d')}\n\nfounded:{founded}\n\ntotal score:{self.score}")
                else:
                    self.index+=1
                    f.write(f"\n\n{self.index})Last Game:{datetime.datetime.now().strftime('%Y/%m/%d')}\n\nfounded:{founded}\n\ntotal score:{self.score}")
            f.close()
            sys.exit(0)

if __name__ == "__main__":
    Hangman()
