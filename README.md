![imaage1](https://github.com/abhijeetsp98/Django/blob/master/Screenshot%20from%202020-09-13%2018-18-29.png)
# Django
Check out requirement file for all dependency along with those we need face_recognition library which futher need cmake,dlib library check out stackoverflow if any problem comes in at the time of installation.

To run the project use: python3 manage.py runserver

# System Overview:
Admin: This is the one who have entire control over the data and have authority to update delete the data in the system.
Party: Individual party have the their own credential to login the system where they will register their own candidiate for election.
People: People will comes in and cast their votes their data has been added by the admin and voting is done by admin only so to perform the voting login with admin.

# Credential:
Admin: go to http://127.0.0.1:8000/admin/ <br>
username: ECI <br>
password: testing321 <br>

# Party:
username:BJP  # Name of the party and password is same for all <br>
password:testing321 <br>

# Voting Process:
Add user data using amdin credentails onces add then use voting button to perform voiting.
1. Soon after you tap on it webcam will start.
2. Type s to take snapshot.
3. Then face_recognition will detect the user after that if voted then tells it or else display list of candidates according to the user's location.
4. User will cast the vote and registered as the user wo casted the vote.

![imaage1](https://github.com/abhijeetsp98/Django/blob/master/Screenshot%20from%202020-09-13%2018-15-11.png)
