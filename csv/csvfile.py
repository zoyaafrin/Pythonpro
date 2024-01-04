import csv
# with open('mca.csv','w',newline='') as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow (['id','name','mobile','email'])
#     data2=[
#         [1,'john',9876543234,'jhon@example.com'],
#         [1,'alex',9876543564,'alex@example.com'],
#         [1,'rolex',9876547834,'rolex@example.com'],
#     ]
#     data.writerows(data2)
# with open('mca.csv','r')as csvfile:   
#     data= csv.reader(csvfile)
#     for i in data:
#         print(i)
with open('mca1.csv','w',newline='')as csvfile:
    fieldnames=['id','name','mobile','email']
    data=csv.DictWriter(csvfile,fieldnames)
    data.writeheader()
    rows=[
        {'id':1,'name':'lijitha','mobile':9078190234,'email':'l@gmail.com'},
        {'id':2,'name':'shiva','mobile':9781905634,'email':'l@gmail.com'}
    ]
    data.writerows(rows)
                                             
with open('mca1.csv','r')as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print (row['name'])