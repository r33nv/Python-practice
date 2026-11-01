def main():
    name = str(input("What is your full name ")).title().strip()
    tidy(name)
def tidy(d):
    d = d.split()
    d = (f"{d[-1]}, {d[0]}")
    print(d)
main()