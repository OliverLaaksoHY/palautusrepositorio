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
