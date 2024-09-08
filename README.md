# Automation Test
-----------------

### [Assignment 1](assignment_1/) - **UI Testing Automation**

##### Objective
Automation of Resolution Testing and Screenshots using Selenium Web Drivers.

> [!NOTE]
> We want the candidate to test and check the website is opening correctly in multiple
> browsers and resolutions. We want them to create a folder for each Browser and
> Resolution where in they save the screenshot of the whole page saved.
>

- **INPUT**
    - [Sitemap.xml](https://www.getcalley.com/page-sitemap.xml) file for the website or XLS file for all the pages of the website.
    - List of Resolutions & Devices on which the test runs need to be automated.

- **OUTPUT**
    - Folder for the screenshots taken with the following structure
        - Device name > Resolution > Screenshot-date-time.png
    - [A video of the Test in Running Mode.](assignment_1/Assignment_1.mkv)
    - [Script to check and validation of test case.](assignment_2/)
    - [Working Video](assignment_1/Assignment_1.mkv)

- **List of Screen Resolutions & Devices**
    - **Desktop -**
        - 1920×1080
        - 1366×768
        - 1536×864

    - **Mobile -**
        - 360×640
        - 414×896
        - 375×667

> [!IMPORTANT]
> Tests to be done for - `Chrome`, `Firefox` and `Safari`



### [Assignment 2](assignment_2/) - **Functional Testing Automation**

##### Objective
Write a test to check the functional flow of the application using Selenium Web Drivers.

> [!NOTE]
> This is a test in which we have to log in to a web application using the supplied credentials and upload an XLS
> file that is provided. Once uploaded, there will be validations that need to be checked on the page, and we
> have to take a screenshot of the final output received.

+ **INPUT**
  + URL for the Panel - [https://demo.dealsdray.com/](https://demo.dealsdray.com/)
  + Login credentials for the Panel
    - Username : `prexo.mis@dealsdray.com`
    - Password : `prexo.mis@dealsdray.com`
  + [XLS file to upload](assignment_2/demo-data.xlsx)

+ **OUTPUT**
  + [Video for the Login process & File upload ](assignment_2/Assignment_2.mkv)
  + [Screenshot of the Final Output page](assignment_2/Screenshot-24-09-07-00-22-24.png)
  + [Script for the Test Written to be provided](assignment_2/Assignment.py)
