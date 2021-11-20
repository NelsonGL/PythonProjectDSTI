import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import seaborn as sns
import json
from pandas.api.types import CategoricalDtype
import warnings
import squarify
import circlify
warnings.filterwarnings('ignore')

#HEADER

html_header="""
<head>
<title>DataJobMarketAnalysis</title>
<meta charset="utf-8">
<meta name="keywords" content="Python Project, dashboard, Data Field, DSTI">
<meta name="description" content="DataJobMarketAnalysis Dashboard">
<meta name="author" content="Nelson Lopez - Virgile Sarniguet">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#008080; text-align: center; font-family:Arial"> Data Field Job Market Analysis<br>
 <h2 style="color:#008080; font-family:Arial"> Dashboard</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""


st.set_page_config(page_title="Project Dashboard", page_icon="", layout="wide")

st.markdown('<style>body{background-color: #fbfff0}</style>',unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: #008080; font-family:Arial'>Summary of data job market in France, analysing Job Offers of one of the most important job sites in France (Welcome to the Jungle)</h5>", unsafe_allow_html=True)
#st.sidebar.markdown("<h2 style='text-align: center; color: #008080; font-family:Arial'>Filter Options</h2>", unsafe_allow_html=True)

#READING DATA
@st.cache
def load_data(nrows):
    data = pd.read_csv('cleaneddf0811.csv', nrows=nrows)
    return data


df = load_data(6000)
df = df.drop_duplicates()


#SIDEBAR
#st.sidebar.multiselect('Select Role or Roles', ['Data Analyst','Data Engineer','Data Scientist'])
#st.sidebar.multiselect('Select Industry', ['Industry 1','Industry 2','Industry 3'])
#st.sidebar.multiselect('Select WebSite', ['Welcome to the Jungle','Indeed'])

#BODY

html_card_header1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 968px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Overall Job Offering Distribution by Role</h3>
  </div>
</div>
"""
html_card_footer1="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #75a8ae; padding-top: 1rem;; width: 200px;
   height: 50px;">
    <p class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Offers</p>
  </div>
</div>
"""
html_card_header2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 820px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Overall Education Requirement</h3>
  </div>
</div>
"""
html_card_footer2="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffffff00; padding-top: 0.5rem;; width: 820px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#ffffff00; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;"></h5>
  </div>
</div>
"""
html_card_header3="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 820px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;">Overall Work Experience Requirement</h3>
  </div>
</div>
"""
html_card_footer3="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #ffffff00; padding-top: 1rem;; width: 820px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#ffffff00; color:#25545b; font-family:Arial; text-align: center; padding: 0px 0;"></h5>
  </div>
