#!/usr/bin/env python
# coding: utf-8

# # BHARAT INTERN ARTIFICIAL INTELLIGENCE INTERSHIP

# # TASK 1: RESUME PARSER

# # BY Ayushi George

# In[2]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# ## Download NLTK resources 

# In[3]:


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# ## Load the resume and job description text

# In[4]:


resume_text = """
[WISFLUX TECHLABS. (80+ employee software as a service based startup) Jaipur, Raj
Software Engineer Intern Mar 2022 – July 2022
▪︎ Contributed to a React based project using front-end and worked on UI content for the application.
▪︎ Aggregated unstructured data from 20+ sources to build the user manual of a new product.
MICROSOFT- FUTURE READY TALENT (Virtual Internship by AICTE) Remote
Software Engineer Intern Aug 2022 – 2022
▪︎ Deployed project responsive website with HTML, CSS, Javascript & Bootstrap on Azure Cloud, Microsoft Service Link
THE SPARKS FOUNDATION (Singapore based internship platform) Remote
1. Android Development Intern. Sept 2022 —Oct 2022
▪︎ Constructed basic application for social media Link
2. Data Science Intern
▪︎ Developed Data Analysis of Business data analytics on a Sample Store as Business perspective.Link
GOLDMAN SACHS VIRTUAL INTERNSHIP - by FORAGE. Aug 2022– Sep 2022
▪︎Completed virtual internship by in domain of cybersecurity :Cryptography, Password Cracking, password best practices
WORDPRESS DEVELOPER (Ayushi George) Freelance
▪︎ Constructed WordPress for over 2 years with 1500+ views and 22 followers and reach of 2000.
▪︎ Delivered a site for clients service startup on the PreMarital advice platform.
AR CREATOR (Augment Reality based filters developer by Meta's SparkAR) Freelance
▪︎ Deployed AR based filters on official handles of JECRC College page for Renaissance (Annual Techno-Cultural Fest) and
Freshers Party and MUN official filter.
▪︎ Selected as Official Campus Representative for Meta's SparkAR training campaign, made AR Game as Filter
]
"""


# In[5]:


job_description = """
[0-3 years work experience Proficiency in Python, Spark, SQLDegree in data science, statistics, engineering, applied mathematics, operations research, information sciences, or another biological/physical science. Strength in code documentation Proficiency in Git and code versioning tools (Gitlab) Proficiency in Atlassian Suite such as JIRA and Confluence. Familiarity with cloud computing (AWS, Goolge Cloud preferred)Knowledge of statistics and machine learning (Computer Science/IT with good knowledge of Statistics)/ Analytics/ Data Science. Proficient in Python or R and other open source tools Relevant work experience of 0 to 4 years Intellectual curiosity and persistence to find answers to questions Eager to continuously learn and adapt to changing technologies and tools. Solid understanding of Statistics. Good aptitude for data analysis. Familiar with contemporary database systems]
"""


# ## Tokenize and preprocess the resume text

# In[6]:


resume_tokens = word_tokenize(resume_text)
resume_tokens = [token.lower() for token in resume_tokens if token.isalpha()]
resume_tokens = [token for token in resume_tokens if token not in stopwords.words('english')]
lemmatizer = WordNetLemmatizer()
resume_tokens = [lemmatizer.lemmatize(token) for token in resume_tokens]


# ## Tokenize and preprocess the job description text

# In[7]:


job_tokens = word_tokenize(job_description)
job_tokens = [token.lower() for token in job_tokens if token.isalpha()]
job_tokens = [token for token in job_tokens if token not in stopwords.words('english')]
job_tokens = [lemmatizer.lemmatize(token) for token in job_tokens]


# ## Compare the tokens and find the matching keywords

# In[8]:


matching_keywords = set(resume_tokens) & set(job_tokens)


# ## Print the matching keywords

# In[9]:


print("Matching Keywords:")
for keyword in matching_keywords:
    print(keyword)


# # Thank You 

# In[ ]:




