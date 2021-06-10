# import statements
import streamlit as st
import numpy as np
import pandas as pd
# adding title and text in the app

import requests
from tensorflow import keras
import numpy as np
# import time
from datetime import datetime
# from timeit import default_timer as timer

#-------------------------------------------------------------------------------
# page_bg_img = '''
# <style>
# .stApp{
# background-image: url("https://pixabay.com/vectors/mountains-panorama-forest-mountain-1412683/");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

head="""
		<div style="background-color:#1E90FF;padding:0px">
		<h2 style="color:#ffffff;text-align:center;font-weight:bold;">Prediction of Flight Fares</h2>		
		</div>
		"""
st.markdown(head,unsafe_allow_html=True)

title="""
		<div style="background-color:#ffffff;padding:0px">
		<h4 style="color:#000000;text-align:center;font-weight:bold;">NEVER JUDGE A PAGE BY IT'S COVER, TRY IT</h4>
		</div>
		"""
st.markdown(title,unsafe_allow_html=True)
st.subheader("")


#=--------------------------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")
		



name=''
st.markdown("""<b>1. Enter your name</b>""",unsafe_allow_html=True)
name=st.text_input("",key='name')
# st.write('name')
head="""
		<div style="background-color:#1E90FF;padding:0px">
		<h2 style="color:#ffffff;text-align:center;font-weight:bold;">Prediction of Flight Fares</h2>		
		</div>
		"""
st.sidebar.markdown(head,unsafe_allow_html=True)
flag=0
start=''
end=''
dep_date=pd.to_datetime("2021/08/09")

