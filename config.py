# bias audit tool configuration

DATA_PATH = "predictions.csv"

# which column contains the demographic group
GROUP_COLUMN = "age_group"

# flag groups whose accuracy is more than this below the best group
DISPARITY_THRESHOLD = 0.10  # 10%