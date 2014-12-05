import os
import time
import json
from Constants import Parameters
from pymongo import MongoClient






with open(Parameters.DATASET_FILE +'yelp_academic_dataset_review.json') as dataset:
    i = 0
    for line in dataset:

            data = json.loads(line)
          #  isRestaurant = business_collection.find({"_id": data["business_id"]}).count();
          #  print data['stars']
            try:
                if int(data['stars']) == 4 or int(data['stars']) == 5:
                    out = open('../pos/'+str(i)+'_'+str(data['stars'])+'.txt','w')
                    out.write(str(data["text"]))
                    out.close()
                    i=i+1
                    if i ==2500:
                        break
           #     print i
            except Exception:
                continue
         #   break
