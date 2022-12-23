#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from pandasql import sqldf
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
#client = Socrata("data.cityofnewyork.us/resource/jb7j-dtam.json", "J5F17tXpdVYQUtsJEjvqXn9Li")

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                  "J5F17tXpdVYQUtsJEjvqXn9Li",
                 username="igabyus@gmail.com",
                  password="Web1312@1")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("jb7j-dtam", limit=2000)


# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
pysqldf = lambda q: sqldf(q, globals())
#print(results_df)

def top_10_deaths():
    #print("top 10 causes of death ")
    causes_rank = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       GROUP BY leading_cause
       ORDER BY  count DESC
       LIMIT 10;"""
    death_causes_rank = pysqldf(causes_rank)

    return death_causes_rank

def woman_10_death():
    print("top 10 causes of death in woman ") 
    woman_rank = """SELECT leading_cause, SUM(deaths) as count 
        FROM results_df
        WHERE sex = "Female" or sex = "F"
        GROUP BY leading_cause
        ORDER BY  count DESC
        LIMIT 10;"""
    death_woman_rank = pysqldf(woman_rank)
    #print(death_woman_rank)
    return death_woman_rank

def men_10_death():
    print("top 10 causes of death in men ")
    men_rank = """SELECT leading_cause, SUM(deaths) as count 
        FROM results_df
        WHERE sex = "Male" or sex = "M"
        GROUP BY leading_cause
        ORDER BY  count DESC
        LIMIT 10;"""
    death_men_rank = pysqldf(men_rank)
    #print(death_men_rank)
    return death_men_rank

def death_year():
       death_year = """SELECT year, SUM(deaths) as count 
       FROM results_df
       GROUP BY year
       ORDER BY year;"""
       death_year_display = pysqldf(death_year)
       return death_year_display

def _2019():

       death_2019 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2019"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2019 = pysqldf(death_2019)
       return(death_year_2019)


def _2014():
       death_2014 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2014"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2014 = pysqldf(death_2014)
       return(death_year_2014)

def _2013():
       death_2013 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2013"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2013 = pysqldf(death_2013)
       return(death_year_2013)

def _2012():
       death_2012 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2012"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2012 = pysqldf(death_2012)
       return(death_year_2012)

def _2011():
       death_2011 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2011"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2011 = pysqldf(death_2011)
       return(death_year_2011)

def _2010():
       death_2010 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2010"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2010 = pysqldf(death_2010)
       return(death_year_2010)

def _2009():
       death_2009 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2009"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2009 = pysqldf(death_2009)
       return(death_year_2009)

def _2008():
       death_2008 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2008"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2008 = pysqldf(death_2008)
       return(death_year_2008)

def _2007():
       death_2007 = """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              where year = "2007"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_year_2007 = pysqldf(death_2007)
       return (death_year_2007)


def hispanic():
       death_hispanic =  """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              WHERE race_ethnicity = "Hispanic"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_hispanic_displayed  = pysqldf(death_hispanic)
       return(death_hispanic_displayed)

#print("leading cause of death in Asian and Pacific Islander")
def asian():
       death_asian =  """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              WHERE race_ethnicity = "Asian and Pacific Islander"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_asian_displayed  = pysqldf(death_asian)
       return(death_asian_displayed)


#print("leading cause of death in Black Non-hispanic")
def black():
       death_black =  """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              WHERE race_ethnicity = "Black Non-Hispanic" or race_ethnicity = "Non-Hispanic Black"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_black_displayed  = pysqldf(death_black)
       return(death_black_displayed)

def white():
       death_white =  """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              WHERE race_ethnicity = "White Non-Hispanic" or race_ethnicity = "Non-Hispanic White"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_white_displayed  = pysqldf(death_white)
       return(death_white_displayed)

def none():
       death_none =  """SELECT leading_cause, SUM(deaths) as count 
              FROM results_df
              WHERE race_ethnicity = "Other Race/ Ethnicity" or race_ethnicity = "Not Stated/Unknown"
              GROUP BY leading_cause
              ORDER BY count DESC
              LIMIT 10 ;"""
       death_none_displayed  = pysqldf(death_none)
       return(death_none_displayed)

'''
print("death caused by other over years observed")
other =  """SELECT year,  SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "(Other)" or leading_cause = "All Other Causes"
       GROUP BY year
       ORDER BY year
        ;"""
death_other  = pysqldf(other)
print(death_other)

print("death caused by cancer over years observed")
cancer =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Malignant Neoplasms (Cancer: C00-C97)" 
       GROUP BY year
       ORDER BY year
        ;"""
death_cancer  = pysqldf(cancer)
print(death_cancer)

print("death caused by flu over years observed")
flu =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Influenza (Flu) and Pneumonia (J09-J18)" 
       GROUP BY year
       ORDER BY year
        ;"""
death_flu  = pysqldf(flu)
print(death_flu)

print("death caused by heart disease over years observed")
heart =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Diseases of Heart (I00-I09, I11, I13, I20-I51)" 
       GROUP BY year
       ORDER BY year
        ;"""
death_heart  = pysqldf(heart)
print(death_heart)

print("death caused by diabeaties over years observed")
dia =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Diabetes Mellitus (E10-E14)" 
       GROUP BY year
       ORDER BY year3
        ;"""
death_dia  = pysqldf(dia)
print(death_dia)
'''

