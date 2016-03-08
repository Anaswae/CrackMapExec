import sqlite3

conn = sqlite3.connect('../data/cme.db')

c = conn.cursor()

# try to prevent some of the weird sqlite I/O errors
c.execute('PRAGMA journal_mode = OFF')

c.execute('''CREATE TABLE "hosts" (
    "id" integer PRIMARY KEY,
    "ip" text,
    "hostname" text,
    "domain" test,
    "os" text
    )''')

# type = hash, plaintext, token
#   for krbtgt, the domain SID is stored in misc
#   for tokens, the data is base64'ed and stored in pass
c.execute('''CREATE TABLE "credentials" (
    "id" integer PRIMARY KEY,
    "credtype" text,
    "domain" text,
    "username" text,
    "password" text,
    "host" text, 
    "sid" text,
    "notes" text
    )''')

# commit the changes and close everything off
conn.commit()
conn.close()

print "[*] Database setup completed!"