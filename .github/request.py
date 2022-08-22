di={"apple":100, "banana":50}
print(di.get("apple"))

feedback={"title": "Experienced salespeople", 
"name": "Alex H.", "date": "2020-02-02", 
"feedback": "It was great to talk to the salespeople in the team, they understood my needs and were able to guide me in the right direction"}
print(feedback.get('title'))

li=[{'name':'Ian Li',"username":'ili', "phone":{"cell":'04-24630538', "tele":'0988145070'}, "department":"AV"},
{'name':'Joan Cheng',"username":'jc', "phone":{"cell":'04-8888888', "tele":'058666577'}, "department":"IT"}]
print(li[1])
print('--------------------------------------------------------------------------------------------------------------------------------------')

print('-----------------------------------------------------------------------------------------')



print('----------------------------------------------------------------------------')
import os
import requests

home=os.path.expanduser('~')
path=r'/data/feedback'
fileslist=os.listdir(path)
all=[]
for file in fileslist:
    feed={}
    with open(os.path.join(path, file),'r+') as f:
        reader=f.readlines()
        feed['title']=reader[0].replace('\n','')
        feed['name']=reader[1].replace('\n','')
        feed['date']=reader[2].replace('\n','')
        feed['feedback']=reader[3].replace('\n','')
    print(feed)
    
    response = requests.post("http://34.173.42.243/feedback/",json = feed)
    




