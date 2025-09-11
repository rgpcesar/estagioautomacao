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


## Selenium Grid

Selenium Grid is a component of the Selenium suite that specializes in running multiple tests across different browsers, operating systems, and machines in parallel. This capability significantly speeds up test execution and expands test coverage.

### Core Concepts

*   **Hub:** The Hub is the central point in the Selenium Grid that receives test requests and distributes them to the appropriate Nodes. It acts as a manager, keeping track of which nodes are available and what their capabilities are (e.g., which browser, which platform). There is only one Hub in a Grid.

*   **Node:** Nodes are the machines (physical or virtual) that execute the tests. Each Node is registered with the Hub and advertises its capabilities. A Grid can have multiple Nodes, and each Node can have multiple browser instances. For example, a single Node could run instances of Chrome, Firefox, and Edge.


### Running the Grid with Docker Compose

The easiest way to run the Selenium Grid is by using the provided `docker-compose.yml` file. This file defines the Hub and a Node for each browser (Chrome, Firefox, and Edge).

**Prerequisites:**

*   Docker and Docker Compose must be installed on your system.

**Instructions:**

1.  **Start the Grid:**
    Open a terminal in the root of the project and run the following command:
    ```bash
    docker-compose up -d
    ```
    This will download the necessary images and start the Hub and Node containers in the background.

2.  **Verify Node Registration:**
    Open your web browser and navigate to the Selenium Grid console:
    [http://localhost:4444](http://localhost:4444)

    You should see the Grid dashboard with the Chrome, Firefox, and Edge nodes registered and available.

3.  **Stop the Grid:**
    When you are finished, you can stop the Grid with the following command:
    ```bash
    docker-compose down
    ```


### Parallel Test Execution with `pytest-xdist`

To speed up the test suite execution, this project uses `pytest-xdist` to run tests in parallel.

**Installation:**

```bash
pip install pytest-xdist
```

**Usage:**

To run tests in parallel, use the `-n` flag to specify the number of parallel workers. For example, to run the `test_text_box.py` test in three parallel instances across the Selenium Grid:

```bash
pytest tests/test_text_box.py --remote -n 3
```


### A Note on Docker Image Tags

The `docker-compose.yml` file has been updated to use the `latest` tag for all Selenium images. While this is convenient for getting started, for production environments, it is best practice to pin to a specific, stable version tag to ensure repeatable builds.


### Troubleshooting: Frozen Terminal

If you run `pytest --remote` and the terminal appears to freeze, it is likely a network communication issue between your test runner (on `localhost`) and the Selenium Hub container. The `docker-compose.yml` has been updated to include `SE_HUB_HOST=localhost` for the Hub service, which should resolve this.

**To ensure a clean start:**

1.  Bring down any existing Grid containers:
    ```bash
    docker-compose down
    ```
2.  Start the Grid again with the updated configuration:
    ```bash
    docker-compose up -d --force-recreate
    ```
3.  Run your tests.


### Running Cross-Browser Parallel Tests

The test framework is now configured to run tests across multiple browsers in parallel.

**Usage:**

To run the tests on specific browsers, use the `--browsers` flag, followed by the browser names. To run in parallel, use the `-n` flag with the number of workers (which should typically match the number of browsers).

```bash
# Run tests on Chrome and Firefox in parallel on the Grid
pytest -n 2 --remote --browsers chrome firefox tests/test_tool_tips.py
```
