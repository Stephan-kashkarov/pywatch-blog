# PyWatch & Formula
An smart-watch and sudo-operating system combo. Made following this [template](https://docs.google.com/document/d/1r0GTRO4lXpps-CGbwxwoR6mGB3-vlfBPeM9mDhD-C5o/edit)
___

## Project Definition Infromation

| Field                      | Response                |
| ------------------------ | -------------------------- |
| **Project Name** | PyWatch & Formula |
| **Project Team**  | Stephan Kashkarov |
| **Mentoring Teacher** | Edwin Griffin   |
| **Start Date**       | 5 Aug 2019               |
___

### Idea
The idea behind PyWatch is to create a fully functional smart watch in both software and hardware with less cost then other contemporary smart-watches. This project consists of the following:
1. Fully functional smart watch hardware
2. Reuseable expandable react like OS
3. Formula Appstore website
___

### Purpose
PyWatch was created to be a cheaper alternative to other smart wearables such as the apple watch. These devices cost upwards of $300 and are therefore unafforable for most of society. The aim of smart watch is to use cheap components to create a fully functional smart-watch that can be used by the masses. Formula's aim is to create a simple react like sudo-OS which can be easily reused across multiple devices complete with app-store and a dev friendly API written in MicroPython.
___
### Capabilities

| Member | Capabilities |
| ----------- | ---------------- |
| Stephan Kashkarov |  Python, MicroPython, C++, Arduino, Java, Javascript, Haskell, C#, CSS, HTML, Various ML APIs including Keras and PyTorch, Flask and KiCad.|
___
## Objectives
| Outcomes | Description |
| --- | --- |
| Functions as clock | has the ability to show correct time |
| Touch Display input | The device has the ability to take a touch input and display its location on the screen |
| Multiple App | Has the ability to have two different apps on device |
| Functional App store | Appstore contains a variety of Apps that can be downloaded and run on PyWatch |
___
## Scope
| In Scope | Out of Scope |
| --- | --- |
| Basic functionalities for smartwatch (like interacting with accelerometer) | Security of Apps on store |
| Functioning App store | Creating an Arduino based wrapper |
| Create Rendering engine for formula code | Writing Libraries to interface with display ICs |
___
## Time Frame
The timeframe of this project is as follows:
1. Week 8 of term 3 | Have working clock prototype
2. Week 1 of term 4 | Have basic App functionality
3. Week 3 of term 4 | Have Functioning App store
___
### Third Party Interest
| Party | Involvement |
| --- | --- |
| App developers | Needed for feedback on Framework and Basic Testing |
| Consumers | Needed for funding and interviewed for feature requests |
___
### Constraints
| Constraint | Impact |
| --- | --- |
| Use Third party MicroPython libraries where possible | Low |
| Maintain sub $100 Budget (per unit) | Med |
| Keep formula considerably lower than Flash Memory size | High |
| Ensuring scope doesn't grow exponentially | High |
| Ensure OS runs well | Low |
___
### Feesability
| Skill | Resource |
| --- | --- |
| Hardware Integration | Knowlege of electonic interactions and common protocals such as I2C and SPI |
| Rendering Engine | Knowlege of browser internals, HTML rendering and React design philosophy|
| App-store Web interface | Knowlege of Flask and MicroPython Networking |
___

### Roles

| Member | Responsabilites |
| --- | --- |
| Stephan Kashkarov | Hardware design and integration, OS development, App Framework Development, App store Web portal development, PR, SEO, CEO, CFO, WHS. So the whole project.|
___
### Inital Issues
| Issue | Desc |
| --- | --- |
| Lack of Hardware | As the project is in its infancy the focus has been in the hardware rather then software. Due to the hardware design not yet being finalised the software development may not take any meaningful form and hence has not yet been started. |
| Growing Project scope | The scope of the project has been growing exponentially in the leadup to pycon which ultimately lead to the projects failure. To combat this a MVP has been defined and most work has been restarted. |
| Shipping times and prices | The shipping times and prices have resulted in delayed starting of the project. As parts have not arrived for basic manufacturing. |
___
### Risks
| Risk | Desc | Impact | Solution |
| --- | --- | --- | --- |
| Sickness | Team member becomes sick | L | Deadlines conservatively set |
| Memory Issues | Formula code becomes too large to fit onto flash memory | H | Flash memory expanded from defaults |
| Complexity and scope | The complexity of this task could lead to problems down the line if scope keeps growing | H | make a set of targets and stick with them |
___
### Timeline
| Deliverable | Duration | Completion Date | Dependencies |
| --- | --- | --- | --- |
| Basic clock | 1 Week | 26 August | Basic Hardware (out of scope)|
| Basic pedometer App | 3 Weeks | 16 September | Basic Clock |
| Appstore | 1 Week | 21 September | Basic App |