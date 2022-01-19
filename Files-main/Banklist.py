banks_list=["kotak","HDFC","RBL","SBI","Bank of Baroda"]
file=open("bank_list","w")
for i in banks_list:
    file.write(i+"\n")
file.close()