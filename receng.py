import numpy
import rawdata
data = rawdata.raw_scores

def diff(v1,v2) :
    v = numpy.zeros(len(v1))
    for i in range(len(v1)) :
       if v1[i]<0 or v2[i]<0:  
           v[i] = 0
       else :
           v[i] = v1[i] - v2[i]
    return v

class Engine(object):

   def set_data(self,data):
       self.d = data

   def create_matrix(self):
       self.matrix = numpy.zeros( (self.NP, self.NR) )
       for i in range(self.NR) :
           referee = self.referees[i]
           for j in range(self.NP) :
               paper = self.papers[j]
               if self.papers[j] not in self.d[referee] :
                   self.matrix[j,i] = -1
               else :
                   self.matrix[j,i] = self.d[referee][paper]
      
   def create_papers(self):
       p = []
       for referee in self.d.values(): 
          for paper in referee.keys() :
              p.append(paper)
       sp = set(p)
       self.papers = list(sp)
       self.NP = len(self.papers)

   def create_referees(self):
       self.referees = self.d.keys()       
       self.NR = len(self.referees)

   def similarity(self,r1,r2):      
       v1 = numpy.array(self.matrix[:,r1])
       v2 = numpy.array(self.matrix[:,r2])
#       print v1
#       print v2
       v = diff(v1,v2)   
#       print v  
       return numpy.linalg.norm( v )

   def pearson(self,r1,r2):      
       v1 = numpy.array(self.matrix[:,r1])
       v2 = numpy.array(self.matrix[:,r2])
       v1l = []
       v2l = []
       for i in range(self.NP) :
         if v1[i]>=0 and v2[i] >= 0 :
            v1l.append(v1[i])
            v2l.append(v2[i])
       if len(v1l) > 0 :
         return numpy.cov( v1l, v2l )[0,1]
       else :
         return 0
   
   def tanimoto(self,r1,r2):
       v1 = numpy.array(self.matrix[:,r1])
       v2 = numpy.array(self.matrix[:,r2])
       a = 0.
       o = 0.
       for i in range(self.NP) :
           if v1[i]>=0 and v2[i]>0 : a += 1.
           if v1[i]>=0 or  v2[i]>0 : o += 1.
       return a/o     
   
  
engine = Engine()
engine.set_data(data)
engine.create_referees()
engine.create_papers()
engine.create_matrix()
print engine.referees
print engine.papers
print engine.matrix
print engine.similarity(2,4)
print engine.pearson(2,3)
print engine.tanimoto(2,3)
