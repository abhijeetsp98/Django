# Django

This project demonstrates an online verification/voting/attendance system which has been made using the Django framework and face_recogniton library ( https://github.com/ageitgey/face_recognition ) for detecting faces and directly allow the user to do a respective job. The basic fundamental of website structure is inspired by Corey Schafer ( https://github.com/CoreyMSchafer ) feel free to check it out to have an overview of database and data entries use admin section having credentials ECI and testing321 .


We have three separte django app for handling their data separately as User, Public and Blog. Where user represents data of main party and it is one to one associated with Blog entries this part has been inherited from the code by CoreyMSchafer so it is not changed. Public represents the data of public who are intersted in performing the specific task in this case it's voting. Finally we have Blog which basically handles the party data. 

For recognising people we have use the github library listed above we have created an folder within media where all data is saved regarding know people and testing people's faces soon as people is verified we then allow it to caste vote and based on the choice we then update the respective fields.
