
# Temperature & Humidity

I have chosen to follow the course on DataScience for my study in HR




## Code explanation
![App Screenshot](https://cdn.discordapp.com/attachments/1073274328227000332/1099081842856042506/carbon.png)

In order to make a functioning program that can measure the temperature of the raspberry pi and the humidity of the room, i imported the `SenseHat`library and built in libraries such as `requests` and `time`

When I created my ThingSpeak channel I made 2 fields: Temperature and Humidity.

I copied the API key from my ThingSpeak channel and the endpoint too.

![App Screenshot](https://cdn.discordapp.com/attachments/1073274328227000332/1099083923746730084/carbon_4.png)

The next step was to declare those 2 fields in python and to initialize my SenseHat library.

![App Screenshot](https://cdn.discordapp.com/attachments/1073274328227000332/1099083321822167220/carbon_2.png)

Next i created a while loop that gets the temperature and the humidity from the senseHat meeting and it prints them out in my terminal for reference, then the payload and the response were created to post them in ThingSpeak. Lastly i made a timer that waits every 15 seconds to post the data on ThingsSpeak.



## Demo

![App Screenshot](https://cdn.discordapp.com/attachments/1073274328227000332/1099085064266059846/Screenshot_2023-04-21_at_23.31.35.png)

As you can see there are 2 charts, the Temperature chart and the Humidity chart, both contain the data that has been measured by my sensehat.

![App Screenshot](https://media.discordapp.net/attachments/1073274328227000332/1099085243786469386/Screenshot_2023-04-21_at_23.32.15.png?width=2062&height=1138)

Here is the Write Api key that was used to insert data into those 2 charts.

## Video Link
Hier is de video voorbeeld van mijn project: 
https://cdn.discordapp.com/attachments/1037350971753373819/1099093149319700690/8mb.video-Uqb-wzobpnkE.mp4

