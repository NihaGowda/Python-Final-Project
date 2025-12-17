project_title: "Path of the Sort"

team_members:
  - name: "Niha Neelakantappa Gowda"
    email: "ngowda1@stevens.edu"
  - name: "Praveen Elayaraja"
    email: "pelayar@stevens.edu"
  - name: "Mohamed Shafwaan Mohamed Youssuf"
    email: "shxfwaanwork@gmail.com"

problem_description: >
  Sorting algorithms are a fundamental topic in computer science, but many students
  struggle to move beyond memorizing definitions and time complexities. Applying these
  concepts in quizzes and exams requires deeper understanding, which traditional study
  methods often do not fully support.

  Path of the Sort is a terminal-based Python application designed to help users actively
  learn and practice sorting algorithms through interaction. The program combines
  explanation-based learning with quiz-driven assessment to reinforce understanding.

  The project focuses on making learning sorting algorithms more engaging, structured,
  and practice-oriented.

program_structure:
  root_directory: "Path_of_the_Sort"
  files_and_folders:
    - name: "run.py"
      description: "Main entry point used to start the program and display the menu"
    - name: "main.ipynb"
      description: "Jupyter Notebook version of the program (course requirement)"
    - name: "requirements.txt"
      description: "List of required Python libraries"
    - name: "README.md"
      description: "Project documentation"
    - name: "data/"
      description: "Folder containing external data files"
      contents:
        - file: "levels.csv"
          purpose: "Stores difficulty and level configuration"
        - file: "questions.json"
          purpose: "Question bank for quiz mode"
    - name: "src/"
      description: "Main source code directory"
      contents:
        - file: "game.py"
          purpose: "Main game engine and menu handling"
        - file: "learn.py"
          purpose: "Learn Mode explanations and examples"
        - file: "quiz.py"
          purpose: "Challenge Mode quiz logic with scoring and hints"
        - file: "player.py"
          purpose: "Handles player progress and score tracking"
        - file: "metrics.py"
          purpose: "Score calculation and penalties"
        - file: "algorithms.py"
          purpose: "Sorting algorithm implementations"
        - file: "io_utils.py"
          purpose: "Utility functions for loading CSV and JSON data"
    - name: "tests/"
      description: "Unit testing folder"
      contents:
        - file: "test_algorithms.py"
          purpose: "Basic tests for sorting algorithms"

how_to_use_the_program:
  steps:
    - "Ensure Python 3 is installed on the system"
    - "Install required dependencies using: pip install -r requirements.txt"
    - "Run the program using: python run.py"
    - "Follow the on-screen menu to select a mode"

  modes:
    learn_mode:
      description: >
        Learn Mode provides clear explanations of sorting algorithms including how they
        work, time complexity, space complexity, stability, and small examples.
    challenge_mode:
      description: >
        Challenge Mode allows the user to select a difficulty level and answer five
        randomized multiple-choice questions. Hints are available, but using a hint
        reduces the score. The final score is displayed at the end of the quiz.
    exit:
      description: "Exits the program"

team_contributions:
  - member: "Niha Neelakantappa Gowda"
    contributions:
      - "Developed Learn Mode content including algorithm explanations, complexity analysis, stability, and examples"
      - "Assisted with testing and validation of program flow"

  - member: "Praveen Elayaraja"
    contributions:
      - "Contributed to overall program structure and supporting modules"
      - "Assisted with integrating quiz logic and scoring mechanisms"

  - member: "Mohamed Shafwaan Mohamed Youssuf"
    contributions:
      - "Implemented Challenge Mode quiz logic including randomization and hints"
      - "Worked on data handling using CSV and JSON files"
