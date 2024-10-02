# TBC student scores

<p>A Python project that gets information from given csv file, analyzes it using library Pandas. </p>
<p>Generates excel file and charts using library Matplotlib according to analyzed data.</p>
<p>After analyzing and generating charts and excel file, the following results are displayed to users :</p>

1. **Students who didn't pass exams**
2. **Average scores by semesters**
3. **Students with highest scores**
4. **Worst subject. subject that students had lowest scores in**
4. **Shrinked data of students who have upgraded their scores semester after semester**
4. **Total number of students who have upgraded their scores**


### Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)

#

### Features

- Reads data from given csv file.
- Analyzes data.
- Generates excel file and charts according to analyzed data.
- Displays the result to the users.

#

### Prerequisites

- <img src="readme/assets/python.png" width="25" style="position: relative; top: 8px" /> _Python @3.X and up_

- Libraries:
  - `pandas` (for data analysis and manipulation)
  - `matplotlib` (library for creating static, animated, and interactive visualizations)

- Other packages that comes with python: json


#

### Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/NikaKhiz/student-scores.git
    cd student-scores
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
    or

    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

**Run scripts**:
  - Simply run the `students_scores.py` file:

  ```bash
  python students_scores.py
  ```
  or

  ```bash
  python3 students_scores.py
  ```

### After that program will read the information from given csv file, analyze data, generate the charts and excel file and finally display the results in the terminal!!!


### Project Structure

```bash
├─── readme
│   ├─── assets
- .gitignore
- readme.md
- requirements.txt
- students_scores.py
```