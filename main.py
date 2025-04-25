# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.to_string())

def signupUser():
    while True:
        email = input("Enter a email to sign up (or 'exit' to quit): ")

        if email.lower() == 'exit':
            print("Exiting the signup process. Goodbye!")
            break

        with open('emails.txt', 'a') as file:
            file.write(email+"\n")

        print(f"Email {email} stored successfully!")


if __name__ == "__main__":
    signupUser()
