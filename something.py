import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode
import pandas as pd
import random
import seaborn as sns
from collections import Counter
from itertools import takewhile

st.set_page_config(page_title="Jishnu's Data Analyser",
                   page_icon=":bar_chart:",
                   layout="wide")
st.sidebar.title('Options')
j = st.sidebar.selectbox('Enter your choice',
                         ['Data Analyser', 'Make your own graph'])
if (j == 'Data Analyser'):
  st.title = ('Box plot maker')
  manual_or_advtech = st.selectbox(
      'Enter numbers manually or enter a set of numbers separated by commas',
      ('Enter numbers manually', 'Enter a set of numbers'))
  if (manual_or_advtech == 'Enter numbers manually'):

    def main():
      data = list()
      times = st.number_input(
          'How many numbers would you like to add? (minimum 5 numbers)',
          min_value=5,
          key='times')
      repeat = 0
      for i in range(times):
        question = st.number_input('Enter the number', key=repeat)
        data.append(question)
        st.write('Your numbers', data)
        repeat += 1
      mean = np.mean(data)
      median = np.median(data)
      counter=Counter(data)
      if counter:
        mostCommon=counter.most_common()
        max_count=mostCommon[0][1]
        modes=[t[0] for t in takewhile(lambda x:x[1]==max_count,mostCommon)]
      q1=np.quantile(data,0.25)
      q3=np.quantile(data,0.75)
      inter_q_range=(q3-q1)
      top_whisker=q3+(1.5*inter_q_range)
      bottom_whisker=q1-(1.5*inter_q_range)
      outlier=[]
      for i in data:
        if i>=top_whisker or i<=bottom_whisker:
          outlier.append(i)
      if outlier==[]:
        fig, ax = plt.subplots()
        ax.boxplot(data, label=['Data'], vert=False)
        ax.set_title('Your Box Plot')
        ax.set_xlabel('Values')
        ax.set_ylabel('Data')
        st.pyplot(fig)
          
      else:
        st.header('Outliers:')
        st.write(outlier)
        y=st.selectbox('Would you like to take the outliers out?',['Yes','No'])
        if y=='No':
          fig, ax = plt.subplots()
          ax.boxplot(data, label=['Data'], vert=False)
          ax.set_title('Your Box Plot')
          ax.set_xlabel('Values')
          ax.set_ylabel('Data')
          st.pyplot(fig)
        else:
          for i in outlier:
            data.remove(i)
          fig, ax = plt.subplots()
          ax.boxplot(data, label=['Data'], vert=False)
          ax.set_title('Your Box Plot')
          ax.set_xlabel('Values')
          ax.set_ylabel('Data')
          st.pyplot(fig)
          st.header('New Data')
          mean = np.mean(data)
          median = np.median(data)
          counter=Counter(data)
          if counter:
            mostCommon=counter.most_common()
            max_count=mostCommon[0][1]
            modes=[t[0] for t in takewhile(lambda x:x[1]==max_count,mostCommon)]
          for i, item in enumerate(data, start=1):
            st.write(f'{i}. {item}')
          st.write('The mean is ', mean)
          st.write('The median is ', median)
          st.write('Modes:', modes)

    main()
  elif (manual_or_advtech == 'Enter a set of numbers'):
    x = st.text_input('Enter the numbers')
    y = x.split(',')

    if x:
      numbers = [float(value.strip()) for value in y]
      st.write('Your numbers')
      mean = np.mean(numbers)
      median = np.median(numbers)
      counter=Counter(numbers)
      if counter:
        mostCommon=counter.most_common()
        max_count=mostCommon[0][1]
        modes=[t[0] for t in takewhile(lambda x:x[1]==max_count,mostCommon)]
      for i, item in enumerate(numbers, start=1):
        st.write(f'{i}. {item}')
      st.write('The mean is ', mean)
      st.write('The median is ', median)
      st.write('Modes:', modes)
      q1=np.quantile(numbers,0.25)
      q3=np.quantile(numbers,0.75)
      inter_q_range=(q3-q1)
      top_whisker=q3+(1.5*inter_q_range)
      bottom_whisker=q1-(1.5*inter_q_range)
      outlier=[]
      for i in numbers:
        if i>=top_whisker or i<=bottom_whisker:
          outlier.append(i)
      if outlier==[]:
        fig, ax = plt.subplots()
        ax.boxplot(numbers, label=['Data'], vert=False)
        ax.set_title('Your Box Plot')
        ax.set_xlabel('Values')
        ax.set_ylabel('Data')
        st.pyplot(fig)
      else:
        st.header('Outliers:')
        st.write(outlier)
        y=st.selectbox('Would you like to take the outliers out?',['Yes','No'])
        if y=='No':
          fig, ax = plt.subplots()
          ax.boxplot(numbers, label=['Data'], vert=False)
          ax.set_title('Your Box Plot')
          ax.set_xlabel('Values')
          ax.set_ylabel('Data')
          st.pyplot(fig)
        else:
          for i in outlier:
            numbers.remove(i)
          fig, ax = plt.subplots()
          ax.boxplot(numbers, label=['Data'], vert=False)
          ax.set_title('Your Box Plot')
          ax.set_xlabel('Values')
          ax.set_ylabel('Data')
          st.pyplot(fig)
          st.header('New Data')
          mean = np.mean(numbers)
          median = np.median(numbers)
          counter=Counter(numbers)
          if counter:
            mostCommon=counter.most_common()
            max_count=mostCommon[0][1]
            modes=[t[0] for t in takewhile(lambda x:x[1]==max_count,mostCommon)]
          for i, item in enumerate(numbers, start=1):
            st.write(f'{i}. {item}')
          st.write('The mean is ', mean)
          st.write('The median is ', median)
          st.write('Modes:', modes)
        
    else:
      st.write('Please write numbers')

