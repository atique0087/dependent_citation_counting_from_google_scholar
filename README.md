# dependent_citation_counting_from_google_scholar
# Author: Atiqur Chowdhury.
**Step-1:** To read your google scholar citation as pdf, just go to google scholar profile's citation page, select all text and paste it in a microsoft doc file as a text.
Then convert it as a pdf file.
**Step-2:** In the 
         authors = {'collaborator1_alon':['write collaborator1 name as in google scholar with small letter'],      
        'collaborator2_alon':['write collaborator2 name as in google scholar with small letter'],.....and so on
        'myself':['write your name as in google scholar with small letter']} 
**Step-3:**  Now in the following sections: 
         # Obtain the scores for each author_name
for author_name in authors.keys():
        
    if author_name == 'collaborator1_alone':
        for word in authors[author_name]:
            if word in text:
               collaborator1_alone =text.count('write collaborator1 name as in google scholar with small letter')
        scores.append(collaborator1_alone)
        
    elif author_name == 'collaborator2_alone':
        for word in authors[author_name]:
            if word in text:
               collaborator2_alone =text.count('write collaborator2 name as in google scholar with small letter')
        scores.append(collaborator2_alone)
        ......
        ......
        ......
        #add as many as name your colloborators.
        
    else: 
        for word in authors[author_name]:
            if word in text:
                myself =text.count('write your name as in google scholar with small letter')
        scores.append(myself)
        
   then run the code. You will see how many dependent citations you have among the total citations.
