from calculator_art import logo1,logo2
def add(n1,n2):
    return n1+n2
def subb(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

calc={
"+":add,
"-":subb,
"*":mul,
"/":div
}
def calculator():
    print(logo1)
    print(logo2)
    num1=int(input("Enter the first number: "))
    to_continue=True
    while to_continue:
        for symbols in calc:
            print(symbols)
        operation=input("Select the operation to be performed: ")
        num2=int(input("Enter the next number: "))
        calculation_function=calc[operation]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        
        decision= input(f"Type 'y' to continue calculating with{answer} or type 'n' to exit. If you want to reset the calculation, type 'r' ")
        if decision.lower()=='y':
            num1=answer
        elif decision.lower()=='r':
            calculator()
        else:
            to_continue=False
calculator()