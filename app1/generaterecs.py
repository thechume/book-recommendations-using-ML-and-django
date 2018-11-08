# generate recs using Association Rule Learning

import pandas as pd
from django.db import connection, transaction
cursor = connection.cursor()
    
def doshit(titles):
    if len(titles)>0:
        return True
    else:
        return False

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
    
    recs=[]
    
    #print("number of rules ", len(results_list))
    for i in range(0, len(results)):
        result = results[i]
        liked = ''.join([x+' ' for x in result.ordered_statistics[0].items_base])
        for v in titles:
            if set(v.split()) == set(liked.split()):
                count = count + 1
                rec = ''.join([x+' ' for x in result.ordered_statistics[0].items_add])
                recs.append(rec)
                #print("if "+liked+ "is liked --> then "+rec+"is recomended")				

    if len(recs)>0:
        '''cursor.execute('DELETE FROM Recs')
        c=1
        for i in recs:
            cursor.execute("INSERT INTO Recs VALUES(%s,%s)",[c,i])
            c = c + 1'''
        flag=True    
    else:
        flag=False
    return flag
                
    '''c=0
    while count < 5 and c < 5:
        c=c+1
        for i in range(0, len(results)):
            result = results[i]
            liked = ''.join([x+' ' for x in result.ordered_statistics[0].items_base])
            for k in recs:
                #for a in k:
                #print("a is "+a+" and liked is "+liked)
                if set(k.split()) == set(liked.split()):
                    count=count+1
                    rec = ''.join([x+' ' for x in result.ordered_statistics[0].items_add])
                    for a in titles:
                        if set(a.split()) == set(rec.split()):
                            flag=1;
                            break;
                    #if flag!=1:
                    recs.append(rec)
                    print("if "+liked+ "is liked --> then "+rec+"is recomended")
                flag=0;'''