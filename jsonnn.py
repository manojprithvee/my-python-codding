import json
row={"name":"manoj","age":"12"}
json_row=json.dumps(row,indent=2)
fileh=open("sample.json","w")
fileh.write(json_row)
fileh.close()
