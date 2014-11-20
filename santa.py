#Secret Santa Assignments with Tidbits about each person##

import random 

players = ["name", "name2", "name3", "name4", "name5", "name6"]
couples = [["name", "name3"], ["name2", "name6"]]
tidbits = [["name", "I like animals"], 
["name2", "I like Dr. Who"], 
["name3", "Favorite movie: HOME ALONE!"], 
["name4", "Movie: Slumdog Millionaire\n Toy as a Kid: Sky Dancers"], 
["name5", "I was really into the Little Mermaid when I was a kid."],
["name6", "I was REALLY into fresh water fish and owning and caring for my fish tank."]
 ]

def removeCouples(origin, arrAux):
  for couple in couples:
    if (couple[0] == origin):
      if arrAux.count(couple[1]) > 0: #If a pair exists remove it from the auxiliary list
        arrAux.remove(couple[1])        
      return arrAux
    elif (couple[1] == origin):
      if arrAux.count(couple[0]) > 0: #If a pair exists remove it from the auxiliary list
        arrAux.remove(couple[0])      
      return arrAux

  return arrAux

def calculateSecretSantaPairs():
  randomizedPlayers = players[:] #Copy the array to a temp array
  random.shuffle(randomizedPlayers)

  for origin in players:
    aux = randomizedPlayers[:]
  
    #Remove from the temp array the current player
    if aux.count(origin) > 0:
      aux.remove(origin) 

    #Pair removed also from the temp array
    aux = removeCouples(origin, aux)      

    file = open('secrets\%s.txt' % origin,'w')
    file.write('Your secret santa is %s. \n\n' % aux[0])
    for tidbit in tidbits:
      if (tidbit[0] == aux[0]): 
        file.write("Here's a hint: \"%s\"\n" % tidbit[1])
    file.close()
    
    randomizedPlayers.remove(aux[0])

okCalculation = False

while not okCalculation:
  try:
    calculateSecretSantaPairs()
    okCalculation = True
  except IndexError:
    print "###### Error calculating pairs. Someone has been left without possible couple. Recalculating..."
	
