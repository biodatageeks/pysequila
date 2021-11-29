@setup_tables
Feature: Basic PySeQuiLa pileup tests SQL/API

  Background: some requirement of this test
    Given a sequila session
    And create alignment tables

  Scenario: Count of pileup output with SQL
    Given a sequila session
    And I compute pileup with quals using SQL API
    Then row count is "14671"

  Scenario: Count of pileup output with DataFrame
    Given a sequila session
    And I compute pileup with quals using DataFrame API
    Then row count is "14671"