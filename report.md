Elisabeth Garfield & Patricia Ganchozo EC 463 Senior Design Mini Project Report September 17 2020

Task 0

After running both "ws_server.py" and "ws_client.py", the simulation's greeting message is "ECE Senior Capstone IoT simulator". Afterwards, data begins to come in every few seconds as seen in the image below.

![Screen Shot 2020-09-15 at 10 44 27 PM](https://user-images.githubusercontent.com/45433428/93286370-160f7e00-f7a5-11ea-88e8-d420c6d8d727.png)


Task 1

After adding code to the "ws_client.py" module, the data read by the sensor is saved to a text file. To specify that the data should be saved, the following must be run on the terminal: python ws_client.py "filename".

Task 2

For EC 463 Senior Design, Patricia and I were asked to program a system to report and find average temperatures based on a set of simulated sensors provided by the staff. Using Python websockets libraries, as opposed to a compiled language like C++ websockets, increased the difficulty of this miniproject as Patricia and I are relatively unfamiliar with Python and more comfortable with a C++ library. It would be preferable for the server to poll the sensors rather than have the senors reach out to the server when they have data so that the burden lays on the server rather than the sensors. A minor disadvantage to this method could be that if the server were to go down, none of the sensors would report data, while if a sensor goes down, the server would still receive data. This disadvantage goes either way with both methods.

The most similar instance of this simulation and its stated requirements is, in our minds, a Nest Home type operation. This could also be applied to larger settings, including weather mapping over fields to determine prime locations for different types of crops. However, this simulation is deficient in that it does not account for humidity, air quality, light exposure, UV ratings, or other qualities that could affect the "feel" or effective temperature in the room.