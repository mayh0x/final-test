Feature: Change the password

    Scenario: Changing password successfully (3a)
        Given a user accesses the profile page (3a)
        When the user clicks "Mudar senha", fills in the fields and submits (3a)
        Then it should see "Perfil atualizado!" (3a)