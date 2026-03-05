class LoginLocators:

    EMAIL_INPUT = "//input[@name='email']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//button[normalize-space()='Sign In']"
    CANCEL_BUTTON = "//button[normalize-space()='Cancel']"


#     "#email",                                  # CSS by ID
#     "input#email",                             # CSS full
#     "id=email",                                # Playwright ID selector

#     "//input[@id='email']",                    # XPath by ID
#     "//input[@placeholder='EMAIL']",            # XPath by attribute

#     "[name='email']",                          # CSS by name (if present)
#     "//input[@name='email']",                  # XPath by name

#     ".input_error",                            # CSS by class

#     # Playwright recommended
#     "get_by_placeholder=EMAIL",                 # By placeholder
