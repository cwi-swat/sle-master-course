from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from more_itertools import collapse
from input_data_generation import *
from logging_actions import *
from reporting import *
import random   


def start_SUT_and_get_driver(website_url,preparations):
    """
    Starts up the System Under Test (SUT) by starting a Chrome WebDriver instance and
    performing any necessary preparation steps.

    Parameters:
    - website_url (str): The URL of the web application to be tested. This is where the WebDriver will navigate after starting.
    - preparations (list of functions): A list of preparation steps (functions) to be executed once the WebDriver is
      initialized and navigated to the target URL. These steps might include actions like logging in or setting up the
      initial application state. Each function in the list should accept the WebDriver instance as an argument.

    Returns:
    - WebDriver instance (driver) that can be used for further interactions within the SUT.
    """
    
    # Create ChromeOptions instance
    chrome_options = Options()
    
    # Add the desired argument
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    
    # Initialize the WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to the URL of the application to be tested
    driver.get(website_url)
    
    # Execute the necesary preparations (i.e. login, etc.) if any.
    for prepare in preparations:
        prepare(driver)
    
    return driver


def derive_actionable_elements(driver, filter_elements, discovered):
    """
    Derives a list of actionable elements (widgets) from the current state of the web application.
    
    """
     
    # Define the selectors for actionable elements
    selectors = [
        "a",               # Links
        "button",          # Buttons
        "input",           # Input fields (text, checkbox, radio, etc.)
        "select",          # Dropdowns
        "[onclick]",       # Elements with onclick attributes (custom clickable elements)
        "[role='button']"  # Elements with a role attribute as buttons (often used in modern UIs)
    ]

    # Combine all the selectors into a single CSS selector
    all_selectors = ", ".join(selectors)

    # Find all actionable elements
    actionable_elements = driver.find_elements(By.CSS_SELECTOR, all_selectors)
    
    # Compute the list of elements that should be filtered
    filtered_elements = list(collapse([f(driver) for f in filter_elements]))
    
    # Derive only those that are displayed and enabled and should not be filtered
    visible_actionable_elements = [
    element for element in actionable_elements
    if element.is_displayed() and element.is_enabled() and not (element in filtered_elements)
    ]
    
    # Save discovered elements to calculate coverage
    for element in visible_actionable_elements:
        log_discovered(element, discovered)

    return visible_actionable_elements

def derive_actions(driver, filter_elements,visited, discovered):
    """
    Derives all possible actions on a a set of actionable elements
    """
    visible_actionable_elements = derive_actionable_elements(driver, filter_elements, discovered)
    
    actions = []
    
    for element in visible_actionable_elements:
    
        # Basic click
        actions.append(lambda el=element: (log_visited("click", el, visited), el.click()))

        # Advanced clicks
        actions.append(lambda el=element: (log_visited("double-click", el, visited), ActionChains(driver).double_click(el).perform()))
        #actions.append(lambda el=element: (log_visited("right-click", el, visited), ActionChains(driver).context_click(el).perform()))
        actions.append(lambda el=element: (log_visited("click and hold", el, visited), ActionChains(driver).click_and_hold(el).perform()))

        
        # Advanced keyboard inputs applicable to any element
        actions.append(lambda el=element: (log_visited("press TAB", el, visited), el.send_keys(Keys.TAB)))
        actions.append(lambda el=element: (log_visited("press ENTER", el, visited), el.send_keys(Keys.ENTER)))
        actions.append(lambda el=element: (log_visited("press ESCAPE", el, visited), el.send_keys(Keys.ESCAPE)))
        actions.append(lambda el=element: (log_visited("press arrow UP", el, visited), el.send_keys(Keys.ARROW_UP)))
        actions.append(lambda el=element: (log_visited("press arrow DOWN", el, visited), el.send_keys(Keys.ARROW_DOWN)))
    
        element_type = element.get_attribute("type").lower()
        element_tag_name = element.tag_name.lower()
        
        
        if element_tag_name == "input" and element_type in ["text", "number", "email", "password"]:
            # Send some random text, numbers, naughty
            random_text = generate_random_text()
            random_number = generate_random_number()
            naughty_string = generate_naughty_string()

            # keys
            actions.append(lambda el=element: (log_visited("random text keys", el, visited, random_text), el.send_keys(random_text, Keys.RETURN)))
            actions.append(lambda el=element: (log_visited("random number keys", el, visited, random_number), el.send_keys(random_number, Keys.RETURN)))
            actions.append(lambda el=element: (log_visited("random naughty keys", el, visited, naughty_string), el.send_keys(naughty_string, Keys.RETURN)))
            # clear
            actions.append(lambda el=element: (log_visited("clear", el, visited), el.clear()))
            # clear + keys
            actions.append(lambda el=element: (log_visited("clear+text keys", el, visited, random_text), el.clear(), el.send_keys(random_text, Keys.RETURN)))
            actions.append(lambda el=element: (log_visited("clear+ number keys", el, visited, random_number), el.clear(), el.send_keys(random_number, Keys.RETURN)))
            actions.append(lambda el=element: (log_visited("clear+ naughty keys", el, visited, naughty_string), el.clear(), el.send_keys(naughty_string, Keys.RETURN)))
            
        elif element_tag_name == "select":
            # For dropdowns, select different options
            select = Select(element)
            for option in select.options:
                actions.append(lambda el=element, opt=option: (log_visited("select dropdown option", el, visited, opt.text), select.select_by_visible_text(opt.text)))

        elif "[onclick]" in element.get_attribute("outerHTML"):
            # For elements with `onclick` attributes, simply test clicking
            actions.append(lambda el=element: (log_visited("click element with onclick", el, visited), el.click()))

    return actions

 
