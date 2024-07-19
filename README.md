# ZQ Accessible Voice Controlled Text Editor

## Introduction
ZQ is a Python-based accessible text editor that allows you to control a document using only voice commands. It leverages the `speech_recognition` module (powered by Google Speech API, OPEN AI Whisper, and TensorFlow) to capture voice input and perform various operations such as saving the file, selecting text, and altering the formatting of the text.

## Features

- **File Operations:** Create, open, save, and save as files.
- **Text Editing:** Cut, copy, paste, select, select all, and delete text.
- **Cursor Navigation:** Move the cursor to the start or end of the text, to a specific line number, or to a specific word.
- **Voice Control:** All commands are accessible through voice input.
- **Interface:** Clean and user-friendly interface with a focus on functionality. High-contrast colors used to allow for color-blind accessibility.

## Usage

Use the GUI to edit your text file or use the following voice commands:

### File Operations
- "ZQ new"
- "ZQ open"
- "ZQ save"
- "ZQ save as"

### Text Editing
- "ZQ cut"
- "ZQ copy"
- "ZQ paste"
- "ZQ select"
- "ZQ select all"
- "ZQ delete"

### Cursor Navigation
- "ZQ go to start"
- "ZQ go to end"
- "ZQ go to line [line number]"
- "ZQ go to word [word]"

## Installation

To install ZQ, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ZQ-TextEditor.git
   ```
2. Navigate to the project directory:
   ```
   cd ZQ-TextEditor
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the ZQ text editor, use the following command:
```
python zq_text_editor.py
```

## Contributing

We welcome contributions to ZQ. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```
   git push origin feature-branch
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

