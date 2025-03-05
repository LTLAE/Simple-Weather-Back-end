<div align="center">
    <h1>Simple Weather</h1>
</div>  

## Team members    
水流正在引导 -  UI designer, Test engineer  
Fill name here  - PM, Frontend Developer  
Longtail Amethyst Eralbrunia - Architecture designer, Backend Developer  

## Background  
Nowadays, weather forecast is a vital to our daily life. Knowing what the weather will be like in the next few hours or days can help us plan or adjust our activities. We expect to give users a convenient and pleasant experience when they check the weather.  
In order to understand how software management works and practice our software management skills, we decided to develop a weather app. It will be suitable for our level and skills and would not be much too complex to handle.  
We are looking forward to manage this project in a professional way and push the process according to our learning progress.  

## Project description and scope  
- Topic: A web application (website) that provides weather forecast and other related information.  
- Goals: Show weather condition including weather, temperature, humidity, wind speed and so on according to user's demand. Such as specific location, time, etc. Meanwhile some relevant suggestions like what to wear and recommended activities.  
- Scope: Our target is to present weather information in a user-friendly way. Users can access our app simply by a web browser. The application will only present basic information. Professional data like high-altitude wind speed, satellite radar reflectivity, cloud temperature and lightning information will not be included.  

## SWOT Analysis  
**Strengths**  
- Simple and User-Friendly Interface  
Unlike many complex weather apps on the market, our app focuses on a clean design that provides core weather information, allowing users to quickly access the data they need.  
- High Accuracy and Real-Time Updates  
By using the OpenWeatherMap API, we ensure the accuracy and timeliness of the weather data, meeting users' demand for real-time weather updates.  
- Personalization Features  
Users can save frequently used cities and receive scheduled notifications, enhancing the user experience.  

**Weaknesses**  
- Dependence on External API  
The app relies on the OpenWeatherMap API, which might lead to potential issues like service outages, access limits, or costs. If the API encounters problems, it could affect the app's stability and reliability.  
- Basic Features  
Compared to feature-rich weather apps, our app focuses on simple functionalities, which may not meet the needs of advanced users who require more detailed or professional weather data.  
- Intense Market Competition  
There are already many mature weather apps in the market, creating fierce competition. Gaining users and promoting the app may require additional resources and time.  

**Opportunities**  
- More people are focusing on real-time weather updates.   
Climate change causing unstable weather patterns. A simple, effective weather app could attract a large user base.  
- Widespread Use of Mobile Applications  
With the increasing use of smartphones, the demand for convenient and efficient weather apps continues to grow. Mobile devices provide a broader user base for our app.  

**Threats**  
- API Costs and Limits  
The OpenWeatherMap API has usage limitations on the free tier. As the user base grows, there may be a need to pay for API usage, which increases costs.  
- Technical Risks  
If there are issues with API integration, data synchronization, or other technical aspects, it could result in inaccurate data or app failures, negatively impacting the user experience.  
- User Privacy Concerns  
Since the app requires users' geo-location, there is a potential risk of privacy breaches if user data is not handled properly.  

## Function Requirements  
- The application will provide fundamental and punctual weather information to users.  
- The application will allow users to obtain weather forecast for the next 7 days.  
- The application will provide clothing suggestions to users.  
- The application will give users some recommended activities according to the weather.  
- The application shall be able to search weather information by location.  

## Non-Functional Requirements  
- The application will need internet access to update weather information.    
- The application will need a web browser to render its interface.  
- If the user want to check the weather of current location, location service should be enabled.  

## Architecture and Technical approach  
- Frontend: HTML, CSS, JavaScript, React.js  
- Backend: Python, Node.js, OpenWeatherMap API  
- Database: MySQL  

## Risk identification  
- Server will need stable and reliable internet connection.  
- Weather information need to be updated in time.  
- The API service may have the chance to be interrupted or inaccessible.  
- If too many data or request was made, the interface may load slowly or stall.  
- When user allowed the application to use their location, some privacy data like location information will be sent to the server.  

## Budget and Timeline  
1. Development Tools/Software
   - IDEs: Free for now.   
   - Design Tools: Free  
   - If there is further need, we may consider purchasing a license.  

2. Weather API Costs
   - Open weather API: Free for now.
   - It is generally sufficient for now. If there is further need, we may consider purchasing a paid plan.  

3. Server Costs
   - An entry-level plan from a cloud service provider. Estimated cost: around $50-100/month.  

## Timeline

| Phase                         | Time    | Task                                                                  | Responsible        |
|-------------------------------|---------|-----------------------------------------------------------------------|--------------------|
| **Requirements Analysis & Planning** | Week 1-3 | - Define feature requirements (real-time weather, future forecasts, etc.) <br> - Choose API provider and define API call limits | Everyone          |
| **Design Phase**               | Week 4-5 | - UI/UX design (app interface prototype, interaction design) <br> - Define color scheme and app style  | UI/UX Designer     |
| **Frontend Development**       | Week 6-12 | - Develop weather query page <br> - Implement real-time weather and future forecast display <br> - Optimize and test frontend pages | Frontend Developer |
| **Backend Development**        | Week 4-12 | - API integration (fetch and parse weather data) <br> - Handle user requests and data transmission  | Backend Developer  |
| **Integration & Testing**      | Week 12-14 | - Integrate frontend and backend functionalities <br> - Conduct comprehensive testing (functional, performance, UI/UX testing, etc.) | Everyone          |
| **Launch & Optimization**      | Week 14-15 | - Launch the app <br> - Collect user feedback and optimize the app  | Everyone          |

Total Duration: About 16 weeks.



## Conclusion
In conclusion, this weather app project aims to provide users with essential weather information in an intuitive and accessible way. We strive to ensure that users accurate information to their needs. The project will offer a valuable experience in software management and development. All in all, we look forward to completing the project and delivering a functional and reliable tool for users.  
