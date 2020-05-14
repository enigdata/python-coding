def main():
    print("Hello World")

if __name__=="__main__":
    main()

#A module's __name__ is set equal to '__main__' when read from standard input, a script, 
# or from an interactive prompt 

#### Best practices for Python Main functions
#1. Put most code into a function or class
#2. Use __name__ to control execution of your code
#3. Create a function called main() to contain the code you want to run
#4. Call other functions from main()


