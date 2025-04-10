# Ask the user to enter an email address
email = input("Enter the email: ")

# Define a set of characters that are not allowed in the local part of the email
invalidchar = set("(),:;<>[\\]")

# Step 1: Check if the email has at least 6 characters
if len(email) >= 6:
    
    # Step 2: Email should not contain any spaces
    if " " in email:
        print("Wrong email. No spaces are allowed")
    else:
        # Step 3: Email must contain exactly one '@' symbol
        if ("@" in email) and (email.count("@") == 1):

            # Step 4: Split the email into local and domain parts
            localpart, domainpart = email.split("@")
            
            # Step 5: The first character of the local part must be an alphabet
            if localpart[0].isalpha():
                
                # Step 6: Local part must not start with a dot (.)
                if localpart.startswith("."):
                    print("Wrong email. Address cannot start with .")
                else:

                    # Step 7: Local part must not exceed 64 characters
                    if len(localpart) > 64:
                        print("Wrong email. Address limit reached")
                    else:

                        # Step 8: Local part must not contain any forbidden special characters
                        if(any(char in localpart for char in invalidchar)):
                            print("Wrong Email. Special characters are not allowed")
                        else:

                            # Step 9: Local part must not contain consecutive dots (..)
                            if(localpart.count("..") >= 1):
                                print("Wrong email. Consecutive Dots are not allowed")
                            else:

                                # Step 10: Domain part must not exceed 255 characters
                                if len(domainpart) >= 255:
                                    print("Wrong email. Address limit reached")
                                else:

                                    # Step 11: Domain part must not start or end with a hyphen (-)
                                    if(domainpart.startswith("-") or domainpart.endswith("-")):
                                        print("Wrong email. Hyphens are not allowed in domain part")
                                    else:

                                        # Step 12: Domain part must contain at least one dot (.)
                                        if("." in domainpart):
                                            #After passing all these tests here comes the Right email
                                            print("Right email. You can proceed now")
                                        else:
                                            print("Wrong email. Domainpart is not correct")
            else:
                print("Wrong Email. The starting letter is not a alphabet")
        else:
            print("Wrong email. @ is not there")
else:
    print("Wrong email. The email should contain 6 or more than 6 characters")