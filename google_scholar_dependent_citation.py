import PyPDF2
import re
import string
import pandas as pd 
import matplotlib.pyplot as plt

pdfFileObj = open('sample_file.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
text = text.lower()

text = re.sub(r'\d+',' ',text)
text = re.sub(r'\n',' ',text)
text = text.translate(str.maketrans(' ',' ',string.punctuation))

scores =[]

authors = {'Kabir_alone':['kma kabir', 'km ariful kabir'],      
        'x_wang_alone':['x wang'],
        'myself':['a chowdhury']}

# Obtain the scores for each author_name
for author_name in authors.keys():
        
    if author_name == 'Kabir_alone':
        for word in authors[author_name]:
            if word in text:
                Kabir_alone =text.count('kma kabir')
        scores.append(Kabir_alone)
        
    elif author_name == 'x_wang_alone':
        for word in authors[author_name]:
            if word in text:
                x_wang_alone =text.count('x wang')
        scores.append(x_wang_alone)
        
    else: 
        for word in authors[author_name]:
            if word in text:
                myself =text.count('a chowdhury')
        scores.append(myself)
        
    
summary = pd.DataFrame(scores,index=authors.keys(),columns=['number of citations']).sort_values(by='number of citations',ascending=False)
print(summary)

# Create pie chart visualization
pie = plt.figure(figsize=(10,10))
plt.pie(summary['number of citations'], labels=summary.index, explode = (0.1,0,0), autopct='%1.0f%%',shadow=True,startangle=90)
plt.title('My dependent Citations ststistics')
plt.axis('equal')
plt.show()

# Save pie chart as a .png file
pie.savefig('resume_screening_results.png')
