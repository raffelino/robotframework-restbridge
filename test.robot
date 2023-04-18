*** Test Cases ***
Sleep Endlessly Test
    Sleep    1
    Log to console    hello, world.
    Sleep    1

    # The above keyword will sleep for 24 hours (86400 seconds).
    # Since there are no further steps, the test will effectively sleep endlessly.