</div>
"""

html_br="""
<br>
"""

with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,10,1,2,1])
    with col1:
        st.write("")
    with col4:
        st.markdown(html_card_header1, unsafe_allow_html=True)
        fig,ax1=plt.subplots(figsize=(15,7))
        data=df.groupby("Job")["Job"].apply(lambda x : x.count())
        data.plot.bar(ax=ax1,color=["#ffeda0","#feb24c","#f03b20"])
        axIns=ax1.inset_axes([0.55,0.35,0.6,0.6])                     
        data.plot.pie(ax=axIns,autopct="%.1f%%",colors=["#ffeda0","#feb24c","#f03b20"])
        ##ax1.set_ylabel("count")
        axIns.set_frame_on(False)
        axIns.set_ylabel("")
        ##fig.suptitle("Job offers by job type",fontsize=25)
        fig.tight_layout()
        fig.show()
        st.pyplot(fig)
        ##st.markdown(html_card_footer1, unsafe_allow_html=True)
        
        st.markdown(html_br, unsafe_allow_html=True)

#Block 2 highlight numbers

with st.container():
    col1, col2, col3, col4, col5 = st.columns([0.1,2.5,0.1,2.5,0.1])
    with col1:
        st.write("")
    with col2:
        cat_type1 = CategoricalDtype(categories=["Not specified",'No degree','High School Diploma','1 year of college' '2 years of college',\
                                                '3 years of college',"Bachelor's Degree","Master's Degree",'PhD'], ordered=True)
        df["Education Requirements"] = df["Education Requirements"].astype(cat_type1)
        df.loc[df["Education Requirements"].isnull(),"Education Requirements"]="Not specified"
        df['Jobb'] = 'All Jobs'
        st.markdown(html_card_header2, unsafe_allow_html=True)
        # Get the percentage of diploma requirements per job
        test=df.groupby(["Education Requirements", "Job"])["Job"].count().unstack().fillna(0).T
        cols=list(test.columns)
        test[cols]=test[cols].div(test[cols].sum(axis=1),axis=0).multiply(100)
        # Create an horizontal stacked bar plot
        fig,ax1,=plt.subplots(figsize=(12,7))
        #fig.suptitle('Proportion of Education requirements per job', fontsize=16)
        test.plot.bar(ax= ax1,figsize=(15,8),color=["#808080","#ffffb2","#fed976","#feb24c","#fd8d3c","#fc4e2a","#e31a1c","#b10026"])
        plt.legend(loc='upper left')
        plt.ylabel("percentage")
        for tick in ax1.get_xticklabels():
          tick.set_rotation(0)
        fig.tight_layout()
        st.pyplot(fig)
        st.markdown(html_card_footer2, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        cat_type = CategoricalDtype(categories=["Not specified",'< 6 months','> 6 months', '> 1 year','> 2 years','> 3 years','> 4 years','> 5 years',\
                                              '> 7 years','> 10 years'], ordered=True)
        df["Experience Requirements"] = df["Experience Requirements"].astype(cat_type)
        df.loc[df["Experience Requirements"].isnull(),"Experience Requirements"]="Not specified"
        st.markdown(html_card_header3, unsafe_allow_html=True)
        test=df.loc[df["Experience Requirements"]!="None",:].groupby(["Experience Requirements","Job"])["Job"].count().unstack().fillna(0).T
        cols=list(test.columns)
        test[cols]=test[cols].div(test[cols].sum(axis=1),axis=0).multiply(100)
        # Create an horizontal stacked bar plot
        fig,ax1,=plt.subplots(figsize=(12,7))
        #fig.suptitle('Proportion of experience requirements per job', fontsize=25)
        test.plot.bar(ax= ax1,figsize=(15,8),color=["#808080","#ffffcc","#ffeda0","#fed976","#feb24c","#fd8d3c","#fc4e2a","#e31a1c","#bd0026","#800026"])
        plt.legend(loc='upper right')
        plt.ylabel("percentage")
       
        for tick in ax1.get_xticklabels():
            tick.set_rotation(0)
        fig.tight_layout()
        st.pyplot(fig)
        st.markdown(html_card_footer3, unsafe_allow_html=True)
    with col5:
        st.write("")


st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)


### Block 3#########################################################################################
html_card_header5="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 700px;
   height: 45px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Job Offers Location</h3>
  </div>
</div>
"""
html_card_block4_header="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #75a8ae; padding-top: 5px; width: 720px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Top 20 Industries Hiring Data Professionals</h3>
  </div>
