import pandas as pd

# List of team members with emails
team_members = [
    ("Josue Acevedo", "jva5829@psu.edu"),
    ("Mohammad Ahmad", "mohammad.ahmad@psu.edu"),
    ("Aneesa Ahmat", "afa6049@psu.edu"),
    ("Waqas Ahmed", "wja5138@psu.edu"),
    ("Reem Saud A Algarah", "rsa5312@psu.edu"),
    ("Nouf Altuwayjiri", "nqa5481@psu.edu"),
    ("Tanvi Rupeshkumar Amlani", "tra5258@psu.edu"),
    ("Arthi Anbalagan", "arthianbalagan@psu.edu"),
    ("Dana Awlia", "dma5893@psu.edu"),
    ("Bryan R Bennett", "brb5545@psu.edu"),
    ("Mrudvi Bhatt", "mkb6611@psu.edu"),
    ("Giulia Cantella", "gjc5610@psu.edu"),
    ("Yunshu Cao", "ykc5481@psu.edu"),
    ("Rohit Chorghe", "rpc5776@psu.edu"),
    ("Prithvi Choudhary", "pfc5346@psu.edu"),
    ("Bhuvanesh Sallagundla Chowdary", "bsc5486@psu.edu"),
    ("Febin Clement", "fmc5271@psu.edu"),
    ("Christian Gabriel Cruz-Yanes", "cpc6162@psu.edu"),
    ("Angela Maya Deras", "amd7917@psu.edu"),
    ("Kuber Oza Dey", "kod5261@psu.edu"),
    ("Ata Dural", "axd5991@psu.edu"),
    ("Alexander Fedorychev", "amf7257@psu.edu"),
    ("Reginald Fields", "rxf5209@psu.edu"),
    ("Rensi Nilesh Gajipara", "rng5152@psu.edu"),
    ("Areet Gandhi", "apg6048@psu.edu"),
    ("Anmol Garg", "abg6200@psu.edu"),
    ("Peter Ulanga George", "pgu5002@psu.edu"),
    ("Ritam Ghosh", "rpg5573@psu.edu"),
    ("Riya Goyal", "rmg6205@psu.edu"),
    ("Kathleen Greenleaf", "ksg5218@psu.edu"),
    ("Abigail Elizabeth Gross", "apg5931@psu.edu"),
    ("Sita Vaibhavi Gunturi", "gsv5053@psu.edu"),
    ("Jonathan Nicholas Yun Hamel", "jnh5311@psu.edu"),
    ("HFS Student Scheduler", "scheduler@psu.edu"),
    ("Destiny Hill", "dah6105@psu.edu"),
    ("Apoorva Shashikant Jadhav", "asj5511@psu.edu"),
    ("Steven Tyler Johnson", "stj5169@psu.edu"),
    ("Kathan Sanjay Joshi", "ksj5289@psu.edu"),
    ("AJITH KEVIN ANAND KAMALESAN", "axk6243@psu.edu"),
    ("Sabiha Khan", "skk6224@psu.edu"),
    ("Neha Khatriya", "nfk5315@psu.edu"),
    ("Hyun Subb Kim", "hsk5172@psu.edu"),
    ("PAVANI KOLASANI", "ppk5357@psu.edu"),
    ("Vishnu Koraganji", "vfk5129@psu.edu"),
    ("Jacq Lee", "jxl6891@psu.edu"),
    ("Nelson Divyam Lobo", "ndl5213@psu.edu"),
    ("Yanwen Luo", "ypl5780@psu.edu"),
    ("Maeve Elizabeth Macaulay", "mem6957@psu.edu"),
    ("Jacob Alan Macklin", "jam9242@psu.edu"),
    ("Abhishek Mandar Mahakal", "amm10344@psu.edu"),
    ("Sravani Malla", "sqm6704@psu.edu"),
    ("Sai Madhur Mallampalli", "saimadhurmallampalli@psu.edu"),
    ("Andrew Douglas Mason", "adm6264@psu.edu"),
    ("Patrick Henry McLaughlin", "phm5149@psu.edu"),
    ("Sana Mehmood", "szm6402@psu.edu"),
    ("Sumeet Mekala", "sxm6596@psu.edu"),
    ("Angel De Jesus Mercedes Abreu", "adm6017@psu.edu"),
    ("Max Mikhailov", "msm6530@psu.edu"),
    ("Abhilasha Mishra", "afm6697@psu.edu"),
    ("Sameerah Mohammed", "sqm6271@psu.edu"),
    ("Tyler Jay Muessig", "tpm5690@psu.edu"),
    ("Geethika Naraveni", "gpn5134@psu.edu"),
    ("An Thuy Nguyen", "atn5257@psu.edu"),
    ("Rebecca Nortey", "rmn5441@psu.edu"),
    ("Mannat Kaur Oberoi", "mqo5352@psu.edu"),
    ("Indira Yvette Owembabazi", "iyo5032@psu.edu"),
    ("Mounika Pasham", "mjp7163@psu.edu"),
    ("Darsh Bharatkumar Patel", "dbp5588@psu.edu"),
    ("Disha Mahendrabhai Patel", "dmp6528@psu.edu"),
    ("Nyralee Isabel Perez", "nip5203@psu.edu"),
    ("Varshith Ponnam", "vqp5208@psu.edu"),
    ("Daanesh Potnuri", "dmp6538@psu.edu"),
    ("Saatvik Pradhan", "szp6118@psu.edu"),
    ("Ashna reddy Rapaka", "arr6117@psu.edu"),
    ("Daniel Sunil Kumar Ravi", "dxr5576@psu.edu"),
    ("Siddharth Rayabharam", "nqr5356@psu.edu"),
    ("Adarsh Regulapati", "abr6174@psu.edu"),
    ("Ixzaira Jasmine Rivera", "ijr5083@psu.edu"),
    ("Andres Eduardo Rubio", "aer5788@psu.edu"),
    ("Ganesh Sadanala", "gxs5493@psu.edu"),
    ("Ishika Saini", "ims5409@psu.edu"),
    ("Andrew Sapelli", "ajs9694@psu.edu"),
    ("Aayushi Piyush Shah", "ams12225@psu.edu"),
    ("Sneh Shah", "sbs7057@psu.edu"),
    ("Abhishek Sharma", "axs7326@psu.edu"),
    ("Raghab Sharma", "rps6236@psu.edu"),
    ("Aditya Ketankumar Sheladia", "aps7194@psu.edu"),
    ("Muhammad Usman Siddiqui", "mms8130@psu.edu"),
    ("Rakshit Singh Bist", "rvs6202@psu.edu"),
    ("Joshua Tyler Still", "jts6278@psu.edu"),
    ("Rayyan Syed", "rvs6267@psu.edu"),
    ("Jonathan Tan", "jzt5707@psu.edu"),
    ("CLAUDIO TARALLO", "ckt5383@psu.edu"),
    ("Elena Thankam Thomas", "ext5269@psu.edu"),
    ("Harrison Michael Troy", "hmt5391@psu.edu"),
    ("Tiniira Tubo", "txt5341@psu.edu"),
    ("Vivian Santosh Varughese", "vxv5141@psu.edu"),
    ("Yunxiang Wang", "yzw5705@psu.edu"),
    ("Ta'Nya Abree Williams", "taw5867@psu.edu"),
    ("Harry Ward Winter", "hww5203@psu.edu"),
    ("Manas Diwakar Yawalkar", "mby5247@psu.edu"),
    ("Zihan Zhao", "zxz5500@psu.edu")
]

