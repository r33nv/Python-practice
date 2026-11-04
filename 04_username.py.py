def main():
    user = input("What is your username? ").split()
    print(username1(user))
def username1(first):
    first =  "_".join(first).lower()
    return first
main()