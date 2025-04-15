#Create a phonebook containing Contact Name, Primary Phone Number, 
#Secondary Phone Number, Email, Address and Other Socials (Instagram & LinkedIn)

name=input("Enter the name of the contact : ")
primary_phone_number=input("Enter the primary contact number : ")
secondary_phone_number=input("Enter the secondary contact number : ")
email=input("Enter the email address : ")
address=input("Enter the address : ")
instagram_URL=input("Enter the Instagram URL : ")
linkedIn_URL=input("Enter the linkedIn URL : ")

phonebook={}
phonebook[name]={      #created dictionary in a dictionary - the value of the key is another disctionary
    "primary_phone_number": primary_phone_number,
     "secondary_phone_number":secondary_phone_number,
     "email_adrdress":email,
     "address":address,
     "instagram url":instagram_URL,
     "linked_IN":linkedIn_URL
     }
     
print(phonebook)