# Create initial DataFrame with team members
summary_data = pd.DataFrame(team_members, columns=['Name', 'Email'])
summary_data['Points'] = 0
summary_data['Position'] = 'Part-Time Food Service Worker'

# Create an empty DataFrame for transactional data
transactional_data = pd.DataFrame(columns=[
    'Name', 'Shift Time', 'Station', 'Issue', 'Comments', 'Tardy Minutes', 'Uniform Action', 
    'No ID Sent Home', 'No ID Minutes Late', 'Safety Issue Reason', 'Timestamp', 'Manager'
])

# Create a DataFrame for managers
managers_data = pd.DataFrame([
    {"Name": "Manager 1", "Position": "Crew Leader"},
    {"Name": "Manager 2", "Position": "Crew Leader"}
])

# Create a DataFrame for stations
stations_data = pd.DataFrame([
    {"Station Name": "Stacks Pizza"},
    {"Station Name": "Stacks Grill"},
    {"Station Name": "Stacks Server"},
    {"Station Name": "Stacks Deli"},
    {"Station Name": "Stacks Cashier"},
    {"Station Name": "Stacks Dishes"},
    {"Station Name": "Stacks Dining Room/Utility"},
    {"Station Name": "Stacks Receiver"},
    {"Station Name": "Stacks Catering"},
    {"Station Name": "Stacks Expo"},
    {"Station Name": "PSU 2 Go"},
    {"Station Name": "Culinary Assistant"},
    {"Station Name": "Biscottis Cashier"},
    {"Station Name": "Biscottis Barista"},
    {"Station Name": "ID/Main Office"},
    {"Station Name": "Mail Room"},
    {"Station Name": "Catering Crew leader"},
    {"Station Name": "Olmsted Crew leader"}
])

# Save to Excel with multiple sheets
excel_file = 'attendance_records1.xlsx'
with pd.ExcelWriter(excel_file) as writer:
    summary_data.to_excel(writer, sheet_name='Summary', index=False)
    transactional_data.to_excel(writer, sheet_name='Transactions', index=False)
    managers_data.to_excel(writer, sheet_name='Managers', index=False)
    stations_data.to_excel(writer, sheet_name='Stations', index=False)

excel_file
