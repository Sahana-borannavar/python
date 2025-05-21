import pandas as pd
data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[24,23,27],
    'City':['New York','Los Angeles','Chicago']
}
df=pd.DataFrame(data)
print(df)
df.to_csv('employees.csv',index=False)
df.to_json('employees.json',orient='records')


# Create a CSV and JSON files with following headers emp_id,emp_name and emp_salary with 3 records

import pandas as pd
data={
    'emp_id':[24,35,67],
    'emp_name':['Alice','Bob','John'],
    'emp_salary':[20000,25000,30000]
}
df=pd.DataFrame(data)
df.to_csv('employees1.csv',index=False)
df.to_json('employees1.json',orient='records')



# To read the csv and json file
import pandas as pd
data={
    'emp_id':[24,35,67],
    'emp_name':['Alice','Bob','John'],
    'emp_salary':[20000,25000,30000]
}
df=pd.DataFrame(data)
df.to_csv('employees1.csv',index=False)
df.to_json('employees1.json',orient='records')
df_csv=pd.read_csv('employees1.csv')
pprint(df_csv)
df_json=pd.read_json('employees1.json')
print(df_json)



# To add new record to the existing table csv
import pandas as pd
data={
    'emp_id':[24,35,67],
    'emp_name':['Alice','Bob','John'],
    'emp_salary':[20000,25000,30000]
}
df=pd.DataFrame(data)
new_data=pd.DataFrame([{'emp_id':26,'emp_name':'David','emp_salary':35000}])
df_csv=pd.read_csv('employees1.csv')
df_csv=pd.concat([df_csv,new_data],ignore_index=True)
df_csv.to_csv('employees1.csv',index=False)




# To add new record to the existing table json
import pandas as pd
data={
    'emp_id':[24,35,67],
    'emp_name':['Alice','Bob','John'],
    'emp_salary':[20000,25000,30000]
}
df=pd.DataFrame(data)
new_data_json=pd.DataFrame([{'emp_id':26,'emp_name':'David','emp_salary':35000}])
df_json=pd.read_json('employees1.json')
df_json=pd.concat([df_json,new_data_json],ignore_index=True)
df_json.to_json('employees1.json',orient='records')




# to delete the record in csv
import pandas as pd
data={
    'emp_id':[24,35,67],
    'emp_name':['Alice','Bob','John'],
    'emp_salary':[20000,25000,30000]
}
df=pd.DataFrame(data)
df_csv=pd.read_csv('employees1.csv')
df_csv=df_csv[df_csv['emp_name']!='Bob']
df_csv.to_csv('employees1.csv',index=False)




# to delete the record in json
import pandas as pd
data={
    'emp_id':[24,35,67],
    'emp_name':['Alice','Bob','John'],
    'emp_salary':[20000,25000,30000]
}
df=pd.DataFrame(data)
df_json=pd.read_json('employees1.json')
df_json=df_json[df_json['emp_name']!='Bob']
df_json.to_json('employees1.json',orient='records')

 
 


import pandas as pd
data={
    'Book_id':[212,235,265],
    'Book_name':['Animal Farm','The Great Gatsby','The Little Prince'],
    'Author':['George Orwell','F. Scott Fitzgerald','Antoine'],
    'Price':[250,270,300]
}
df=pd.DataFrame(data)
# To create the csv and json file
df.to_csv('book.csv',index=False)
df.to_json('book.json',orient='records')
# To add a new record to csv
new_data=pd.DataFrame([{'Book_id':286,'Book_name':'Of Mice and Men','Author':'John Steinbeck','Price':350}])
df_csv=pd.read_csv('book.csv')
df_csv=pd.concat([df_csv,new_data],ignore_index=True)
df_csv.to_csv('book.csv',index=False)
# To add a new record to json
new_data_json=pd.DataFrame([{'Book_id':286,'Book_name':'Of Mice and Men','Author':'John Steinbeck','Price':350}])
df_json=pd.read_json('book.json')
df_json=pd.concat([df_json,new_data_json],ignore_index=True)
df_json.to_json('book.json',orient='records')
# To delete the record in csv
df_csv=pd.read_csv('book.csv')
df_csv=df_csv[df_csv['Book_name']!='Animal Farm']
df_csv.to_csv('book.csv',index=False)
# To delete the record in json
df_json=pd.read_json('book.json')
df_json=df_json[df_json['Book_name']!='Animal Farm']
df_json.to_json('book.json',orient='records')