</div>
"""


with st.container():
    col1, col2, col3, col4, col5 = st.columns([0.1,2.2,0.7,2.2,0.1])
    with col1:
      st.write("")
    with col3:
      role_selection = st.selectbox('', ("All Roles", "Data Engineer", "Data Analyst","Data Scientist"))
    with col2:

        df["Postal Code"] = df["Postal Code"].astype(str)
        df["Postal Code"]=df['Postal Code'].apply(lambda x: '{0:0>2}'.format(x))
        #Creating a function to group by departement on a specifique sliced dataframe
        def groupbydept(df):
        #Create a dataframe with count of offer Grouped by departement
            test2=df.groupby("Postal Code").size().to_frame(name = 'Count').reset_index()
        #Introduce missing departements in dataframe
            listdetp=pd.DataFrame({ 'Postal Code' : range(1, 96)})
            listdetp["Postal Code"]=(listdetp["Postal Code"].
                                astype(str).
                                apply(lambda x: '{0:0>2}'.format(x)))
            deptot=listdetp.merge(test2,on='Postal Code',how='left')
        #Format Postal code so that it correspond to the Json file code
            deptot['Postal Code']=deptot['Postal Code'].apply(lambda x: '{0:0>2}'.format(x))
        #Replace nan by 0
            deptot.loc[deptot.Count.isnull(),'Count']=0
            return deptot
        deptDE= groupbydept(df.loc[df.Job=="DE"])
        deptDA=groupbydept(df.loc[df.Job=="DA"])
        deptDS=groupbydept(df.loc[df.Job=="DS"])
        deptTotal=groupbydept(df)
        st.markdown(html_card_header5, unsafe_allow_html=True)
        def createmap(data,name):
        # Setting the maximum values depending of the job type
            if name== "Data Scientist":
                max=50
            elif name == "Data Analyst":
                max=100
            else :
                max=200
        #Import Json that contain the geometric coordinates of france departements
            with open('departements-version-simplifiee.txt') as json_file:
                dep = json.load(json_file)
            fig = px.choropleth(data, geojson=dep, locations='Postal Code',color='Count',featureidkey="properties.code",
                                    color_continuous_scale=["white","#fecc5c","#fd8d3c","#e31a1c","blue"],
                                    range_color=(0,max),
                                        projection="mercator"
                                    )
            fig.update_geos(fitbounds="locations", visible=False)
            fig.update_layout(margin={"r":0,"t":27,"l":0,"b":0})
            st.plotly_chart(fig)
        
        allindus=[i.strip() for i in (df.Industry.
                                      str.
                                      cat(others=None, sep=", ", na_rep=None, join='left').
                                      split(","))]
        daindus=[i.strip() for i in (df.loc[df.Job=="DA",:].Industry.
                                    str.
                                    cat(others=None, sep=", ", na_rep=None, join='left').
                                    split(","))]
        dsindus=[i.strip() for i in (df.loc[df.Job=="DS",:].Industry.
                                    str.
                                    cat(others=None, sep=", ", na_rep=None, join='left').
                                    split(","))]
        deindus=[i.strip() for i in (df.loc[df.Job=="DE",:].Industry.
                                    str.
                                    cat(others=None, sep=", ", na_rep=None, join='left').
                                    split(","))]          
        if role_selection == "All Roles":
          createmap(deptTotal, "all jobs")
          industry = allindus
        elif role_selection == "Data Engineer":
          createmap(deptDE, "Data Engineer")
          industry = deindus
        elif role_selection == "Data Analyst":
          createmap(deptDA, "Data Analyst")
          industry = daindus
        elif role_selection == "Data Scientist":
          createmap(deptDS, "Data Scientist")
          industry = dsindus
        

#Figure
    with col4:
        st.markdown(html_card_block4_header, unsafe_allow_html=True)
        

                                    
        #if industry_role == "All Roles ":
         # industry = allindus
        #elif industry_role == "Data Engineer ":
         # industry = deindus
        #elif industry_role == "Data Analyst ":
         # industry = daindus
        #elif industry_role == "Data Scientist ":
         # industry = dsindus
        fig,ax1,=plt.subplots(figsize=(12,7))
        ax1=pd.Series(industry).value_counts()[0:20].sort_values().plot.barh(ax=ax1,color="#b10026")
        #ax1.set_title("All jobs")
        #fig.suptitle("Top 20 industries that hire the most for each job",fontsize=25)
        fig.tight_layout()
        st.pyplot(fig)      
    with col5:
        st.write("")

    with col3:
        st.write("")

st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)

### Block 4#########################################################################################

#### BLOCK VIRGILE
with st.container():
    col1, col2, col3, col4, col5 = st.columns([1.6,1,0.1,2.5,0.1])
    with col4:
        st.write("")
    with col2:
        st.write("")
    with col3:
        st.write("")

st.markdown(html_br, unsafe_allow_html=True)

### Block 5#########################################################################################
html_line_block5="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
"""
html_card_block51_header="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #75a8ae; padding-top: 5px; width: 450px;
   height: 30px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Role Comparisson</h3>
  </div>
</div>
"""
html_card_block52_header="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 10px 10px; background: #75a8ae; padding-top: 5px; width: 450px;
   height: 30px;">
    <h3 class="card-title" style="background-color:#75a8ae; color:#25545b; font-family:Arial; text-align: center; padding: 5px 0;">Skill Comparisson</h3>
  </div>
</div>
"""

