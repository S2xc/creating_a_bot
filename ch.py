 

begin=input("Здравствуйте!\
    \nВы хотите ввести текст и увидеть его в программе? (1)\
    \nили\
    \nНаписать бота и увидеть его в действии? (2)\
    \nНапишите цифру: ")

# Условие номер 1 к begin
if begin == "1":
    
    print('\nЯзыки программирования:\nPython\nC++\nC#\nKotlin\nJavaScript\nSwift\n') 
    language=input("Ведите нужный вам язык программирования: ")
    text=input("Ведите текст : ")
    
    #Проверка на C++
    if language in ["c++","с++","С++","C++"]:
        print("\n#include <iostream>\n\
        using namespace std;\nint main()\n\
        {\ncout<< \" "+text+" \";\nreturn 0;\n}\n")  

    # Проверка на C#
    elif  language in ["с#","c#","С#","C#"]:  
        print("\nusing System;\nclass HelloWorld {\n\
            static void Main() {\n    Console.WriteLine(\" "+text+" \");\n  }\n}")  

    # Проверка на Kotlin    
    elif  language in ["котлин","Котлин","rjnkby","Rjnkby","Kotlin"]:
        print("\nfun main(args: Array<String>) {\n  print(\" "+text+" \")\n}")

    # Проверка на JavaScrip, Swift, Python  
    elif language in ['JS','JavaScript',"джава скрипт","джаваскрипт","Swift",\
         "свифт","свифт","Свифт","Сфифт","swift","Python","python","питон","пайтон"]: 
        print("\nprint(\'"+text+"\')\n")

    # Проверка на наличий Ошибок   
    else:
        print("Ведите более корректно язык программирования.")

# Условие номер 2 к begin

elif begin == "2":

    print('Вам надо введите количество условий. К примеру (if, elif, else) тут 3 условия')
    number_of_conditions = int(input())

    cell=['\nx = input()\n']
    tab = (" "*4)

    def tyt(x):
        cell.append(x)

    k1 = input("Введите условие для (if x == ' *Ваш текст '): ")
    j1 = (f"if x == ('{k1}'):")
    tyt(j1) 

    k2 = input("Что должено вывести условие if:")
    j2 = (f"{tab}print('{k2}')\n")
    tyt(j2)  

    for i in range(2, number_of_conditions):
        text_elif=input(f"Введите условля для условия {i} elif x == ' *Ваш текст ': ")
        end1 = (f"elif x == '{text_elif}':")
        tyt(end1)

        text_elif_end = input("Введите текст при выполнении elif: ")
        end2 = (f"{tab}print('{text_elif_end}')\n")
        tyt(end2)

    text_else1 = print("Если не выполнятся все остольные условия то будет выполнятся условие else")
    text_else2 = input("Введите текст который выведит else: ")
    t_else = (f"else:\n{tab}print('{text_else2}')\n")
    tyt(t_else)

    print('\n'.join(cell))
             





