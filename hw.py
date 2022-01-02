class Judge:
    def __init__(self, answer: str) -> None:
        self.answer = answer
        self.answerlen = len(answer)
    def guess(self, num: str) -> bool:
        A, B =0, 0
        for i in range(self.answerlen):
            for j in range(self.answerlen):
                if num[i] == self.answer[j]:
                    if i == j:
                        A += 1
                    else:
                        B += 1
        print(f"Your guess is {num}; the result is {A}A{B}B")
        if A == self.answerlen:
            return True
        else:
            return False
def read_input(guess_len: int) -> str:
    print("Enter your guess:")
    while True:
        guess = input()
        Havechar = False
        twonum = False
        if len(guess) != guess_len:
            print("Invalid, please enter your guess again:")
            continue
        c = [0,0,0,0,0,0,0,0,0,0]
        for i in range(len(guess)):
            if guess[i] == "0":
                c[0] += 1
            elif guess[i] == "1":
                c[1] += 1
            elif guess[i] == "2":
                c[2] += 1
            elif guess[i] == "3":
                c[3] += 1
            elif guess[i] == "4":
                c[4] += 1
            elif guess[i] == "5":
                c[5] += 1
            elif guess[i] == "6":
                c[6] += 1
            elif guess[i] == "7":
                c[7] += 1
            elif guess[i] == "8":
                c[8] += 1
            elif guess[i] == "9":
                c[9] += 1
            else:
                print("Invalid, please enter your guess again:")
                Havechar = True
                break
        for i in range(10):
            if c[i] > 1 and Havechar == False:
                twonum = True
                print("Invalid, please enter your guess again:")
                break
        if Havechar == True or twonum == True:
            continue
        return guess

def enter_answer() -> str:
    answer = input()
    return answer