@setup_tables
Feature: Basic PySeQuiLa interval joins tests SQL/API

  Background: some requirement of this test
    Given a sequila session
    And create alignment tables
    And create target table

  Scenario: check explain plan for SQL query
    Given a sequila session
    And I compute interval join using SQL API
    Then explain plan contains "IntervalTreeJoinOptimChromosome"


  Scenario: count interval join output with SQL
    Given a sequila session
    And I compute interval join using SQL API
    Then row count is "1"

  Scenario: check explain plan for DataFrame API
    Given a sequila session
    And I compute interval join using Dataframe API
    Then explain plan contains "IntervalTreeJoinOptimChromosome"

  Scenario: count interval join output with DataFrame
    Given a sequila session
    And I compute interval join using Dataframe API
    Then row count is "1"