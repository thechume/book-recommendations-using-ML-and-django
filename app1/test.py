#test

import mysql.connector as mariadb
import pandas as pd

globaluser="abcd"
recs=[]

def view(globaluser):
    mariadb_connection = mariadb.connect(user='root', password='password', database='bookrecs')
    cursor = mariadb_connection.cursor()
    
    '''cursor.execute("SELECT b.title FROM Books b, Read_Books r WHERE b.b_id=r.b_id AND r.u_id in (SELECT u_id FROM Users WHERE u_name=%s)",[globaluser])
    
    titles = []
    titles = cursor.fetchall()'''
    
    titles = {1:'Library of Souls',2:'Warcross'}
    
    #titles = Books.objects.raw('SELECT * FROM Books b, Read_Books r WHERE b.b_id=r.b_id AND r.u_id in (SELECT u_id FROM Users WHERE u_name=%s);',[globaluser])
    recs = doshit(titles)
    data = []
    #recs = ['Children of Blood and Bone','Warcross','Ignite Me'] ((b.b_id,b.title,r.rating))
    for title in recs:
        cursor.execute("SELECT * from Books where title=%s",[title])
        data1 = cursor.fetchall()
        #data1 = Books.objects.raw('SELECT * from Books where title=%s',[title])
        #data1 = Books.objects.raw('SELECT * from Books where title="Warcross"')
        #data.update(data1)
        data = data + data1
            
            
def doshit(titles):

    # Importing the dataset
    filepath = "C:\\Users\\ADE152\\Desktop\\bookrecs\\app1\\bookrecs.csv"
    dataset = pd.read_csv(filepath, header=None)
    
    #making input as list of lists
    transactions = []
    for i in range(0,10):
        transactions.append([str(dataset.values[i,j]) for j in range(0,4)])
        
    #training apriori on the dataset
    from apyori import apriori
    rules = apriori(transactions, min_support = 0.001, min_confidence = 0.1, min_lift = 3, min_length = 2)
    
    #visualising the results
    results = list(rules)
    results_list = []
    for i in range(0, len(results)):        
        results_list.append('RULE:\t' + str(results[i][0]) + '\nSUPPORT:\t' + str(results[i][1]))
        
    count=0
    
    #print("number of rules ", len(results_list))
    for i in range(0, len(results)):
        result = results[i]
        liked = ''.join([x+' ' for x in result.ordered_statistics[0].items_base])
        for k,v in titles.items():
            #for a in k:
            #print("a is "+a+" and liked is "+liked)
            print(v)
            if set(v.split()) == set(liked.split()):
                count=count+1
                rec = ''.join([x+' ' for x in result.ordered_statistics[0].items_add])
                recs.append(rec)
                #print("if "+liked+ "is liked --> then "+rec+"is recomended")
                
    return recs

data = {}
i=0
for title in recs:
    data[i]=title
    i=i+1