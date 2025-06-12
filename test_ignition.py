# Script Name: read_waste_dataset_with_format
# Main Function: Reads and formats the dataset from a tag in Ignition.
# Date of Writing: October 15, 2024

def function_01_read_dataset():
    # Import necessary Ignition library
    from com.inductiveautomation.ignition.common import BasicDataset
    import system

    # Path to the dataset tag
    tag_path = '[default]01_ci_trackers/01_mallow_waste/dataset_waste'

    try:
        # Reading the dataset tag value
        tag_value = system.tag.readBlocking([tag_path])[0].value
        
        # Checking if the tag value is a dataset
        if isinstance(tag_value, BasicDataset):
            dataset = tag_value
            # Iterate over each row in the dataset
            for row in range(dataset.getRowCount()):
                tag_name = dataset.getValueAt(row, "Tag")
                value = dataset.getValueAt(row, "Value")
                # Print in "Tag: Value" format using .format()
                print("{}: {}".format(tag_name, value))
        else:
            print("The tag value is not a dataset.")
    
    except Exception as e:
        print("Error reading dataset: ", str(e))

# Call the function to execute
function_01_read_dataset()