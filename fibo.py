
def fibo_rec(n):
    """
    :param n: (int), n-tý prvek posloupnosti
    :return:
    """
    if n <= 1:
        return 1
    else:
        return (fibo_rec(n - 1) + fibo_rec(n -2))



def main():
    number = int(input("Zadej císlo: "))
    print(fibo_rec(number))

if __name__ == '__main__':
    main()
