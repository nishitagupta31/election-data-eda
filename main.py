import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv("indian-state-level-election.csv")  # Make sure file exists!

# Generate report
profile = ProfileReport(df, title="Election Data Analysis")
profile.to_file("election_report.html")  # Save as HTML