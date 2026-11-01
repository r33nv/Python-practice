def main():
    name = str(input("What is your full name ")).title().strip()
    print(tidy(name))
def tidy(d):
    d = d.split()
    d = (f"{d[-1]}, {d[0]}")
    return d
main()