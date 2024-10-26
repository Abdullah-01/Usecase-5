import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("A Fresh Look at Job Opportunities in Saudi Arabia")
st.markdown('#')
st.markdown("Saudi Arabia's job market offers unique insights that can help fresh graduates better understand where to focus their career search. My analysis explores where jobs are located, what employers are looking for in terms of experience and gender, and what fresh graduates can expect in terms of salary.")
image = Image.open('44777317.jpg')
st.image(image, width=600)
st.markdown('#')
st.markdown('## *Where Are the Jobs?*')
st.markdown("Most job opportunities are concentrated in Riyadh and Jeddah. These two cities have the highest number of postings, suggesting they’re the best places for job seekers to find opportunities.")
image2 = Image.open('image_1.jpg')
st.image(image2)
st.markdown('#')
st.markdown('## *Gender Preferences in Job Postings*')
st.markdown("Employers in Saudi Arabia are becoming more inclusive. While about 39% of jobs are open to both men and women, some roles still specify a gender preference—32.8% for men and 27.9% for women.")
image3 = Image.open('image_2.jpg')
st.image(image3)
st.markdown('#')
st.markdown('## *Expected Salary for Fresh Graduates*')
st.markdown("For fresh graduates, starting salaries tend to be around SAR 4,000, with some roles offering up to SAR 10,000 or more. Chart: The histogram shows most entry-level jobs pay around SAR 4,000, giving new graduates a benchmark for salary expectations.")
image4 = Image.open('image_3.jpg')
st.image(image4)
st.markdown('#')
st.markdown('## *Experience Requirements*')
st.markdown("Over half (56.2%) of the jobs don’t require experience, making it easier for fresh graduates to find roles. However, some positions still ask for 2–4 years of experience.")
image5 = Image.open('image_4.png')
st.image(image5)
st.markdown('#')
st.markdown('## *Key Takeaways*')
st.markdown('Saudi Arabia’s job market is centered around Riyadh and Jeddah, becoming more gender-inclusive, and offers decent starting salaries for fresh graduates. Many jobs are accessible without prior experience, making it a promising environment for new graduates stepping into their careers.')