st.markdown(html_line_block5, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #008080; font-family:Arial'>Interactive Data Comparisson</h3>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1,2,1,10,1,2,1])

    with col2:
      st.write("")
        #role_selection_skill = st.selectbox('Select Role to Compare', ['Data Analyst','Data Engineer','Data Scientist'])
        #if role_selection == "Data Engineer":
        #  role_skill = "DE"
        #elif role_selection == "Data Analyst":
        #  role_skill = "DA"
        #elif role_selection == "Data Scientist":
        #  role_skill = "DS"
    with col6:
      st.write("")

    with col4:
      st.write("")
      role_selection_skill = st.selectbox('Select Role to Compare', ['Data Analyst','Data Engineer','Data Scientist'])
      if role_selection_skill == "Data Engineer":
        role_skill = "DE"
      elif role_selection_skill == "Data Analyst":
        role_skill = "DA"
      elif role_selection_skill == "Data Scientist":
        role_skill = "DS"
      indus = st.selectbox('Select Industry to Compare', ['Big Data','SaaS / Cloud Services','Intelligence artificielle / Machine Learning','IT / Digital',\
                                                            'E-commerce','Logiciels','FinTech / InsurTech','Application mobile','Digital Marketing / Data Marketing',\
                                                            'media/cinema/music/film','banque/finance','pharma/santé','Publicité','Stratégie','Energie','Transports',\
                                                            'Économie collaborative','Assurance','Cybersécurité','Organisation / Management'])


      def circulize(job,data,indus):
          """Cirulize create a packing circle vizualisation for a specified job and industry"""
          if job=="DA":
              color="#ffeda0"
          elif job=="DS":
              color="#f03b20"
          else:
              color="#feb24c"
          data=(df.loc[df.Industry.str.contains(indus),:].
                groupby("Job")['sql','python', 'cloud', 'big_data', 'machine_learning', 'design',\
              'development', 'google_analytics', 'google_cloud', 'aws', 'spark',\
            'power_bi', 'dashboard', 'visualisation', 'docker', 'javascript',\
            'modelisation', 'kafka', 'etl', 'sap', 'crm', 'sql_server', 'excel',\
            'security', 'api', 'linux', 'qa', 'architecture', 'saas', 'ux', 'nosql',\
            'apache', 'databases', 'java', 'devops', 'kubernetes', 'tableau', 'git',\
            'r', 'azure', 'scala', 'microsoft', 'hadoop', 'elasticsearch', 'mysql',\
            'postgresql', 'oracle', 'access', 'statistiques', 'qlik', 'vba', 'c',\
            'c++', 'c#', 'travailler_équipe', 'analytique', 'communication',\
            'leadership', 'innovant', 'rigoureux', 'problem_solving', 'autonome',\
            'curieux'].
                apply(lambda x :x.sum()/x.count())
                .T.
              sort_values(job,ascending=False)[0:15])
          circles = circlify.circlify(
              data[job].tolist(), 
              show_enclosure=True, 
              target_enclosure=circlify.Circle(x=0, y=0, r=1)
          )
          labels=data.sort_values(by=job).index
          fig, ax = plt.subplots(figsize=(10,10))

          # Remove axes
          ax.axis('off')

          # Find axis boundaries
          lim = max(
              max(
                  abs(circle.x) + circle.r,
                  abs(circle.y) + circle.r,
              )
              for circle in circles
          )
          plt.xlim(-lim, lim)
          plt.ylim(-lim, lim)

          # print circles
          for circle,label in zip(circles,labels):
              x, y, r = circle
              x, y, r = circle
              ax.add_patch(plt.Circle((x, y), r, alpha=0.4, linewidth=2,color=color))
              plt.annotate(
                    label, 
                    (x,y ) ,
                    va='center',
                    ha='center'
              )
          st.pyplot(fig)
      circulize(role_skill,data,indus)

st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)
st.markdown(html_br, unsafe_allow_html=True)



html_br="""
<br>
"""



#FOOTER

html_line="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<div style="color: #008080; font-family:Arial; text-align: right;">Designed by Nelson Lopez and Virgile Sarniguet</div>
<div style="color: #008080; font-family:Arial; text-align: right;">DSTI Project - Python Labs</div>
"""
st.markdown(html_line, unsafe_allow_html=True)