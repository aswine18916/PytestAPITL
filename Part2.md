Team A

Below are the key sections in a Test Strategy that the team needs to work on

* Testing objectives- Objective is to run the web app in mobile devices, tablets and desktops in chrome and safari
    * An analytics report is very much needed which describes the user devices in percentage, this helps to classify the test coverage across various devices.
        * Devices most of the user’s using- Phone/Tablet model, OS version and Browser combination
        * Viewport testing is very much essential to ensure the compatibility 
    * Cypress implementation in Safari is only an experimental kit, previously it was not there. A good research is very much needed there.
    * Testing in iOS/safari combination is never considered which can be a huge miss.
    * Always think in the customer’s angle. As a QA engineer application has to be tested and executed where the customer does it.
* Testing guidelines- How the testing has to be carried out in different time frames
    * Testing Levels needs to finalised, types of testing  are not defined
* Roles and responsibilities
    * Member responsibilities are not said, who will do what as there are no QA Engineers. As I assume it is a new application some amount of Manual testing is necessary.
* Levels of testing- 
    * Integration and other higher level testing needs to be performed in different environments before Prod and after Dev, like Staging, PreProd. As unit testing is only 50% covered, there can be major/critical functionalities needs to be thoroughly tested which may not have been covered in unit testing.
    * When and how the API has to be tested.
* Test requirements- 
    * Requirements have to be finalised before automating them. Also the automation strategy. 
    * Since team uses Kanban, requirements can change at any point of time and doing the testing for changed requirements across all platforms will be a tedious task. Automation is very much essential here.
* Test deliverable- 
    * Which test artefacts that has to be provided to stakeholders and higher managements
* Entry and exit criteria
    * Definition of entry and exit criteria are needed which helps in reducing doubts and discussion on responsibilities and expectations during the work
* Defect management
    * Defect workflow, triage and reporting are needed which is a key factor and can improve the “lessons learnt”
* What test reports will be provided
    * Test reports to be provided as part of meetings, scheduled runs to different people during different times
* Test environment information and migration procedures
    * What are the different test environment needed and how they are aligned towards actual Prod environment, deployment strategy and CD practices.
    * Continuous runs must be performed in other environments other than in Dev to understand the behaviour of the application before deploying to production
* Test Constraints
    * Since the web app is used across a lot of platforms, the constraints that can come across when deploying a new feature and testing has to be carried out in all the devices/platforms where in time can be a crucial factor.
* Test Risk including project and product risks
    * UAT and PreProd environment testing is needed so that product risks can be minimised and defects can be captured early.
    * Devices and Browser combinations are never told here which is a huge drawback and product quality can be compromised
    * Testing on the API is never told anywhere.


Team B

	Below are the key sections in a Test Strategy that the team needs to work on

* Testing objectives
    * Who uses the APIs and How to test them has to be very clear
* Testing approach
    * API documentation has to be clear so that each and every field in the API response/ input data is well known
* Roles and responsibilities
    * Integration and E2E testing is very much needed and should be defined who will do these.
* Levels of testing
    * As integration is already covered,  E2E testing has to be performed as per the user’s different journeys
* Test requirements
    * What is each API and where they come in the user’s journey has to be deeply analysed
* Test deliverable
    * Artifacts has to be clearly called out, which of them will be delivered to whom and what time point of time
*  Entry and exit criteria
    * Definition of entry and exit criteria are needed which helps in reducing doubts and discussion on responsibilities and expectations during the work
* Defect management
    * Defect workflow, triage and reporting are needed which is a key factor and can improve the “lessons learnt”
* What test reports will be provided
    * Frequency of test reports to be provided to stakeholders and higher managements during various stages of the test cycle
* Test environment information and migration procedures
    * What are the different test environment needed and how they are aligned towards actual Prod environment, deployment strategy and CD practices.
    * Continuous runs must be performed in other environments other than in Dev to understand the behaviour of the application before deploying to production
* Test Constraints
    * E2E testing has to be performed here which will help us to determine the user flows and API performances including response times taken in different situation with different sets of data.
* Test Risk including project and product risks
    * Integration of the APIs with front end components is not tested here which has to be performed before deployment to higher environments

