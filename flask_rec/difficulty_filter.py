def search_results(search):
    
    if search == 'Easy':
        results=data[data['Difficulty']=='Easy']
    elif search == 'Medium':    
        results=data[data['Difficulty']=='Medium']
    elif search == 'Difficult':  
        results=data[data['Difficulty']=='Difficult']
    else:
        results=None
       
    return results
