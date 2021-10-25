Feature: HelpDesk

    Scenario: Successfully opening a case (2a)
        Given an achiever accesses the helpdesk (2a)
        When the achiever submits a case with the required fields filled in (2a)
        Then the case stays in progress (2a)