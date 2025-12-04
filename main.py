from pyscript import display, document

club_info = {"club_name": {"Name": "Marching Band",
                  "Moderator": "Mr.Alumno",
                  "Meeting Schedule": "Monday, Tuesday, and Wednesday at 3:00 PM - 4:30 PM",
                  "Description": "The Marching Band is a group of talented musicians who perform at school events and competitions.",
                  "Location": "Marching Band Room"
                  "No. Of Members": "42"}}, 

    {"club_name2": {"Name": "Dance Club",
                   "Moderator": "Mr. Cases",
                   "Meeting Schedule": "Tuesday 3:00 PM - 5:00 PM",
                   "Description": "The Dance Club is a vibrant group that explores various dance styles and performs at school functions.",
                   "Location": "Teatro Preciosza"
                   "No. Of Members": "30"}},
    
    {"club_name3": {"Name": "Math Club",
                   "Moderator": "Mr. Gabuya",
                   "Meeting Schedule": "Monday 2:30 PM - 4:30 PM ",
                   "Description": "The Math Club is dedicated to enhancing students' mathematical skills through competitions and collaborative learning.",
                   "Location": "Room 404"
                   "No. Of Members": "16"}},

    {"club_name4": {"Name": "Science Club",
                   "Moderator": "Ms. Maramag",
                   "Meeting Schedule": "Tuesday 3:00 PM - 5:00 PM || Friday 2:00 PM - 3:00PM"
                   "Description": "The Science Club fosters a love for science through experiments, projects, and field trips.",
                   "Location": "Room 404"
                   "No. Of Members": "18"}},
    
    {"club_name5": {"Name": "Cadet Officer Candidate Course (COCC)",
                   "Moderator": "Ms. David",
                   "Meeting Schedule": "Wednesday 2:30 PM - 4:30 PM ",
                   "Description": "The COCC is a leadership training program that prepares students for future roles in the cadet corps.",
                   "Location": "Quadrangle / Teatro Preciosza / 4th Floor"
                   "No. Of Members": "24"}},
    
    {"club_name6": {"Name": "Glee Club",
                   "Moderator": "Mr. Martin",
                   "Meeting Schedule": "Monday & Friday 3:00 PM - 4:30 PM",
                   "Description": "The Glee Club is a musical ensemble that performs vocal music at school events and competitions.",
                   "Location": "HS Music Room",
                   "No. Of Members": "28"}},
    
    {"club_name7": {"Name": "Communication Arts Club",
                   "Moderator": "Ms. Fernandez",
                   "Meeting Schedule": "Wednesday & Friday 3:00 PM - 4:00 PM",
                   "Description": "The Communication Arts Club focuses on developing students' skills in media, journalism, and public speaking.",
                   "Location": "Room 406"
                   "No. Of Members": "23"}}
                
      





def Show_Club(e):
   document.getElementById("club_info").innerHTML = ""
   selected_club = document.getElementById("output").value
   info = club_info.get(selected_club, club_info[""])
   
   