elif (j == 'Make your own graph'):
  st.title = ('Make your own graph')
  graph_choice = st.selectbox(
      'What graph would you like to make?',
      ['Scatter Plot', 'Bar Graph', 'Circle Graph (pie chart)'])
  if (graph_choice == 'Circle Graph (pie chart)'):
    st.title = ('Circle Graph (pie chart)')
    y = int(st.number_input('Enter the number of categories', min_value=1))
    if ValueError:
      st.write('Please fill all the boxes')
    names = []
    sizes = []
    for i in range(y):
      name = st.text_input('Enter the category name', key=f"category_name{i}")
      names.append(name)
      size = int(
          st.number_input('Enter the value of the category',
                          min_value=1,
                          key=f"category_value{i}"))
      sizes.append(size)
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=names, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

  elif (graph_choice == 'Scatter Plot'):
    st.title = ('Scatter Plot')
    table = pd.DataFrame(columns=['X Values', 'Y Values'])
    config = {
        'x': st.column_config.NumberColumn('Enter the X values', min_value=0),
        'y': st.column_config.NumberColumn('Enter the y values', min_value=0)
    }
    graph = st.data_editor(table, column_config=config, num_rows='dynamic')

    if st.button('Make a scatter plot'):
      ab = st.data_editor(graph)
      da_list = ab.values.tolist()
      da_list = []
      two_list = []
      for index, row in ab.iterrows():
        da_list.append(row['X Values'])
        two_list.append(row['Y Values'])

      xsor = sorted(da_list)
      ysor = sorted(two_list)
      x = [float(i) for i in xsor]
      y = [float(i) for i in ysor]
      fig, ax = plt.subplots()
      ax.scatter(x, y)
      ax.set_xlabel('X Values')
      ax.set_ylabel('Y Values')
      ax.set_title('Scatter Plot')
      st.pyplot(fig)

  elif (graph_choice == 'Bar Graph'):
    st.title = ('Bar Graph')
    y = int(st.number_input('Enter the number of categories', min_value=1))
    if ValueError:
      st.write('Please fill all the boxes')
    names = []
    sizes = []
    for i in range(y):
      name = st.text_input('Enter the category name', key=f"category_name{i}")
      names.append(name)
      size = int(
          st.number_input('Enter the value of the category',
                          min_value=1,
                          key=f"category_value{i}"))
      sizes.append(size)
    if st.button('Click to make graph'):
      fig, ax= plt.subplots()
      colors_bar=['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown']
      plt.bar(names, sizes, color=colors_bar)
      plt.xlabel('Categories')
      plt.ylabel('Values')
      plt.title('Your Bar Graph')
      st.pyplot(fig)

  
        
  
      
      
