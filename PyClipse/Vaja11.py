import os

#Preimenuje file
os.rename("a.txt", "Banana.txt")


#ustvari dir
os.mkdir("test")

#CH = CHANGE - se premaknemo v 
os.chdir("test")

#naredi dir jabolko
os.mkdir("jabolko")

#ODstrani
os.rmdir("jabolko")

print("dela")