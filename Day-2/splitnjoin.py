#with in built func
#text = input("Enter a string:")

#words = text.split()
#print("After Split: ", words)

#joined_text = "-".join(words)
#print("After join: ", joined_text)

#with funciton
def split_n_join(text):
    return "-".join(text.split())

if __name__ == "__main__":
    text = input("Enter the string: ")
    result = split_n_join(text)
print(result)

