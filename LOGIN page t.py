
users = {
'nathan': '2313',
'geez': 'pass231',
'abebe': '092313133',
'miki': 'pl3s34d0noth4ckm3'
}

for i in range(5):
# prompt user for username and password
  username = input("Username: ")
  password = input("Password: ")
  if username in users and users[username] == password:
    print("Welcome to GTST company!")
    exit()
else:
  print("Incorrect login!")

if i == 4:
 print("Sorry, you are limited!") 
