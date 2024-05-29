# Created by Nandini at 5/28/2024
Feature: Test case AQA_176


  Scenario: 22-User can filter by sale status Newly Launch
    Given Open the Relly main page
    Then Input email nandinisarkar079@gmail.com is entered
    Then Input password field Howrah123$ is entered
    Then Click on Continue button
    Then Verify test+nandini+careerist logged in
    Then Click on Off-plan at the left side menu
    Then Open filter window
    Then Filter by sale status of “Newly Launched”
    Then Verify each product contains the Newly Launched tag