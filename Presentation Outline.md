# Presentation Outline  
## 1. Software Introduction  <!-- Short intro, 1 min is ok-->
<!-- can we copy some paragraph from proposal aka README.md?-->

## 2. Software Structure  <!-- about 6 min-->
General workflow:  <!-- We should make it into a graph-->
1. User input city name.  
2. Frontend sends search request to backend.  
3. Backend search city to get a possible city list, containing location info.  
4. Pass this list to frontend.  
5. User Select a city and request weather data.  
6. Search DB first, if expired, fetch from API.  
7. Return full weather data to frontend and show to user.  

### 2.1. Frontend  
_(Brief introduction of codes and functions)_  

### 2.2. Backend  
- Flask server to communicate with frontend.  
- Python as main language. As it is already widely used and convenient for this project.  
- Backend is highly modularized. Easy to maintain and expand.
- Get data from DB first, if expired (60s / 12hrs), fetch from API.
- Data structure and process is well-designed to enhance efficiency.  

### 2.3. Database  
- Use mySQL  
- For test, I deployed a mySQL Docker on my Workstation. In the future we may consider using cloud services.  
- SQL as cache since API has limitations.  
- Two tables: current & 5d forecast, containing all necessary data.

## 3. Stage results  
### 3.1. Group meetings  <!-- about 1-2 min-->
**Acceptance criteria**  
Frontend:  

Backend:  
Most of the functions receive simple inputs and return a list.  
eg.  
`get_city_list(city_name: str) -> List[Name: str, State: str, Region: str]`  
`get_current_weather(lat: float, lon: float) -> List[Weather information]`  
Since they are highly modularized, maintaining and expanding is easy.  

**Tools we decided to use**  
- WeChat  
The main communication tool.  
- Gitee as VCS gann 
_Put screenshot and link into slides._  
After discussion, we decided to use Gitee as our VCS. Since some of our group members living in China Mainland, comparing to GitHub, Gitee is more stable and convenient.  
- XMind online  
Put screenshot into slides.  
We use mind map to build our Work Breakdown Structure. XMind online is capable of online editing and collaboration, which is perfect for our group work.  
- Burn down chart  
We are still discussing the workflow to update the chart.
<!-- Can we make a Burn down chart before the first pre?-->
- Excel
Simple gannt chart and task list for time management.  

### 3.2. Issues and solutions by now  <!-- 1min-->
**Issue 1**  
Free api of OpenWeather can only get weather data of 5 days, as we initially planned to get 7 days.  
Solution: Since the frontend is in design and the database is still under construction, we changed the frontend design and database structure to adapt this change.  

**Issue 2**  <!-- Optional-->

### 3.3. Time management
**Initial plan**  <!-- Show only, 30s is ok-->

| Phase                         | Time    | Task                                                                  | Responsible        |
|-------------------------------|---------|-----------------------------------------------------------------------|--------------------|
| **Requirements Analysis & Planning** | Week 1-3 | - Define feature requirements (real-time weather, future forecasts, etc.) <br> - Choose API provider and define API call limits | Everyone          |
| **Design Phase**               | Week 4-5 | - UI/UX design (app interface prototype, interaction design) <br> - Define color scheme and app style  | UI/UX Designer     |
| **Frontend Development**       | Week 6-12 | - Develop weather query page <br> - Implement real-time weather and future forecast display <br> - Optimize and test frontend pages | Frontend Developer |
| **Backend Development**        | Week 4-12 | - API integration (fetch and parse weather data) <br> - Handle user requests and data transmission  | Backend Developer  |
| **Integration & Testing**      | Week 12-14 | - Integrate frontend and backend functionalities <br> - Conduct comprehensive testing (functional, performance, UI/UX testing, etc.) | Everyone          |
| **Launch & Optimization**      | Week 14-15 | - Launch the app <br> - Collect user feedback and optimize the app  | Everyone          |

**Gantt chart** <!-- Show with little talks, 1-2 min-->
<!-- Fake pass, fake future. -->
Progress we have made (time may not accurate):  
Week 1-2  
Form a group.  
Week 3  
Decide the orientation.  
Week 4-5  
Group meetings.  
Register API & API testing.  
Backend module design & database design.  
DB & Backend data structure design & alignment.  
Week 6-7  
Group meetings.  
Frontend demo.  
Backend module design & database build.  
Frontend & Backend data structure design & alignment.  
Week 8  
Prepare for stage pre.