if len(name)>1:
	
	st.sidebar.markdown("""<center> <h2>Hello {} </h2></center>""".format(name),unsafe_allow_html=True)
	# st.subheader("2.Enter the Source?")
	st.markdown("""<b>2. Enter the source</b>""",unsafe_allow_html=True)

	source = st.selectbox('',('','Banglore','Chennai','Delhi','Kolkata','Mumbai'))


	if len(source)>1:
		st.info("{}, You are in such a beautiful city ".format(name))
		# st.sidebar.markdown("""- <h3><b></b></h3>""",unsafe_allow_html=True)
		st.sidebar.warning("* You selected the source")

		


		st.markdown("""<b>3. Enter the destination</b>""",unsafe_allow_html=True)
		destination = st.selectbox('',('','Banglore','Cochin','Delhi','Hyderabad','Kolkata'))

		if len(destination)>1:
			# st.sidebar.markdown("""- <h3><b></b></h3>""",unsafe_allow_html=True)
			
			if source != destination:	
				st.sidebar.warning("* You selected the destination")
				st.info("{}, {} is very good for travelling ".format(name,destination))
				st.markdown("""<b>4. Enter the Airline name</b>""",unsafe_allow_html=True)
				airline = st.selectbox('',('','Air Asia','Air India','GoAir','IndiGo','Jet Airways','Multiple carriers','Multiple carriers Premium economy','SpiceJet','Vistara'))

				if len(airline)>1:
					st.info("{}, You selected - {}".format(name, airline))
					st.sidebar.warning("* You selected the Airline")

					

				    # Destination_Banglore	Destination_Cochin	Destination_Delhi	Destination_Hyderabad	Destination_Kolkata	



					st.markdown("""<b>5. Select Departure date</b>""",unsafe_allow_html=True)
					# st.subheader("5. Enter Departure Date")
					from datetime import date
					today = date.today()

					# st.write("Today's date:", today)

					dep_date=st.date_input('')

					# weekno = dep_date.weekday()

					# if weekno < 5:
					#     # st.sidebar.markdown("""- <h3><b></b><h3>""",unsafe_allow_html=True)
					#     # st.sidebar.warning("* It's a weekday")
					# else:  # 5 Sat, 6 Sun
					#     # st.sidebar.markdown("""- <h3><b></b><h3>""",unsafe_allow_html=True)
					#     # st.sidebar.warning("* It's a weekend")


					# st.write(dep_date)

					day=dep_date.day

					month=dep_date.month


					arr=[]

					arr.append(day)
					arr.append(month)


					# st.subheader("")

					if day != today.day:
						

						st.sidebar.warning("* You selected the Departure Date")
						st.markdown("""<b>6. Select Departure hour</b>""",unsafe_allow_html=True)
						dep_hour=st.slider("Departure Hour",min_value=0,max_value=24)



						arr.append(dep_hour)

						st.markdown("""<b>7. Select Departure minute</b>""",unsafe_allow_html=True)
						dep_min=st.slider("Departure Minutes",min_value=0,max_value=60)
						
							

						arr.append(dep_min)

						if (dep_hour == 0 and dep_min != 0) or (dep_hour != 0 and dep_min == 0) or (dep_hour != 0 and dep_min != 0):


							st.sidebar.warning("* You selected the Departure Hour")

							st.sidebar.warning("* You selected the Departure Minute")
							# st.subheader("")

							st.markdown("""<b>8. Select Duration Hour</b>""",unsafe_allow_html=True)
							duration_hour=st.slider("Duration Hour",min_value=0,max_value=10)

								

							arr.append(duration_hour)

							st.markdown("""<b>9. Select Duration Minute</b>""",unsafe_allow_html=True)
							# st.subheader("")
							duration_min=st.slider("Duration Minutes",min_value=0,max_value=60)

							if (duration_hour == 0 and duration_min != 0) or (duration_hour != 0 and duration_min == 0) or (duration_hour != 0 and duration_min != 0):
								
								st.sidebar.warning("* You selected the Duration Minute")
								st.sidebar.warning("* You selected the Duration Hour")


								arr.append(duration_min)

								# st.write(arr)


								# Air Asia	Airline_Air India	Airline_GoAir	Airline_IndiGo	Airline_Jet Airways	 Airline_Multiple carriers	Airline_Multiple carriers Premium economy	Airline_SpiceJet	Airline_Vistara	





								if airline=='Air Asia':
									arr.extend([1,0,0,0,0,0,0,0,0])
								elif airline=='Air India':
								    arr.extend([0,1,0,0,0,0,0,0,0])
								elif airline=='GoAir':
									arr.extend([0,0,1,0,0,0,0,0,0])
								elif airline=='IndiGo':
								    arr.extend([0,0,0,1,0,0,0,0,0])
								elif airline=='Jet Airways':
									arr.extend([0,0,0,0,1,0,0,0,0])
								elif airline=='Multiple carriers':
									arr.extend([0,0,0,0,0,1,0,0,0])
								elif airline=='Multiple carriers Premium economy':
								    arr.extend([0,0,0,0,0,0,1,0,0])
								elif airline=='SpiceJet':
									arr.extend([0,0,0,0,0,0,0,1,0])
								elif airline=='Vistara':
									arr.extend([0,0,0,0,0,0,0,0,1])



									
								# Source_Banglore	Source_Chennai	Source_Delhi	Source_Kolkata	Source_Mumbai

								start=''
								end=''
								if source=='Banglore':
									arr.extend([1,0,0,0,0])
									start='BLR'
								elif source=='Chennai':
								    arr.extend([0,1,0,0,0])
								    start='MAA'
								elif source=='Delhi':
									arr.extend([0,0,1,0,0])
									start='DEL'
								elif source=='Kolkata':
								    arr.extend([0,0,0,1,0])
								    start='CCU'
								elif source=='Mumbai':
									arr.extend([0,0,0,0,1])
									start='BOM'




								# Destination_Banglore	Destination_Cochin	Destination_Delhi	Destination_Hyderabad	Destination_Kolkata	



								if destination=='Banglore':
									arr.extend([1,0,0,0,0])
									end='BLR'
								elif destination=='Cochin':
								    arr.extend([0,1,0,0,0])
								    end='COK'
								elif destination=='Delhi':
									arr.extend([0,0,1,0,0])
									end='DEL'
								elif destination=='Hyderabad':
								    arr.extend([0,0,0,1,0])
								    end='HYD'
								elif destination=='Kolkata':
									arr.extend([0,0,0,0,1])
									end='CCU'


								st.markdown("""<b>9. Select stops</b>""",unsafe_allow_html=True)
								stop = st.selectbox('Total Stops',[0,1,2,3])



								if stop==0:
									arr.extend([0,0,0,1])
								elif stop==1:
									arr.extend([1,0,0,1])
								elif stop==2:
									arr.extend([0,1,0,0])
								else:	
									arr.extend([0,0,1,0])

								#st.write(len(arr))
								#st.write(arr)

								#Loading the saved best model

								model=keras.models.load_model('model_800.h5')

								if st.button("Predict"):
									 
									# start_time=datetime.time(datetime.now())

									st.success("{} ,The Fare price is {}".format(name,round(model.predict(np.array(arr).reshape(1,29))[0][0],0)))

									# end_time=datetime.time(datetime.now())
									# st.write(start_time)
									# st.write(end_time)

									st.warning("Fare Predicted in {} seconds".format(round(end_time-start_time,2)))

									flag=1

					else:
					    st.error("Please select another date")		

			else:
			    st.error("Please enter correct source or destination")



