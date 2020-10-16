s = "My name is Pratyush"
print(s)

s1 = """You are my 
desiny. I cannot believe 
it, it is 2020"""
print(s1)

#indexing
print(s[2])

#Repetition
print(s*3)

print(len(s1))
print(len(s))

print(s[0:5])
print(s[0:])
print(s[:5])
print(s[-3:-1])
print(s[0:9:2])
print(s[15::-1])
print(s[::-1])

s3= "      Hey whats up Bro!     "
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

print(s.find("Pra"))
print(s.find("is", 0, len(s)))

print(s.upper())
print(s.lower())
print(s.title())