#particle swarm optimization for Schwefel minimization problem

#need some python libraries
import copy
import math
from random import Random

#to setup a random number generator, we will specify a "seed" value
seed = 12345
myPRNG = Random(seed)

#to get a random number between 0 and 1, write call this:             myPRNG.random()
#to get a random number between lwrBnd and upprBnd, write call this:  myPRNG.uniform(lwrBnd,upprBnd)
#to get a random integer between lwrBnd and upprBnd, write call this: myPRNG.randint(lwrBnd,upprBnd)

#number of dimensions of problem
n = 2

#number of particles in swarm
swarmSize = 10
      
#Schwefel function to evaluate a real-valued solution x    
# note: the feasible space is an n-dimensional hypercube centered at the origin with side length = 2 * 500
               
def evaluate(x):          
      val = 0
      d = len(x)
      for i in xrange(d):
            val = val + x[i]*math.sin(math.sqrt(abs(x[i])))
                                        
      val = 418.9829*d - val         
                    
      return val                    

#the swarm will be represented as a list of positions, velocities, values, pbest, and pbest values

pos = [[] for _ in xrange(swarmSize)]      #position of particles -- will be a list of lists
vel = [[] for _ in xrange(swarmSize)]      #velocity of particles -- will be a list of lists

curValue = [] #value of current position  -- will be a list of real values
pbest = []    #particles' best historical position -- will be a list of lists
pbestVal = [] #value of pbest position  -- will be a list of real values

#initialize the swarm randomly
for i in xrange(swarmSize): #for every particle i in my swarm
      for j in xrange(n): #for every dimension j
            pos[i].append(myPRNG.uniform(-500,500))    #assign random value between -500 and 500
            vel[i].append(myPRNG.uniform(-1,1))        #assign random value between -1 and 1
            
      curValue.append(evaluate(pos[i]))   #evaluate the current position
                                                 
pBest = pos[:]  # initialize pbest to the starting position
pBestVal = curValue[:]  # initialize pbest to the starting position


          
                                                                          