import requests

# if flag == 1:
# 	# st.write(user_end_time)
# 	# st.write(user_start_time,time.perf_counter())
# 	st.write(start_user)
# 	end_user=timer()
# 	st.write(end_user)
# 	st.success("Thank you for staying in this page for {} minutes".format(end_user-start_user))

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/IN/INR/en-IN/"+ start + '/' + end + '/' + str(dep_date)

#url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/IN/INR/ISO%202/" + start +'/'+ end + '/'+ str(dep_date) + '/'+ str(dep_date)

headers = {
    'x-rapidapi-key': "67764b76e0mshcef79f7d342eda0p1553b0jsnc5d15330a2a5",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

file=response.json()

# st.write(file)

st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")
st.subheader("")

title="""
		<div style="background-color:#DD2A7B;padding:0px">
		<h4 style="color:#ffffff;text-align:center;font-weight:bold;">The Available Flights are (Real-Time)</h4>
		</div>
		"""
st.markdown(title,unsafe_allow_html=True)
st.subheader("")

# st.write(str(response))

if str(response) == "<Response [200]>":

	flight_names=[i["Name"] for i in file["Carriers"]]

	flight_prices=[i["MinPrice"] for i in file["Quotes"]]

	flight_times=[i["QuoteDateTime"] for i in file["Quotes"]]

	for i in range(len(flight_names)):
		st.markdown("""
			Airline is <b>{}</b>\n
				* Price is {} 
				* Departure time is {} """.format(flight_names[i] , flight_prices[i] ,str(pd.to_datetime(flight_times[i])).split()[1]),unsafe_allow_html=True)
else:
	st.info("Sorry {}, we are unable to fetch details at the moment".format(name))
		


















# Day Month	Dep_Hour	Dep_min	Duration_hour	Duration_min	
# Air Asia	Airline_Air India	Airline_GoAir	Airline_IndiGo	Airline_Jet Airways	Airline_Multiple carriers	Airline_Multiple carriers Premium economy	Airline_SpiceJet	Airline_Vistara	
# Source_Banglore	Source_Chennai	Source_Delhi	Source_Kolkata	Source_Mumbai	
# Destination_Banglore	Destination_Cochin	Destination_Delhi	Destination_Hyderabad	Destination_Kolkata	




# Total_Stops_1 stop	Total_Stops_2 stops	Total_Stops_3 stops	Total_Stops_non-stop   



# day=dep_date.date

# month=dep_date.month

# dep_hour                   6

# dep_min

# duration_hour

# duration_min


















































































































































































































































# link="https://cleanuri.com/api/v1/shorten"

# st.subheader('URL SHORTNER')
# url=st.text_input("Enter the url")
# click=st.button("Get the short link")

# if click:
# 	if url!='':
# 		data={'url':url}
# 		r=requests.post(link,data=data)
# 		st.success("Your link generated")
# 		st.write(r.json()['result_url'])
# 	else:
# 	    st.error("Enter the url and press button")

# https://docdro.id/lfwb9MI

# st.markdown("""
# <embed src="https://docdro.id/lfwb9MI" width="700" height='1000'>
# """, unsafe_allow_html=True)
