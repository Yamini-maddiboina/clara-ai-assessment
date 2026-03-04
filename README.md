# Clara AI Assessment

This project processes transcript dataset files using a simple Python pipeline.  
The system extracts information from the dataset, generates structured results, and stores them in the output folder.

---

## Project Architecture

The system works using three main scripts:

- extract.py → Reads transcript files from the dataset folder
- generate.py → Processes the extracted data
- update.py → Updates and saves the final results

Pipeline flow:

Dataset → Extract → Generate → Update → Output

---

## Project Structure

project-folder/

dataset/ → contains transcript files (.txt)  
scripts/ → contains python processing scripts  
output/ → contains generated results  

scripts/
- extract.py
- generate.py
- update.py

---

## How to Run Locally

Step 1: Open the project in VS Code.

Step 2: Open terminal.

Step 3: Navigate to scripts folder

cd scripts

Step 4: Run the scripts

python extract.py  
python generate.py  
python update.py

---

## Adding Dataset Files

Place transcript files inside the dataset folder.

Example:

dataset/
demo_call_1.txt  
onboarding_call_1.txt  

The scripts will automatically read these files.

---

## Output Files

After running the scripts, results will be stored inside the output folder.

Example:

output/
v1.json  
v2.json  

---

## Known Limitations

- Only supports text transcript files (.txt)
- Scripts must be run manually in order
- Basic error handling

---

## Future Improvements

If this system is deployed in production:

- Automate the pipeline
- Add error logging
- Build API integration
- Support larger datasets
- Deploy using cloud infrastructure

---

## Author

Yamini Maddiboina.
B.Tech CSE-AIML
