import os
import random
import shutil

# Function to move files from source to destination directory
def move_files(source_dir, destination_dir, file_list):
    for file in file_list:
        src = os.path.join(source_dir, file)
        dst = os.path.join(destination_dir, file)
        shutil.copy(src, dst)

# Directory containing labeled data
labeled_data_dir = "dataset/FER2013/train"

# Directory to store labeled data for different scenarios
labeled_scenarios_dir = "dataset/FER2013/labeled_scenarios"

# Directory to store unlabeled data
unlabeled_data_dir = "dataset/FER2013/unlabeled"

# List of emotions
emotions = os.listdir(labeled_data_dir)

# Number of labeled samples for each scenario
num_labeled_samples = [10, 25, 100, 250]
# Initialize a set to store all labeled files
all_labeled_files = set()

# Iterate over each scenario
for num_samples in num_labeled_samples:
    # Create a directory for the current scenario
    scenario_dir = os.path.join(labeled_scenarios_dir, f"{num_samples}_labeled")
    os.makedirs(scenario_dir, exist_ok=True)
    
    # Iterate over each emotion
    for emotion in emotions:
        # Get the path to the emotion directory
        emotion_dir = os.path.join(labeled_data_dir, emotion)
        # Check if the directory exists and is a directory
        if os.path.isdir(emotion_dir) and not emotion == '.ipynb_checkpoints':
            # List all image files for the current emotion, excluding .DS_Store
            image_files = [f for f in os.listdir(emotion_dir) if not f.startswith('.')]
            # Randomly select num_samples for labeling
            labeled_files = random.sample(image_files, num_samples)
            # Move the labeled files to the labeled directory
            move_files(emotion_dir, scenario_dir, labeled_files)
            # Add the labeled files to the set of all labeled files
            all_labeled_files.update(labeled_files)
        else:
            print(f"Directory '{emotion_dir}' does not exist or is not a directory.")

# Create the unlabeled directory if it doesn't exist
os.makedirs(unlabeled_data_dir, exist_ok=True) 

# Move the remaining files to the unlabeled directory
for emotion in emotions:
    emotion_dir = os.path.join(labeled_data_dir, emotion)
    if not emotion == '.ipynb_checkpoints' and os.path.isdir(emotion_dir) :
        # List all files (excluding directories) for the current emotion
        remaining_files = [f for f in os.listdir(emotion_dir) if os.path.isfile(os.path.join(emotion_dir, f)) and not f.startswith('.')]
        move_files(emotion_dir, unlabeled_data_dir, remaining_files)
    else:
        print(f"Directory '{emotion_dir}' does not exist or is not a directory.")
s