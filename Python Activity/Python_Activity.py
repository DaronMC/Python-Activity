def hello():
    print("Hello to you as well! ")
def goodbye():
    print("Goodbye to you as well! ")
def joke():
    print("Haha Tell you the truth i dont know any jokes thats why i am cracking up! ")
    print("Get it? Im cracking up cause im old and dont know jokes HAHA! ")

answer = input("type a answer now maybe please hello? ")

if answer == "hello":
   hello()
elif answer == "goodbye":
  goodbye()
elif answer == "joke":
    joke()
else:
    print("Not an option")