baseFaits = []
baseRegles = []
ReglesUtiliser = []
regle=[]
def remplirBases():
    left_regle=''
    right_regle=''
    file = open("test.txt","r")
    f = file.readlines()
     
    for line in f:
        left_regle=''
        right_regle=''
        right_regle1=''
        left_regle1=''
        right_regle2=''
        regle=[]
        left_regle, right_regle = line.split("ALORS")
        right_regle = [right_regle.strip()]
        
        left_regle1,right_regle1= left_regle.split('SI')
        right_regle1 = [x.strip() for x in right_regle1.split(',')]
        
        right_regle1.remove('')
    
        
        left_regle1, right_regle2 = left_regle1.split(':')
        left_regle1 = [left_regle1.strip()]
        regle.insert(0,left_regle1)
        regle.insert(1,right_regle1)
        regle.insert(2,right_regle)
        baseRegles.append(regle)
        
        
#Ajouter un fait
def ajouterFait(f) : baseFaits.append(f)

#Ajouter règle utiliser
def ajouterRegleUt(f) : ReglesUtiliser.append(f)
#Afficher la base des Faits
def affichierBaseFaits(baseFaits) : 
    print('La base des faits: [',end=' ')
    for i in baseFaits: 
        print(i ,end=' ') ;
    print(']')

#Afficher les Règles Utiliser
def affichierReglesUtiliser(ReglesUtiliser) : 
    print('Les Regles Utiliser: [',end=' ')
    for i in ReglesUtiliser: 
        print(i ,end=' ') ;
    print(']')

#recupérer les eléments d'une liste dans un String
def listToString(conds):
    cond = ""
    for c in conds:
        cond += c + " et "
    return cond[:-3]

#Ajouter une règle  
def ajouterRegle(si , alors) : baseRegles.append([si,alors])

#Affichier la base des règles
def affichierRegles(baseRegles):
              
    for i in range(0,len(baseRegles)):                             
     print("R"+str(i+1)+": Si "+ listToString(baseRegles[i][1])+"Alors "+baseRegles[i][2][0])



#recherche si la condition se trouve dans les conséquences des règles
def rechercheCons(c): 
    i=0
    while(i < len(baseRegles)):
         if( c != baseRegles[i][2][0]): i+=1
         else: 
               return True

#Chainage avant
def chainageAvant(f):
     i=0
     j=0
     
     if(set(f).issubset(set(baseFaits))):
        print(f +" est prouve"); 
     else:
        while(i < len(baseRegles)):
            if(set(baseRegles[i][1]).issubset(set(baseFaits))):
                if(not set(baseRegles[i][2][0]).issubset(baseFaits)):
                  ajouterFait(baseRegles[i][2][0]);  
                  ajouterRegleUt(baseRegles[i][0][0])
                  print(baseRegles[i][2][0]+" est prouve")              
                baseRegles.remove(baseRegles[i]);
                
                    
            else: 
                i+=1
                
        if(i==len(baseRegles)):
                  i-=1
                  while(i >=0):
                   if(set(baseRegles[i][1]).issubset(set(baseFaits))):
                     if(not set(baseRegles[i][2][0]).issubset(baseFaits)):
                       ajouterFait(baseRegles[i][2][0])
                       ajouterRegleUt(baseRegles[i][0][0])
                       print(baseRegles[i][2][0]+" est prouve") 
                     baseRegles.remove(baseRegles[i]);
                     i-=1
                      
                    
                   else:
                         for j in range(0,len(baseRegles[i][1])) :
                            if(not set(baseRegles[i][1][j]).issubset(baseFaits)):
                               print("cond "+baseRegles[i][1][j]+" non trouve ")
                         print(baseRegles[i][2][0]+" non trouve ")
                         baseRegles.remove(baseRegles[i]);
                         i-=1
        if(baseRegles ==[]): print(f+" n'existe pas")
     
#Chainage arrière
def chainageArriere(f):
    i=0
    j=0
    if(set(f).issubset(set(baseFaits))):
        print(f +" est prouve") ;
    else:
        while(i <len(baseRegles)):
            if(f == baseRegles[i][2][0]): 
                if(set(baseRegles[i][1]).issubset(set(baseFaits))): 
                    ajouterFait(f); ajouterRegleUt(baseRegles[i][0][0]) ;print(f+" est prouve")
                    i+=1
                else:
                      while(j< len(baseRegles[i][1])):
                        if(set(baseRegles[i][1][j]).issubset(set(baseFaits))):
                             j+=1
                        else:
                            if( not rechercheCons(baseRegles[i][1][j])):
                                print("Echec de trouve la cond: "+baseRegles[i][1][j])
                                print("Echec de trouve  "+f)
                                baseRegles.remove(baseRegles[i])
                                i+=1
                                
                            else:
                                chainageArriere(baseRegles[i][1][j])
                                
                                
            else: i+=1
        
            
                 


    



ajouterFait('E')
ajouterFait('F')
remplirBases()
affichierRegles(baseRegles)
chainageAvant('C')
#chainageArriere('C')
affichierBaseFaits(baseFaits)
affichierReglesUtiliser(ReglesUtiliser)
