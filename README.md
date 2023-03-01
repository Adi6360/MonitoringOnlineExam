# Monitoring Online Exam

As remote exams become more common in the education industry, proctoring has become an essential aspect of the evaluation process. Traditionally, proctoring requires students to visit an examination center or be monitored through a video camera. However, with the development of digital technology, we propose a solution architecture that enables students to take online exams without the need for physical presence or constant proctor intervention.

Our proposed system includes five components that work together to detect cheating in online exams: user authentication, head movement detection, eye gaze detection, motion detection, and report generation. The system requires only one inexpensive webcam as a hardware requirement. We use semantic features to classify whether a candidate is cheating during the examination by aggregating the results of each component.

# Features
- User authentication to ensure the identity of the exam candidate
- Head movement detection to identify when the exam candidate is looking away from the screen
- Eye gaze detection to monitor where the attendee is looking on the screen
- Motion detection to identify if the exam taker leaves their seat during the exam
- Report generation to provide evidence of cheating to instructors

# Getting Started
To use our remote exam proctoring system, you can follow these steps:

1. Clone the project from GitHub
2. Install the required dependencies (list any dependencies and versions)
3. Configure the system according to your needs (database settings, exam settings, etc.)
4. Run the application ```python ExamProctoringInitializer.py```

# Usage

Once the system is up and running, exam administrators can initiate exams, as monitoring will be carried out in the background. Students or candidates can then log in to the system using their credentials and start taking the exam. The system will use the five components to monitor the exam taker and detect any cheating behavior.

# Contributing

We welcome contributions from developers who want to improve our remote exam proctoring system! To contribute, you can follow these steps:

1. Fork the project from GitHub
2. Create a new branch for your changes
3. Make your changes and submit a pull request
4. Wait for a review and approval from the project maintainers