# Estagio CESAR

This project contains web automation tests for the DemoQA website.

## Scenarios

### Practice Form

This test fills out the Practice Form with data and submits it.

**Manual Steps:**

1.  Navigate to `https://demoqa.com/automation-practice-form`.
2.  Enter the First Name.
3.  Enter the Last Name.
4.  Enter the Email.
5.  Select a Gender.
6.  Enter the Mobile number.
7.  Select the Date of Birth.
8.  Enter Subjects.
9.  Select Hobbies.
10. Upload a picture (optional).
11. Enter the Current Address.
12. Select the State.
13. Select the City.
14. Click the Submit button.
15. Verify the confirmation modal appears with the correct information.

## Features

### Parameterization with `@pytest.mark.parametrize`

The Practice Form test utilizes `@pytest.mark.parametrize` to run the same test logic with multiple datasets.

**Advantages:**

*   **Data-Driven Testing:** Separates test data from test logic, making it easier to add new test cases without modifying the test code.
*   **Reusability:** A single test can be used to validate multiple scenarios.
*   **Readability:** Keeps the test code clean and focused on the test flow.
*   **Maintainability:** Test data is managed in a separate file ([`data/practice_form_data.json`](data/practice_form_data.json)), making it easy to update.



### Allure Reports

This project is integrated with Allure to generate detailed test reports.

**Installation:**

1.  Install the `allure-pytest` package:

    ```bash
    pip install allure-pytest
    ```

2.  Install the Allure command-line tool. You can find the installation instructions for your operating system in the [official Allure documentation](https://docs.qameta.io/allure/#_installing_a_commandline).

**Usage:**

1.  Run `pytest` with the `--alluredir` flag:

    ```bash
    pytest --alluredir=allure-results
    ```

2.  Serve the Allure report:

    ```bash
    allure serve allure-results
    ```


### Execution Dashboard

A simple dashboard can be generated to display the results of the test execution.

**Usage:**

Run the `dashboard.py` script to generate the `dashboard.html` file:

```bash
python dashboard.py
```

### Code Coverage with `pytest-cov`

This project uses `pytest-cov` to measure the effectiveness of the tests by analyzing which parts of the source code are executed during the test run.

**Advantages:**

*   **Identify Untested Code:** Pinpoints areas of the application that lack test coverage.
*   **Improve Test Quality:** Encourages the creation of more comprehensive tests.
*   **Maintain Standards:** Can be configured to fail the build if coverage drops below a certain threshold, ensuring a consistent level of quality.

**Installation:**

To use this feature, you need to install the `pytest-cov` package:

```bash
pip install pytest-cov
```

**Usage:**

The coverage report is automatically generated in an `htmlcov` directory when you run `pytest`. The build will fail if the coverage for the `pages` directory is below 80%.
