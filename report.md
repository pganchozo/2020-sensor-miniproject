Elisabeth Garfield & Patricia Ganchozo EC 463 Senior Design Mini Project Report September 17 2020

Task 0: Python Websockets

After running both "ws_server.py" and "ws_client.py", the simulation's greeting message is "ECE Senior Capstone IoT simulator". Afterwards, data begins to come in every few seconds as seen in the image below.

![Screen Shot 2020-09-15 at 10 44 27 PM](https://user-images.githubusercontent.com/45433428/93286370-160f7e00-f7a5-11ea-88e8-d420c6d8d727.png)




## Task 1: Data Flow

After adding code to the "ws_client.py" module, the data read by the sensor is saved to a text file. To specify that the data should be saved, the following must be run on the terminal: python ws_client.py "filename".



## Task 2: Analysis

The median and variance observed from the temperature data after collecting 971 values can be seen in the table 1 below:

<table>
  <tr>
    <th>Room</th>
    <th>Median</th>
    <th>Variance</th>
  </tr>
  <tr>
    <td>office</td>
    <td>22.999100</td>
    <td>415.425114</td>
  </tr>
  <tr>
    <td>lab1</td>
    <td>21.009781</td>
    <td>33.386524</td>
  </tr>
  <tr>
    <td>class1</td>
    <td>26.999745</td>
    <td>110.491456</td>
  </tr>
</table>


The median and variance observed from the occupancy data after collecting 971 values can be seen in table 2 below:

<table>
  <tr>
    <th>Room</th>
    <th>Median</th>
    <th>Variance</th>
  </tr>
  <tr>
    <td>office</td>
    <td>2.0</td>
    <td>1.972535</td>
  </tr>
  <tr>
    <td>lab1</td>
    <td>5.0</td>
    <td>4.581467</td>
  </tr>
  <tr>
    <td>class1</td>
    <td>19.0</td>
    <td>19.908827</td>
  </tr>
</table>

The probability density function for each of the sensors can be seen below:

![Screen Shot 2020-09-15 at 7 50 44 PM](https://user-images.githubusercontent.com/45433428/93287793-6c31f080-f7a8-11ea-917c-2ade5c2947a3.png)


The mean and variance of the time interval can be seen in table 3 below:

<table>
  <tr>
    <th>Mean</th>
    <th>Variance</th>
  </tr>
  <tr>
    <td>1.0096422506361324</td>
    <td>1.0477646527529447</td>
  </tr>
</table>

## Task 3: Design

In order to implement an algorithm that detects anomalies in the temperature dataset a separate module "detection.py" was created. Similar to analyze.py, the detection module takes as input the text file with the dataset. Before identifying anomalies in the data, the mean and standard deviation of the temperature values for each room were calculated using built-in Python functions.


## Task 4: Conclusion

For EC 463 Senior Design, Patricia and I were asked to program a system to report and find average temperatures based on a set of simulated sensors provided by the staff. Using Python websockets libraries, as opposed to a compiled language like C++ websockets, increased the difficulty of this miniproject as Patricia and I are relatively unfamiliar with Python and more comfortable with a C++ library. It would be preferable for the server to poll the sensors rather than have the senors reach out to the server when they have data so that the burden lays on the server rather than the sensors. A minor disadvantage to this method could be that if the server were to go down, none of the sensors would report data, while if a sensor goes down, the server would still receive data. This disadvantage goes either way with both methods.

The most similar instance of this simulation and its stated requirements is, in our minds, a Nest Home type operation. This could also be applied to larger settings, including weather mapping over fields to determine prime locations for different types of crops. However, this simulation is deficient in that it does not account for humidity, air quality, light exposure, UV ratings, or other qualities that could affect the "feel" or effective temperature in the room.