def select_action(possible_actions):
    """
    Returns a randomly selected element from a list 

    """
    selected_action_id = int(random.randint(0, len(possible_actions)-1))
    return possible_actions[selected_action_id]


def execute_action(action):
    """
    Executes an action on a given WebElement based on its type (e.g., click, input text, select a checkbox).

    """
    action()

    
def check_oracles(driver, oracles, errors, seq, acc):
      
    # Iterate through the oracles and call them
    for oracle in oracles:
        try:
            oracle(driver)
        except AssertionError as e:
            print(f"The oracle {oracle.__name__} detected an error during testing: {str(e)} in sequence {seq} and action {acc}")
            errors.append(f"{oracle.__name__} detected that {str(e)} in sequence {seq} and action {acc}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
   
   
def testar(url, num_runs, length_sequence, filter_elements, preparations, oracles):
    """
    Automated scriptless testing of a web application by executing sequences of actions on the System Under Test (SUT).

    Parameters:
    - url (str): The URL of the web application to be tested.
    - num_runs (int): The number of test runs to be executed. Each run is independent and represents a complete test session.
    - length_sequence (int): The length of the test sequence in each test run. This defines how many actions will be executed in a single run.
    - filter_elements (list of functions): A list of functions that take the driver as input and return an element that should not be considered when deriving act
    - preparations (list of functions): A list of preparation steps to be performed before starting each test run. These could include steps like logging in or setting up the initial state.
    - oracles (list of functions): A list of oracle functions used to check the correctness or expected outcomes after actions are performed. These functions should take the driver as input and perform assertions or checks.
    
    The inner loop of the function automates the TESTAR loop:
    1. Derive all actionable elements in the current state
    2. Select one
    3. Execute the corresponding action
    4. Check the state with the oracles
    """
    errors = []
    visited = set()
    discovered = set()
    
    # Outer loop, that iterates through the number of test runs specified
    for run_cnt in range(1, num_runs+1):
        # Start the SUT and get the driver
        driver = start_SUT_and_get_driver(url, preparations)
        
        print(f"Starting test sequence number {run_cnt} of {num_runs}")
        
        # Inner loop that executes the test sequence with the specified number of actions (length_sequence)
        for acc_cnt in range(1, length_sequence+1):
            #derive the actionable widgets in the current state
            possible_actions = derive_actions(driver, filter_elements, visited, discovered)
            
            #select actionable widgets
            selected_action = select_action(possible_actions)
            
            #execute action
            print(f"Action {acc_cnt} of {length_sequence}")
            execute_action(selected_action)
            
            #check oracles
            check_oracles(driver, oracles, errors, run_cnt, acc_cnt)
                
        # Close the SUT and browser
        driver.quit()
        
    # Print the results
    print_test_summary(url, num_runs, length_sequence, errors, visited, discovered)
    