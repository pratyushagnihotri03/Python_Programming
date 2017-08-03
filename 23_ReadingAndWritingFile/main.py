'''
Open new file sample.txt and
'w' is used to define action to be performed which is adding text to it
close the file at the end to save memory.
'''
fw = open('sample.txt', 'w')
#Writing a file
fw.write('writing stuff in my text file \n')
fw.write('I like to like thing that I like a lot. I like it.\n')
fw.close()

'''
Open existing file sample.txt and
'r' is used to define action to be performed which is reading text file
save the read text in some variable
close the file at the end to save memory.
'''

fr = open('sample.txt', 'r')
textFromFile = fr.read()
print(textFromFile)
fr.close()