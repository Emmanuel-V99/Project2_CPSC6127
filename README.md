# Project2_CPSC6127
# Emmanuel Vanderson
# April 24, 2025

Goal is to conduct a large-scale data analysis using Hadoop MapReduce, focusing on distributed data processing.

INSTRUCTIONS
-To install Hadoop and Java on your Windows machine, and configure your environmental variables as needed:
    Carefully follow the instructions given from this link: https://github.com/ruslanmv/How-to-install-Hadoop-on-Windows/tree/master?tab=readme-ov-file within the README.md file
-If this proves to be unsuccessful for you, please utilize the following YouTube links to assist you in Hadoop environment setup
    -How to Install Hadoop on Windows: Step-by-Step Guide | SPPU DSBDA LAB ( https://www.youtube.com/watch?v=Dp2-dAftD1Q )
    -Hadoop HDFS Commands and MapReduce with Example: Step-by-Step Guide | Hadoop Tutorial | IvyProSchool ( https://www.youtube.com/watch?v=7O56u3LyPTY )
-Due to file size restrictions, user must download the enron email data set from the provided link, and place it within the empty /data folder --> https://www.kaggle.com/datasets/wcukierski/enron-email-dataset

-In order to preprocess the data from the Enron emails (because the file is much too large, and is more preferrable in a .txt file anyway), we need to run the command:
    -python scripts\preprocess_enron.py
-It is imperative that you run the following lines in Command Prompt as an Administrator in order to format the namenode and start Hadoop:
    start-dfs.cmd
    start-yarn.cmd  
-Check if Local Host is up by opening a web browser and inputting "localhost:9870".
    -(Should display a site with a green nav bar at the top)
-(Check if NameNode and DataNode are working by inputting the 'dfs' command)
-Please use HDFS for Input/Output:
If your goal is to process files using Hadoop’s distributed architecture, first place the files in HDFS, then reference them.

1. Upload your data file to HDFS
Run these command in Command Prompt:

First, make a directory in HDFS
hdfs dfs -mkdir /emmanuel

Then, upload your data file that you will be running MapReduce on to HDFS
hdfs dfs -put "C:/Users/the6t/OneDrive/Desktop/Spring Semester 2025/CPSC 6127 Contemporary Issues in Database Management Systems/Project 2/Project2_CPSC6127/data/cleaned_emails.txt" /emmanuel/

2. Update your Hadoop streaming command
Now, reference the HDFS paths instead of local Windows paths:

hadoop jar "C:/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar" -input "/emmanuel/cleaned_emails.txt" -output "/emmanuel/output" -mapper "python C:/hadoop_scripts/mapper.py" -reducer "python C:/hadoop_scripts/reducer.py"

IF YOU ARE RE-RUNNING THE ABOVE COMMAND AGAIN, DELETE THE OUTPUT FOLDER FIRST: hdfs dfs -rm -r /emmanuel/output

TO RUN THE HADOOP MAPREDUCE PROGRAM WITH COMBINER
hadoop jar "C:/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar" -input "/emmanuel/cleaned_emails.txt" -output "/emmanuel/output" -mapper "python C:/hadoop_scripts/mapper.py" -reducer "python C:/hadoop_scripts/reducer.py" -combiner "C:/hadoop_scripts/combiner.py"

-Place the calculated "part-00000" file found on localhost:9870 within the output folder in order to run top_15_words.py
