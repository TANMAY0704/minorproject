replacements = {
    'uttar pradesh': 'Uttar Pradesh',
    'up': 'Uttar Pradesh',
    'uttarpradesh': 'Uttar Pradesh',
    'madhya pradesh': 'Madhya Pradesh',
    'mp': 'Madhya Pradesh',
    'maharashtra': 'Maharashtra',
    'mahrashtra': 'Maharashtra',
    'haryana': 'Haryana',
    'hariyana': 'Haryana',
    'orissa': 'Odisha',  
    'karnataka': 'Karnataka',
    'delhi': 'Delhi',
    'delhi ncr': 'Delhi',
    'rajisthan': 'Rajasthan',  # Corrected spelling
    'rajasthan': 'Rajasthan',
    'gujrat' : 'Gujarat',
    'tamil nadu': 'Tamil Nadu', 
    'gujarat': 'Gujarat',
    'assam': 'Assam',  
    'goa': 'Goa',  
    'punjab': 'Punjab',  
    'andhra pradesh': 'Andhra Pradesh',  
    'bihar': 'Bihar',  
    'jharkhand': 'Jharkhand',  
    'tripura': 'Tripura',  
    'kolkata': 'West Bengal',  
    'varanasi': 'Uttar Pradesh',  
    'bigar': 'Bihar',  
    'not from india': 'Not from India',  
    'faridabad': 'Haryana', 
    'bhubaneswar': 'Odisha',
    'Bihar Patna': 'Bihar',
    'province 3 (nepal)': 'Province 3 (Nepal)',
    'chattisgarh': 'Chhattisgarh',  # Corrected spelling
    'karnatak': 'Karnataka',  # Corrected spelling
    'new delhi': 'Delhi',  # Assuming "new delhi" refers to Delhi
    '-': 'Unknown',  # Placeholder for unknown or missing values
    'nan': 'Unknown','bihar patna': 'Bihar',
      'maharastra' :  'Maharashtra'# Handling NaN values
    
}


indian_states_ut = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Lakshadweep', 'Puducherry'
    ]

