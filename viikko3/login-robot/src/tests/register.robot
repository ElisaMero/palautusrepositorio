*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User
*** Test Cases ***

Register With Valid Username And Password
    Input Credentials  hekk  hek12345
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  h  jhgskdf34567
    Output Should Contain  Invalid username, must be at least 3 characters

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  hello23459  kkgjdifjut5437
    Output Should Contain  Invalid username, must contain characters

Register With Valid Username And Too Short Password
    Input Credentials  hellooo  kk32
    Output Should Contain  Must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  helloooo  kkjglsoigushdjfils
    Output Should Contain  Password must contain letters and numbers

*** Keywords ***
Input New Command And Create User
    Input New Command 
    Create User  kalle  kalle123