import streamlit as st
import pickle
import pandas as pd
import sklearn
from xgboost import XGBClassifier

st.title(':blue[CUSTOMER SEGMENTATION APP]')
file = open('customer_segment_xgb.pkl','rb')
model= pickle.load(file)
col1,col2,col3=st.columns(3)
with col1:
    st.subheader(':violet[AGE]')
    age=st.text_input('Enter the age')
    if age:
        age=int(age)

    #st.text(" ")
    st.subheader(':violet[QUALIFICATION]')
    education=['tertiary', 'secondary', 'primary']
    education_qual=st.selectbox('Select Qualification',education)
    if education_qual=='primary':
        education_qual=1
    elif education_qual=='secondary':
        education_qual = 2
    else:
        education_qual =3

    #st.text(" ")
    st.subheader(':violet[CONTACTED]')
    num_calls=st.text_input('Number of Times Contacted')
    if num_calls:
        num_calls=int(num_calls)
        #st.write(type(num_calls))

with col2:
    st.subheader(':violet[CALL DURATION]')
    dur=st.text_input('Enter The Duration')
    if dur:
        dur=int(dur)
    #st.text(" ")
    st.subheader(':violet[CONTACTED DATE]')
    cal=st.date_input('Select Date')
    day=int(pd.to_datetime(cal, format="%Y-%m-%dT%H:%M").day)
    month=int(pd.to_datetime(cal, format="%Y-%m-%dT%H:%M").month)
    if month==1:
        mon_jan = 1
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month==2:
        mon_jan = 1
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month==3:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 1
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month == 4:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 1
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month == 5:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 1
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month == 6:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 1
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month == 7:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 1
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month == 8:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 1
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month == 9:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 1
        mon_oct = 0
        mon_nov = 0
        mon_dec = 0
    elif month == 10:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 1
        mon_nov = 0
        mon_dec = 0
    elif month == 11:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 1
        mon_dec = 0
    elif month == 12:
        mon_jan = 0
        mon_feb = 0
        mon_mar = 0
        mon_apr = 0
        mon_may = 0
        mon_jun = 0
        mon_jul = 0
        mon_aug = 0
        mon_sep = 0
        mon_oct = 0
        mon_nov = 0
        mon_dec = 1
    #st.write(mon_jan,mon_feb,mon_mar,mon_apr,mon_may,mon_jun,mon_jul,mon_aug,mon_sep,mon_oct,mon_nov,mon_dec)
    #st.text(" ")
    st.subheader(':violet[CONVERSATION]')
    call=['unknown', 'cellular', 'telephone']
    call_type=st.selectbox("Select Type Of Call",call)
    if call_type=='unknown':
        call_type_unknown=1
        call_type_telephone=0
        call_type_cellular=0
    elif call_type=='cellular':
        call_type_unknown = 0
        call_type_telephone = 0
        call_type_cellular = 1
    else:
        call_type_unknown = 0
        call_type_telephone = 1
        call_type_cellular = 0
    #st.write(call_type_unknown,call_type_telephone,call_type_cellular)
with col3:
    st.subheader(':violet[JOB]')
    work = ['management', 'technician', 'entrepreneur', 'blue-collar', 'retired', 'admin', 'services', 'self-employed',
           'unemployed', 'housemaid', 'student']
    job=st.selectbox('Select Job',work)
    if job=='management':
        job_admin=0
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=0
        job_management=1
        job_retired=0
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=0
    elif job=='technician':
        job_admin=0
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=0
        job_management=0
        job_retired=0
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=1
        job_unemployed=0
    elif job=='entrepreneur':
        job_admin=0
        job_blue_collar=0
        job_entrepreneur=1
        job_housemaid=0
        job_management=0
        job_retired=0
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=0
    elif job=='blue-collar':
        job_admin=0
        job_blue_collar=1
        job_entrepreneur=0
        job_housemaid=0
        job_management=0
        job_retired=0
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=0
    elif job=='retired':
        job_admin=0
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=0
        job_management=0
        job_retired=1
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=0
    elif job=='admin':
        job_admin =1
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=0
        job_management=0
        job_retired=0
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=0
    elif job=='services':
        job_admin =0
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=0
        job_management=0
        job_retired=0
        job_self_employed=0
        job_services=1
        job_student=0
        job_technician=0
        job_unemployed=0
    elif job=='self-employed':
        job_admin =0
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=0
        job_management=0
        job_retired=0
        job_self_employed=1
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=0
    elif job=='unemployed':
        job_admin =0
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=0
        job_management=0
        job_retired=0
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=1
    elif job=='housemaid':
        job_admin =0
        job_blue_collar=0
        job_entrepreneur=0
        job_housemaid=1
        job_management=0
        job_retired=0
        job_self_employed=0
        job_services=0
        job_student=0
        job_technician=0
        job_unemployed=0
    else:
        job_admin = 0
        job_blue_collar = 0
        job_entrepreneur = 0
        job_housemaid = 0
        job_management = 0
        job_retired = 0
        job_self_employed = 0
        job_services = 0
        job_student = 1
        job_technician = 0
        job_unemployed = 0
    #st.write(job_admin,job_blue_collar,job_entrepreneur,job_housemaid,job_management,job_retired,job_self_employed,job_services,job_student,job_technician,job_unemployed)
    #st.text(" ")
    st.subheader(':violet[OUTCOME]')
    outcome = ['unknown', 'failure', 'other', 'success']
    out=st.selectbox('Select Outcome',outcome)
    if out=='unknown':
        prev_outcome_unknown = 1
        prev_outcome_success = 0
        prev_outcome_other = 0
        prev_outcome_failure = 0
    elif out=='failure':
        prev_outcome_unknown = 0
        prev_outcome_success = 0
        prev_outcome_other = 0
        prev_outcome_failure = 1
    elif out=='other':
        prev_outcome_unknown = 0
        prev_outcome_success = 0
        prev_outcome_other = 1
        prev_outcome_failure = 0
    else:
        prev_outcome_unknown = 0
        prev_outcome_success = 1
        prev_outcome_other = 0
        prev_outcome_failure = 0
    #st.write( prev_outcome_unknown,prev_outcome_success,prev_outcome_other,prev_outcome_failure)

    #st.text(" ")
    st.subheader(':violet[MARITAL STATUS]')
    marital = ['married', 'single', 'divorced']
    mar=st.selectbox('Select Marital Status',marital)
    if mar=='married':
        marital_divorced=0
        marital_married=1
        marital_single=0
    elif mar=='single':
        marital_divorced = 0
        marital_married = 0
        marital_single = 1
    else:
        marital_divorced = 1
        marital_married = 0
        marital_single = 0
    #st.write(marital_divorced,marital_married,marital_single)

submit=st.button('SUBMIT')
if submit:
    prediction=model.predict([[age,education_qual,day,dur,num_calls,job_admin,job_blue_collar,job_entrepreneur,job_housemaid,job_management,job_retired,job_self_employed,job_services,job_student,job_technician,job_unemployed,marital_divorced,marital_married,marital_single,mon_apr,mon_aug,mon_dec,mon_feb,mon_jan,mon_jul,mon_jun,mon_mar,mon_may,mon_nov,mon_oct,mon_sep,call_type_cellular,call_type_telephone,call_type_unknown,prev_outcome_failure,prev_outcome_other,prev_outcome_success,prev_outcome_unknown ]])
    if prediction[0]==0:
        st.write('## :red[Not Subscribed The Insurance]')
    else:
        st.write('## :green[Subscribe The Insurance]')
st.write( ':blue[App Created by KAUSHAL C]' )
