@setup_tables
Feature: Basic PySeQuiLa coverage tests SQL/API

  Background: some requirement of this test
    Given a sequila session
    And create alignment tables

  Scenario: Count of coverage output
    Given a sequila session
      And I compute coverage
    Then row count is "12836"