category_mapping = {
    'Computer Science': 'Computer Science',
    'CSE': 'Computer Science',
    'B.tech': 'Engineering',
    'BTech': 'Engineering',
    'B.Tech.': 'Engineering',
    'B.Tech': 'Engineering',
    'BTech-CSE': 'Computer Science',
    'Engeneering': 'Engineering',
    'Teacher': 'Others',
    'KIIT BHUBANESWAR': 'Computer Science',
    'BTECH - CSE': 'Computer Science',
    'React native, Machine learning': 'Computer Science',
    'Computer Science Engineering': 'Computer Science',
    'KIIT': 'Computer Science',
    'BTECH IN CSE': 'Computer Science',
    'B. Tech.': 'Engineering',
    "Bachelor's in design": 'Design',
    'School student': 'Others',
    'BFA': 'Design',
    'Political Science Honours': 'Others',
    'Biotechnology': 'Others',
    'CSE': 'Computer Science',
    'BA LLB': 'Others',
    'Animation and interior design': 'Design',
    'B tech, electrical engineering': 'Engineering',
    'Bcom': 'Commerce',
    'Chartered Accountancy': 'Others',
    'Mechanical Engineering': 'Engineering',
    'Information Technology': 'Engineering',
    'Engineering': 'Engineering',
    'B.Com hons (marketing) with Liberal Arts': 'Commerce',
    'BAMS': 'Medical',
    'B.Tech. in Artificial Intelligence and Data Science': 'Engineering',
    'BA Hons. - Psychology': 'Psychology',
    'BCom Honors': 'Commerce',
    'BA Psychology Honors': 'Psychology',
    'B.tech CS (IOT - CYBERSECURITY)': 'Computer Science',
    'BCA': 'Others',
    'Btech in Computer Science Engineering': 'Computer Science',
    'Graphic Design': 'Design',
    'Psychology': 'Psychology',
    'Architecture': 'Design',
    'Studied architecture': 'Design',
    'BTech CSE': 'Computer Science',
    'Preparing For Civil Services !!': 'Others',
    'Masters in economics': 'Others',
    'B.TECH': 'Engineering',
    'btech cse': 'Computer Science',
    'Btech(CSE)': 'Computer Science',
    'Finance in Mba': 'MBA',
    'B.com hons.': 'Commerce',
    'B com': 'Commerce',
    'BTECH': 'Engineering',
    'No': 'Others',
    'Commerce': 'Commerce',
    'Bsc Computer Science': 'Computer Science',
    'BSc. Applied Psychology': 'Psychology',
    'Bdes': 'Design',
    'Bachelor’s of Applied IT': 'Others',
    'Books': 'Others',
    'Design': 'Design',
    '-': 'Others',
    'Neet': 'Medical',  
    'Fashion design': 'Fashion',
    'B.Des': 'Design',
    'Bachelors in Dental Surgery': 'Medical',  
    'Math': 'Others',
    'B. Tech': 'Engineering',
    'Bachelors of Technology in Computer Science': 'Computer Science',
    'IITBOMBAY': 'Engineering',  
    'Bsc': 'BSc',  
    'BTech Aerospace Engineering': 'Engineering',
    'btech aerospace': 'Engineering',
    'MBA': 'MBA',
    'Film studies': 'Others',
    'B.tech aerospace engineering': 'Engineering',
    'BTech Aerospace': 'Engineering',
    'Aerospace Engineering': 'Engineering',
    'MBA - Operations and SCM': 'MBA',
    'B-tech': 'Engineering',
    'Mathematics and computing': 'Others',
    'In job': 'Others',
    'B.Tech CSE': 'Computer Science',
    'WINDCHILL+': 'Others',
    'computer': 'Others',
    'Bsc IT': 'BSc',
    'Bcom accounting and finance': 'Commerce',
    'Bsc nursing': 'Medical',
    'fashion': 'Fashion',
    'Computer science': 'Computer Science',
    'Computer Science and Engineering': 'Computer Science',
    'Btech': 'Engineering',
    'B tech': 'Engineering',
    'B. Tech': 'Engineering',
    'Btech cse': 'Computer Science',
    'B.Tech CSE': 'Computer Science',
    'Computer Science and Communication Engineering': 'Computer Science',
    'BSc Computer Science': 'Computer Science',
    'Btech CSE': 'Computer Science',
    'Btech in cse': 'Computer Science',
    'B tech aerospace': 'Engineering',
    'B.tech aerospace engineering': 'Engineering',
    'BTech Aerospace': 'Engineering',
    'Aerospace Engineering': 'Engineering',
    'Btech Aerospace': 'Engineering',
    'B. Tech in Computer Science and Engineering': 'Computer Science',
    'B tech, electrical engineering': 'Engineering',
    'Bcom accounting and finance': 'Commerce',
    'Bcom hons.': 'Commerce',
    'B com': 'Commerce',
    'B.Com hons (marketing) with Liberal Arts': 'Commerce',
    'MBA - Operations and SCM': 'MBA',
    'Masters in economics': 'Others',
    'Fashion design': 'Fashion',
    'Studied architecture': 'Design',
    'Architecture': 'Design',
    'Graphic Design': 'Design',
    'Animation and interior design': 'Design',
    'Bachelor’s of Applied IT': 'Others',
    'Biotechnology': 'Others',
    'BAMS': 'Medical',
    'Bachelors in Dental Surgery': 'Medical',
    'BSc. Applied Psychology': 'Psychology',
    'BA Hons. - Psychology': 'Psychology',
    'Computer': 'Others',
    'Math': 'Others',
    'No': 'Others',
    'B. Tech CSE': 'Computer Science',
    'Computer science engineering': 'Computer Science',
    'BTech in CSE': 'Computer Science',
    "Bachelor's of design": 'Design',
    'BTech(CSE)': 'Computer Science',
    'International relations with defence and strategic Studies Research': 'Others',
    'B Tech CSE': 'Computer Science',
    'BA': 'Others',
    'B.Tech. in Computer Science and Engineering': 'Computer Science',
    'B.Tech computer science': 'Computer Science',
    'Senior High School': 'Others',
    'BBA': 'Others',
    'B.tech,CSE': 'Computer Science',
    'B.tech Aerospace Engineering': 'Engineering',
    'Bachelors in Design ( Animation, vfx and Illustration)': 'Design',
    'Computer science and engineering' : 'Computer Science', 'BTech in cse':'Computer Science',
    '-': 'Others',
    '2nd year': 'Others',
    'Aerospace Engineering': 'Engineering',
    'Animation and interior design': 'Design',
    'Architecture': 'Architecture',
    'B Tech': 'Engineering',
    'B Tech CSE': 'Computer Science',
    'B Tech, KIIT': 'Engineering',
    'B com': 'Commerce',
    'B tech': 'Engineering',
    'B tech, electrical engineering': 'Engineering',
    'B-Tech': 'Engineering',
    'B-tech': 'Engineering',
    'B. TECH CSE': 'Computer Science',
    'B. Tech': 'Engineering',
    'B. Tech CSE': 'Computer Science',
    'B. Tech cse': 'Computer Science',
    'B. Tech.': 'Engineering',
    'B. Tech. CSE': 'Computer Science',
    'B.Com hons (marketing) with Liberal Arts': 'Commerce',
    'B.Des': 'Design',
    'B.TECH': 'Engineering',
    'B.TECH (C.S.E)': 'Computer Science',
    'B.TECH (CSE)': 'Computer Science',
    'B.TECH Computer Science Engineering': 'Computer Science',
    'B.TECH(CSE)': 'Computer Science',
    'B.Tech': 'Engineering',
    'B.Tech (CSE)': 'Computer Science',
    'B.Tech (Cse)': 'Computer Science',
    'B.Tech CSE': 'Computer Science',
    'B.Tech Computer Science Engineering': 'Computer Science',
    'B.Tech Computer science engineering': 'Computer Science',
    'B.Tech Cse + B.S. in Data Science &  Programming': 'Computer Science',
    'B.Tech computer science': 'Computer Science',
    'B.Tech in CSE': 'Computer Science',
    'B.Tech in Computer science and engineering': 'Computer Science',
    'B.Tech(CSE)': 'Computer Science',
    'B.Tech, Cse': 'Computer Science',
    'B.Tech.': 'Engineering',
    'B.Tech. in Artificial Intelligence and Data Science': 'Computer Science',
    'B.Tech. in Computer Science and Engineering': 'Computer Science',
    'B.com hons.': 'Commerce',
    'B.tech': 'Engineering',
    'B.tech (CSE)': 'Computer Science',
    'B.tech Aerospace Engineering': 'Engineering',
    'B.tech CS (IOT - CYBERSECURITY)': 'Computer Science',
    'B.tech CSE': 'Computer Science',
    'B.tech aerospace engineering': 'Engineering',
    'B.tech in Computer science': 'Computer Science',
    'B.tech,CSE': 'Computer Science',
    'BA': 'Arts',
    'BA Hons. - Psychology': 'Arts',
    'BA LLB': 'Law',
    'BA Psychology Honors': 'Arts',
    'BAMS': 'Medical',
    'BBA': 'Business Administration',
    'BCA': 'Computer Applications',
    'BCom Honors': 'Commerce',
    'BFA': 'Fine Arts',
    'BSc. Applied Psychology': 'Science',
    'BTECH': 'Engineering',
    'BTECH - CSE': 'Computer Science',
    'BTECH - Cse': 'Computer Science',
    'BTECH 2ND YEAR': 'Engineering',
    'BTECH CSE': 'Computer Science',
    'BTECH IN CSE': 'Computer Science',
    'BTECH in CSE': 'Computer Science',
    'BTech': 'Engineering',
    'BTech - CSE': 'Computer Science',
    'BTech Aerospace': 'Engineering',
    'BTech Aerospace Engineering': 'Engineering',
    'BTech CSE': 'Computer Science',
    'BTech cse': 'Computer Science',
    'BTech in CSE': 'Computer Science',
    'BTech in cse': 'Computer Science',
    'BTech(CSE)': 'Computer Science',
    'BTech-CSE': 'Computer Science',
    "Bachelor's in design": 'Design',
    "Bachelor's of design": 'Design',
    'Bachelors in Dental Surgery': 'Medical',
    'Bachelors in Design ( Animation, vfx and Illustration)': 'Design',
    'Bachelors of Technology in Computer Science': 'Computer Science',
    'Bachelor’s of Applied IT': 'IT',
    'Bcom': 'Commerce',
    'Bcom accounting and finance': 'Commerce',
    'Bdes': 'Design',
    'Biotechnology': 'Biotechnology',
    'Books': 'Others',
    'Bsc': 'Science',
    'Bsc Computer Science': 'Computer Science',
    'Bsc IT': 'IT',
    'Bsc nursing': 'Medical',
    'Btech': 'Engineering',
    'Btech (cse)': 'Computer Science',
    'Btech 2nd year': 'Engineering',
    'Btech Aerospace': 'Engineering',
    'Btech CSE': 'Computer Science',
    'Btech CSE 17': 'Computer Science',
    'Btech Cse': 'Computer Science',
    'Btech computer science and engineering': 'Computer Science',
    'Btech course Cse branch 2nd year': 'Computer Science',
    'Btech cse': 'Computer Science',
    'Btech in Computer Science Engineering': 'Computer Science',
    'Btech in Computer Science and Engg': 'Computer Science',
    'Btech in Computer science and Engineering': 'Computer Science',
    'Btech in Computer science engineering': 'Computer Science',
    'Btech in cse': 'Computer Science',
    'Btech(CSE)': 'Computer Science',
    'Btech(cse)': 'Computer Science',
    'CEE': 'Engineering',
    'COA': 'Computer Science',
    'COMPUTER ENGINEERING': 'Computer Science',
    'CSE': 'Computer Science',
    'CSE BTECH': 'Computer Science',
    'Chartered Accountancy': 'Finance',
    'Coa': 'Computer Science',
    'Computer Science Engineering': 'Computer Science',
    'Computer Science and Communication Engineering': 'Computer Science',
    'Computer Science and Engineering': 'Computer Science',
    'Computer science': 'Computer Science',
    'Computer science Engineering': 'Computer Science',
    'Computer science and engineering': 'Computer Science',
    'Cse': 'Computer Science',
    'Cse core': 'Computer Science',
    'Engeneering': 'Engineering',
    'Engneering (btech in CSE)': 'Computer Science',
    'Fashion design': 'Design',
    'Film studies': 'Arts',
    'Finance in Mba': 'Finance',
    'Graphic Design': 'Design',
    'IITBOMBAY': 'Engineering',
    'In job': 'Others',
    'Information Technology': 'IT',
    'International relations with defence and strategic Studies Research': 'Social Science',
    'KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY': 'Engineering',
    'KIIT': 'Engineering',
    'KIIT BHUBANESWAR': 'Engineering',
    'MBA - Operations and SCM': 'MBA',
    'Masters in economics': 'Economics',
    'Math': 'Science',
    'Mathematics and computing': 'Computer Science',
    'Mechanical Engineering': 'Engineering',
    'Neet': 'Medical',
    'No': 'Others',
    'Persuing BTech in CSE': 'Computer Science',
    'Political Science Honours': 'Social Science',
    'Preparing For Civil Services !!': 'Others',
    'Pursuing Btech 3rd year , Computer science and engineering': 'Computer Science',
    'React native, Machine learning': 'Computer Science',
    'School student': 'Others',
    'Senior High School': 'Others',
    'Studied architecture': 'Architecture',
    'Teacher': 'Others',
    'WINDCHILL+': 'Others',
    'b.tech cse': 'Computer Science',
    'btech': 'Engineering',
    'btech aerospace': 'Engineering',
    'btech cse': 'Computer Science',
    'computer': 'Computer Science',
    'fashion': 'Design',
    'Kiit': 'Engineering',
    'Economics' : "Finance"
}


