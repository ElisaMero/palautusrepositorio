*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    kallee
    Set Password    kalle1234
    Set Passwordcheck    kalle1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    y
    Set Password    kalle1234
    Set Passwordcheck    kalle1234
    Submit Credentials
    Register Should Fail With Message    Invalid username, must be at least 3 characters

Register With Valid Username And Invalid Password
    Set Username    yayy
    Set Password    kalleeee
    Set Passwordcheck    kalleeee
    Submit Credentials
    Register Should Fail With Message    Password must contain letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username    yayyy
    Set Password    kalleee345
    Set Passwordcheck    kalleeee324
    Submit Credentials
    Register Should Fail With Message    Passwords are not a match

Login After Successful Registration
    Set Username    kalee
    Set Password    kale1234
    Set Passwordcheck    kale1234
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username    kalee
    Set Password    kale1234
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username    kalee
    Set Password    kale1234
    Set Passwordcheck    kale1234
    Submit Credentials
    Register Should Not Succeed
    Go To Login Page
    Set Username    kalee
    Set Password    kale1234
    Submit Credentials Login
    Login Should Not Succeed


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Welcome Page Should Be Open

Login Should Not Succeed
    Welcome Page Should Be Open

Register Should Not Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Submit Credentials
    Click Button    Register

Submit Credentials Login
    Click Button    Login

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Passwordcheck
    [Arguments]    ${password_conf}
    Input Password    password_confirmation    ${password_conf}

Create User
    Go To Register Page
    Create User    kalle    kalle123
    Register Page Should Be Open
