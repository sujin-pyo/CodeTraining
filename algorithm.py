class Myclass:
    def __init__(self) -> None:
        pass

    def gugudan(self):
        for i in range(2,10):
            print(f"{i}단",end="            ")
        print()
        for i in range(1,10):
            for j in range(2,10):
                print(f"{j} * {i} ={i*j:2}",end="      ")
            print()


if __name__ == "__main__":
    mc = Myclass()
    mc.gugudan()
