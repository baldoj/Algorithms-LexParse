
# coding: utf-8

# In[1]:


# 
import Algorithmia
import csv
import os.path

#client = Algorithmia.client('AKIAIJJGBMHZWU6MZOAQ')


# Iterate over the allheadlines list and print each headline - debug code
#for hl in allheadlines:
#    print(hl)

# Authenticate with your API key
apiKey = "simY4kp1Rtzu0O4J63jmfIngzzo1"

# Create the Algorithmia client object
client = Algorithmia.client(apiKey)

# set URI for S3 Bucket
#uri = 's3+FrameworkAlgorithmia://framework-algorithmia-data/headlinesfile.txt'
uri = 's3+FrameworkAlgorithmia://framework-algorithmia-data/headlinesfile-5Mar2018.txt'


# check if file exists
if client.file(uri).exists():
    print("headlinesfile exists")

# get file
headlinesfile = client.file(uri).getFile().name
tempFile = open(headlinesfile)
#print(tempFile.read())

#algo = client.algo('nlp/KeywordsForDocumentSet/0.1.7')
algo = client.algo('deeplearning/Parsey/1.0.4')

# create a file to store the headlines
# will be used later for visulizing conll output
#save_path = 'D:/DataAnalytics/IN-Q-TEL/Algorithmia/'

#name_of_file = "headlinesfile-5Mar2018-conll"

#completeName = os.path.join(save_path, name_of_file+".txt")
#file = open(completeName, "w")


with open(headlinesfile) as df:  
   line = df.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = df.readline()
       input = {
        "src": line,
        #"format": "conll",
        "format": "tree",
        #"format": "graph",
        "language": "English"
         }
        
       #print(algo.pipe(input))
       print(algo.pipe(input))
   

#for h1 in allheadlines:
#    print(h1)
#    input = {
#        "src": h1,
        #"format": "conll",
#        "format": "tree",
        #"format": "graph",
#        "language": "English"
#    }
#    print(input)
#    client = Algorithmia.client('simkqDtFX4aBNiztv3lUpUd9GAQ1')
#    algo = client.algo('deeplearning/Parsey/1.0.4')
#    print(algo.pipe(input))
 
# end of code 

