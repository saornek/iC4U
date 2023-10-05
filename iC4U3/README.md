# IC4U3
_Tasks by [IAADP](https://iaadp.org/membership/iaadp-minimum-training-standards-for-public-access/tasks-performed-by-guide-hearing-and-service-dogs/)_

## IC4U3 To-Do List Batch #2 - Visually Impaired

### Tasks:
#### LOCATE OBJECTS ON COMMAND
* Find an exit from a room; indicate door knob
* Find the elevator at a business
* Find an empty seat, bench, or unoccupied area
* Follow a designated person, such as a waiter, to restaurant table, clerk to elevator, etc.

### To-Do For Door Tracker
- [x] ~Create a new dataset on Roboflow.~ _Done on 08/02/23_
- [x] ~Add doorknob images.~ _Done on 08/02/23_
- [x] ~Add hand images.~ _Done on 08/03/23_
- [x] ~Train the dataset to a pytorch weight.~ _Done on 08/03/23_
- [x] ~Test the pytorch weight via collab.~ _Done on 08/03/23_
- [x] ~Test the pytorch weight with zed camera~ _Done on 08/04/23_
  - [x] ~Add better hand images~ _Done on 08/04/23_
  - [x] ~Make door undetectable in code.~ _Done on 08/04/23_
- [x] ~Create a code which will calculate distance of hand and door knob~ _Done on 09/01/23_
- [x] ~Add a code in which the guide dog guides the person's hand on the door knob.~ _Done on 09/23/23_
- [ ] Test the code.
- [ ] Take a promotional video.

### To-Do For Elevator Tracker
- [ ] Create a new dataset.
- [ ] Add elevator images.
- [ ] Label the elevator states (Open-Closed)
- [ ] Train the dataset to a pytorch weight.
- [ ] Write a code for iC4U to inform the person of the elevator and its state.
- [ ] Test the code
- [ ] Take a promotional video.

### To-Do For Empty Seat Finder.
- [ ] Create a new dataset.
- [ ] Add seat images.
- [ ] Add person sitting on a chair images
- [ ] Label the seats as empty or full
- [ ] Train the dataset to a pytorch weight.
- [ ] Write a code for iC4U to inform the person of the seat and its state.
- [ ] Take a promotional video.

### To-Do for Person Follower
- [ ] Use ZED's pre-trained and pre-downloaded dataset and code.
- [ ] Limit it to only person detection.
- [ ] Create a code that combines after talking do person detection.
- [ ] Get the person state (moving or idle.)
- [ ] Get the person's speed etc.
- [ ] Then follow the person.
- [ ] Take a promotional video.


---

## IC4U3 To-Do List Batch #1 __(COMPLETED)__ -- Visualy Impaired

### To-Do for Grocery Project
- [x] ~Raw Web Scrapping Code~ _Done on 06/22/23_ 
  - [x] ~Web Scrapping Code Get Title~ _Done on 06/21/23_
  - [x] ~Web Scrapping Code Get Availability~ _Done on 06/21/23_
- [x] ~Add data frame ASIN access to raw web scrapping code~ _Done on 06/23/23_
- [x] ~Combine grocery vision code and the web scrapping code (Using exporter.py Template)~ _Done on 06/23/23_
- [x] ~Test~ _Done on 06/24/23_
- [x] ~Take a promotional video~ _Done on 06/26/23_
- [x] ~Combine sub-outputs(title,availability,price) to a total output.~ _Done on 06/24/23_

### To-Do for City Vision
- [x] ~Write the tracking_viewer code, so it could export the objects in the frame.~ _Done on 06/20/23_
- [x] ~Test the raw code with the extracted frame image~ _Done on 06/20/23_
- [x] ~If both tasks are successfully complete, try the exporter code~ _Done on 06/20/23_
- [x] ~Improve the visuals of the code~ _Done on 06/20/23_
- [x] ~Test it outside, and take a promotional video~ _Done on 06/22/23_
- [x] ~Edit Promotional Video~ _Done on 06/22/23_
- [x] ~Take Out Yellow Detection as Not needed.~ _Done on 06/23/23_
- [x] ~Add more color palettes to green and red~ _Done on 06/23/23_
- [ ] Train the dataset a little more (with black traffic lights).
- [ ] Do Test 2 Outside

### To-Do for Money Detection
- [x] ~Take Photos of dollars with ZED~ _Done on 06/28/23_
- [x] ~Create a new project on Roboflow~ _Done on 07/01/23_
- [x] ~Gather images online and from other datasets~ _Done on 07/01/23_
- [x] ~Work on preprocessing and cleaning your dataset~ _Done on 07/05/23_
- [x] ~Train the dataset~ _Done on 07/05/23_
- [x] ~Update the previous money detection code(only detects if its money or not) to a dollar quantity detectable code~ _Done on 07/06/23_
- [x] ~Test the code with the new weight~ _Done on 07/07/23_
- [x] ~Take a promotional video~ _Done on 07/07/23_
