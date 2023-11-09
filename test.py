fichier=open('etudiants.txt','w')
name='ziyad'
last='joh'
age=0
print("how much etudiant have u")
y= 2
while y>0 :
 print("enter your first name \n")
 name=input()
 print("enter your last name \n")
 last=input()
 print("enter your age")
 age=input()
 fichier.writelines('\n'+name+','+last+','+age)
 fichier=open('etudiants.txt','r')
 print(fichier.read(50))
 
 y=y-1
fichier.close()
