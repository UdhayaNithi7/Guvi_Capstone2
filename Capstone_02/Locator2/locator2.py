
class Orange_locat2:

# Locator for accessing orangehrm login page and reset link page 
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    forgot_password = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
    username_in_forgot_password = "username"
    reset_button = '/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]'
    reset_message = '/html/body/div/div[1]/div[1]/div/h6[text()="Reset Password link sent successfully"]'

# Locators for Login input fields and accessing admin tab and elements od admin tab 

    username_in_launchpage = "username"
    password_in_launchpage = "password"
    login_button = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
    admin_tab = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
    user_management ='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    jobs = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'
    organization ='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]'
    qualification = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span'
    nationalites = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a'
    corporate_branding = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a'
    configuration = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span'

# Locators for side pane Menu Options in orangeHRM 

    pim = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    leave = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span'
    time = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a'
    recruiments = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span'
    my_info = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'
    perfomance = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span'
    dashboard = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span'
    directory = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span'
    maintenance = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span'
    claim = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span'
    buzz = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'