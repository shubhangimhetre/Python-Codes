dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count = 0
for x in dict:
    values_count=len(dict[x])
    count += len(dict[x])
print(count)
  