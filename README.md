# youtube_data_extractor_pytube_data_api

This project can be used to extract a YouTube channel's entire history about it's video's upload time,revenue generated, views,etc..It uses YouTube data API and pytube to extract the listed information's
It's front-end is developed using ReactJS and back-end is developed using Flask & Python.

To first run the back-end you have to install the required packages listed in the requirements.txt file. It can be done using the following steps:-

1. First clone the project and open the back-end path in your terminal.
2. Then enter the below command
Command:- pip -r install requirements.txt
3. Replace your Outlook mail and password in the send_mail.py file to send your mail.
4. Then get the YouTube Data API key from Google Cloud Console and paste it in the youtube_extract.py file.
5. Now run the flask_receiver.py file to start the back-end server.

To first run the front-end you have to install the required packages listed below. It can be done using the following steps:-

1. First install NodeJS and ReactJS in your system.
2. Then create a new react project using the command below
Command:- npx create-react-app my-app
3. Then install the following packages using "npm install"

"axios": "^1.3.4",
"react": "^18.2.0",
"react-dom": "^18.2.0",
"react-router-dom": "^6.10.0",

4. Now start the front-end server using the command below:
Command: npm start
5. Then enter any YouTube channel link for example:
https://www.youtube.com/watch?v=mMHtK908cuo
6. Now emter your email for which you want to get the report mailed
7. Click Submit after the steps 6 & 7.

Note: The data report provided is not accurate it is an approximate value based on the data given by pytube and YouTube Data API.
