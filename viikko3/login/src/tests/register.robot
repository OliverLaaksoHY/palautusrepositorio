*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
# ...
    Set Username  sami
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password And Password Confirmation
    Set Username  sami
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Nonmatching Password And Password Confirmation
    Set Username  sami
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

Register With Too Short Username And Valid Password
    Set username  k
    Set password  kalle123
    Set password Confirmation  kalle123
    Click  button >> text=Register
    Register should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set username  sami
    Set password  s
    Set password Confirmation  s
    Click  button >> text=Register
    Register Should Fail With Message  Password too short

Register With Password Containing Letters And Numbers
    Set Username  sami
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Character
    Set Username  sami
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Consisting Only Of Letters
    Set Username  sami
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password cannot consist only of letters

Register With Password Consisting Only Of Uppercase Letters
    Set Username  sami
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password cannot consist only of letters


Register With Username That Is Already In Use
    Set username  kalle
    Set password  kalle123
    Set password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  Register\nUser with username kalle already exists\nUsername \nPassword \nPassword confirmation \nRegister\nLogin



*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