def update(dic):
       x = [v  for k,v in  dic['leading_cause'].items()]
       y = [str(int(v))  for k,v in  dic['count'].items()]
       l = ""
       for i in range(len(x)):
              l += '["'+x[i]+'", '+y[i]+"]"
              if(i!=len(x)-1):
                     l+=","
       return l



if __name__ == "__main__":
    # Creating an HTML file
    #top_10_deaths()
    #print(top_10_deaths().leading_cause)
    dic = top_10_deaths().to_dict()
    l = update(dic)
    female = update(woman_10_death())
    male = update(men_10_death())
    _2019 = update(_2019())
    _2014 = update(_2014())
    _2013 = update(_2013())
    _2012 = update(_2012())
    _2011 = update(_2011())
    _2010 = update(_2010())
    _2009 = update(_2009())
    _2008 = update(_2008())
    _2007 = update(_2007())

    hispanic = update(hispanic())
    asian = update(asian())
    black = update(black())
    white = update(white())
    none = update(none())
    





    #string = 'hello {0} {1}'.format('test', 'bye')
    #print(string)
   
    # how to get python object to html dataframe

    output_string = '''<!DOCTYPE html>
<html>
<style>
header{
  background-color: rgb(255, 255, 255);
  padding: 10px;
  text-align: center;
  font-size: 25px;
  color: black;
}
nav{
float: left;
width: 20%;
height: 700px; /* only for demonstration, should be removed */
background: rgb(255, 255, 255);

}
article{
float: right;
padding: 20px;
width: 77%;
background-color: rgb(255, 255, 255);
height: 700px; /* only for demonstration, should be removed */
}

.dropbtn {
  background-color: rgb(255, 255, 255);
  color: black;
  padding: 20px;
  width: 300px;
  height: 60px;
  font-size: 16px;
  border: 2px solid black;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: #c6ccc6;;}
</style>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<body>
<header>
<h2>New York City Death Rates</h2>
</header>
<nav>
<h1>Factors</h1>

<div class="dropdown">
  <button class="dropbtn">Year</button>
  <div class="dropdown-content">
    <button  style="height:50px;width:300px" onclick="_2019()">2019</button>
    <button  style="height:50px;width:300px" onclick="_2014()">2014</button>
    <button  style="height:50px;width:300px" onclick="_2013()">2013</button>
    <button  style="height:50px;width:300px" onclick="_2012()">2012</button>
    <button  style="height:50px;width:300px" onclick="_2011()">2011</button>
    <button  style="height:50px;width:300px" onclick="_2010()">2010</button>
    <button  style="height:50px;width:300px" onclick="_2009()">2009</button>
    <button  style="height:50px;width:300px" onclick="_2008()">2008</button>
    <button  style="height:50px;width:300px" onclick="_2007()">2007</button>
  </div>
</div>

<div class="dropdown">
  <button class="dropbtn">Gender</button>
  <div class="dropdown-content">
    <button  style="height:50px;width:300px" onclick="female()">Female</button>
    <button  style="height:50px;width:300px" onclick="male()">Male</button>
  </div>
</div>

<div class="dropdown">
  <button class="dropbtn">Race</button>
  <div class="dropdown-content">
    <button  style="height:50px;width:300px" onclick="hispanic()">Hispanic</button>
    <button  style="height:50px;width:300px" onclick="asian()">Asian</button>
    <button  style="height:50px;width:300px" onclick="black()">African American</button>
    <button  style="height:50px;width:300px" onclick="white()">Caucasian</button>
    <button  style="height:50px;width:300px" onclick="none()">Undeclared</button>
  </div>
</div>









</nav>
<article>
<div
id="myChart" style="width:100%; max-width:1100px; height:800px; float: right">
</div>


<script>
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string +=l
output_string +=''']);

var options = {
  title:'Top 10 Causes of Deaths'
};

var chart = new google.visualization.PieChart(document.getElementById('myChart'));
  chart.draw(data, options);
}
</script>

</article>

<script>
    function female(){
       google.charts.load('current', {'packages':['corechart']});
       google.charts.setOnLoadCallback(drawChart);

       function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string +=female
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in Woman '
       };

       var chart = new google.visualization.PieChart(document.getElementById('myChart'));
       chart.draw(data, options);

       }
    
       }
function male(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
              var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string +=male
output_string +=''']);
              var options = {
              title:'Top 10 Causes of Death in Men'
              };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }

              }
function _2019(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string +=_2019
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2019'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }

function hispanic(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string +=hispanic
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in Hispanics'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function asian(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string +=asian
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in Asians'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function black(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += black
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in African Americans'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }

function white(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += white
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in Cacasians'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function none(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += none
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in Undeclared'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }

function _2014(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2014
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2014'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function _2013(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2013
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2013'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function _2012(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2012
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2012'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function _2011(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2011
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2011'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function _2010(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2010
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2010'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }

function _2009(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2009
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2009'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function _2008(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2008
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2008'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
function _2007(){
              google.charts.load('current', {'packages':['corechart']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
       var data = google.visualization.arrayToDataTable([['Cause', 'count'],'''
output_string += _2007
output_string +=''']);

       var options = {
       title:'Top 10 Causes of Death in 2007'
       };

              var chart = new google.visualization.PieChart(document.getElementById('myChart'));
              chart.draw(data, options);

              }
              }
</script>

</body>
</html>



'''
    


    #print("test",x,y)
    
Func = open("nyc_death.html","w")
    
    # Adding  to the HTML file
Func.write(output_string)
              
    # Saving the data into the HTML file
Func.close()
print("done")
    
    
    


