from django.shortcuts import render
import pandas as pd

def home(request):
	if request.method=='POST':
		f=request.FILES['jfile']
		df=pd.read_json(f)
		df2=df.to_csv()
		fobj=open('new.csv','w')
		fobj.write(df2)
		fobj.close()

	return render(request,'index.html')
