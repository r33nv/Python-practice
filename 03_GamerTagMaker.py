def main():
    name = input("what is your desired username? ")
    suffix = input("what is your desired tag? ")
    print(make_tag(name))
    print(make_tag(name,suffix))
def clean(name):
    return "_".join(name.lower().split()) 
def make_tag(name,suffix = "gg"):
    return f"{clean(name)}_{suffix}"
main()