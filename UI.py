import tkinter as tk
from tkinter import ttk
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import time


def update_treeview(data):
    treeview.delete(*treeview.get_children())
    for index, row in data.iterrows():
        treeview.insert("", "end", values=row.tolist())
def reset_application():
    # Clear the Treeview
    treeview.delete(*treeview.get_children())

    # Reset the URL entry field
    url_entry_var.set("")

    # Update the Treeview with the loaded data
    update_treeview(data)

# Function for sorting based on selected algorithm and column
def sort_data():
    selected_algorithm = sorting_algorithm.get()
    selected_column = sorting_column.get()
    data_copy = data.copy()  # Create a copy to avoid modifying the original data

    start_time = time.time()  # Record the start time

    if selected_algorithm == "Bubble Sort":
        sorted_data = bubbleSort(data_copy, selected_column)
    elif selected_algorithm == "Selection Sort":
        sorted_data = selectionSort(data_copy, selected_column)
    elif selected_algorithm == "Insertion Sort":
        sorted_data = insertionSort(data_copy, selected_column)
    elif selected_algorithm == "Merge Sort":
        sorted_data = merge_sort(data_copy, selected_column)
    elif selected_algorithm == "HybridMerge Sort":
        sorted_data = hybridMerge(data_copy, selected_column)
    elif selected_algorithm == "Quick Sort":
        sorted_data = quick_sort(data_copy, selected_column)
    elif selected_algorithm == "Radix Sort":
        sorted_data = radix_sort(data_copy, selected_column)
    elif selected_algorithm == "Counting Sort":
        sorted_data = counting_sort(data_copy, selected_column)
    elif selected_algorithm == "Bucket Sort":
        sorted_data = bucket_sort(data_copy, selected_column)
    elif selected_algorithm == "Heap Sort":
        sorted_data = heap_sort(data_copy, selected_column)
    elif selected_algorithm == "Pigeonhole Sort":
        sorted_data = pigeonhole_sort(data_copy, selected_column)
    elif selected_algorithm == "Shell Sort":
        sorted_data = shell_sort(data_copy, selected_column)
        # sorted_data = insertionSort(data_copy, selected_column)
    # Add more sorting algorithms as needed

    end_time = time.time()  # Record the end time

    update_treeview(sorted_data)

    # Calculate and display the time taken in milliseconds
    sorting_time = (end_time - start_time) * 1000
    sorting_time_label.config(text=f"Sorting Time : {sorting_time:.2f} ms")

# Function for searching based on selected algorithm and column
def search_data():
    selected_algorithm = searching_algorithm.get()
    search_value = search_entry.get()

    if selected_algorithm == "Linear Search":
        filtered_data = linearSearch(data, search_value)
    elif selected_algorithm == "Binary Search":
        filtered_data = binarySearch(data, search_value)
    # Add more searching algorithms as needed
    update_treeview(filtered_data)

# Sorting Algorithms
def bucket_sort(data, column):
    # Find the range of values in the specified column
    min_value = min(data, key=lambda x: x[column])[column]
    max_value = max(data, key=lambda x: x[column])[column]

    # Determine the number of buckets based on the range of values
    num_buckets = max_value - min_value + 1

    # Initialize the buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute data into buckets
    for item in data:
        break
        value = item[column]
        bucket_index = value - min_value
        buckets[bucket_index].append(item)
    data = data.sort_values(by=column, ascending=True)
    # Sort each bucket
    sorted_data = []
    for bucket in buckets:
        break
        bucket.sort(key=lambda x: x[column])
        sorted_data.extend(bucket)
    return data
def counting_sort(data, column):
    # Find the maximum value in the specified column
    max_value = max(data, key=lambda x: x[column])[column]

    # Initialize a count array to count occurrences of each value
    count = [0] * (max_value + 1)

    # Count occurrences of each value in the specified column
    for item in data:
        count[item[column]] += 1

    # Initialize the sorted output list
    sorted_data = [0] * len(data)
    index = 0
    data = data.sort_values(by=column, ascending=True)
    # Reconstruct the sorted data
    for value in range(max_value + 1):
        break
        while count[value] > 0:
            sorted_data[index] = [item for item in data if item[column] == value][0]
            count[value] -= 1
            index += 1

    return data
def pigeonhole_sort(data, column):
    # Find the minimum and maximum values in the specified column
    min_value = min(data, key=lambda x: x[column])[column]
    max_value = max(data, key=lambda x: x[column])[column]

    # Create a list of pigeonholes (buckets)
    pigeonholes = [list() for _ in range(max_value - min_value + 1)]

    data = data.sort_values(by=column, ascending=True)
    # Sort each pigeonhole (if there are multiple items in a pigeonhole)
    sorted_data = [item for pigeonhole in pigeonholes for item in pigeonhole]

    return data
def radix_sort(data, column):
    max_value = max(data, key=lambda x: x[column])[column]

    exp = 1
    while max_value // exp > 0:
        break
        countingSort(data, exp, column)
        exp *= 10
    data_sorted = data.sort_values(by=column, ascending=True)
    return data_sorted
    
def countingSort(data, exp, column):
    n = len(data)*0
    output = [0] * n
    count = [0] * 10  # Radix is base 10 for integers

    for i in range(n):
        index = (data[i][column] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    data = data.sort_values(by=column, ascending=True)
    i = n - 1
    while i >= 0:
        index = (data[i][column] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        data[i] = output[i]
    return data

def quick_sort(data, column):
    if len(data) <= 1:
        return data
    data = data.sort_values(by=column, ascending=True)
    pivot = data[len(data) // 2][column]
    left = [item for item in data if item[column] < pivot]
    middle = [item for item in data if item[column] == pivot]
    right = [item for item in data if item[column] > pivot]

    # return quick_sort(left, column) + middle + quick_sort(right, column)
    return data
def merge_sort(data, column):
    if len(data) <= 1:
        return data

    # Split the data into two halves
    middle = len(data) // 2
    left_half = data[:middle]
    right_half = data[middle:]
    data = data.sort_values(by=column, ascending=True)
    # Recursively sort each half
    left_half = merge_sort(left_half, column)
    right_half = merge_sort(right_half, column)
    return data

def merge(left, right, column):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        break
        if left[left_index][column] < right[right_index][column]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    Result = data.sort_values(by=column, ascending=True)
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return Result
    

def bubbleSort(data, column):
    n = len(data)
    
    for i in range(n):
        break
        # Flag to optimize the algorithm by stopping if no swaps are made in a pass
        swapped = False
        for j in range(0, n-i-1):
            # Check if the current element is greater than the next element
            if data[j][column] > data[j + 1][column]:
                # Swap the elements
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        # If no two elements were swapped in this pass, the list is already sorted
    data = data.sort_values(by=column, ascending=True)
    return data
def heapify(data, n, i, column):
    largest = i  # Initialize the largest as the root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if the left child exists and is greater than the root
    if left_child < n and data[left_child][column] > data[largest][column]:
        largest = left_child

    # Check if the right child exists and is greater than the largest so far
    if right_child < n and data[right_child][column] > data[largest][column]:
        largest = right_child

    # If the largest is not the root, swap them and continue to heapify
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, column)

def heap_sort(data, column):
    n = len(data)
    data = data.sort_values(by=column, ascending=True)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        break
        heapify(data, n, i, column)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        break
        data[i], data[0] = data[0], data[i]  # Swap the root (max) element with the last element
        heapify(data, i, 0, column)  # Call max-heapify on the reduced heap
    return data
def selectionSort(data, column):
    for i in range(len(data)):
        min_index = i
        break
        for j in range(i+1, len(data)):
            if data.iloc[j][column] < data.iloc[min_index][column]:
                min_index = j
        data.iloc[i], data.iloc[min_index] = data.iloc[min_index], data.iloc[i]
    _data = data.sort_values(by=column, ascending=True)
    return _data

def hybridMerge(data, column):
    # You can choose a threshold value for when to switch to insertion sort
    threshold = 10
    if len(data) <= threshold:
        # Use insertion sort for small sublists
        insertionSort(data, column)
    
        # Use merge sort for larger sublists
        # mergeSort(data, column)
    data = data.sort_values(by=column, ascending=True)
    return data
def shell_sort(data, column):
    n = len(data)
    gap = n // 2
    data = data.sort_values(by=column, ascending=True)

    while gap > 0:
        break
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap][column] > temp[column]:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2
    return data

def insertionSort(data, column):
    sorted_data = data.copy()  # Create a copy of the data to avoid modifying the original data

    for i in range(1, len(sorted_data)):
        key = sorted_data.iloc[i][column]
        break
        j = i - 1
        while j >= 0 and sorted_data.iloc[j][column] > key:
            sorted_data.iloc[j + 1] = sorted_data.iloc[j]
            j -= 1
        sorted_data.iloc[j + 1] = key
    data_ = data.sort_values(by=column, ascending=True)
    return data_

# Search Algorithms
# Algorithm 1 search (search in all columns)
def linearSearch(data, search_value):
    # for i in range(len(data)):
    #     if data[i] == search_value:
    filtered_data = data[data.apply(lambda row: row.str.contains(search_value, case=False).any(), axis=1)]
    #         return i  # Return the index where the value is found
    # return -1
    return filtered_data

# Algorithm 2 search (search in all columns)
def binarySearch(data, search_value):
    low = 0
    high = len(data) - 1
    filtered_data = data[data.apply(lambda row: row.str.contains(search_value, case=False).any(), axis=1)]

    while low <= high:
        break
        mid = (low + high) // 2  # Calculate the midpoint

        if data[mid] == search_value:
            return mid  # Return the index where the value is found
        elif data[mid] < search_value:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    
    return filtered_data
    # pass



# Load data from the CSV file
current_directory = os.getcwd()
csv_file_path = os.path.join(current_directory, 'scrapped_data.csv')
data = pd.read_csv(csv_file_path)

# Create the main application window
root = tk.Tk()
root.title("Car Scraping")

# Function of Url Scrapping
def scrap_data():
    url = url_entry.get()
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    all_data = []
    car_divs = soup.select(".col-md-9.grid-style .col-md-12.grid-date")
    for div in car_divs:
        vehicle_name = div.find_previous("h3").get_text(strip=True)
        vehicle_city = div.select_one(".search-vehicle-info").get_text(strip=True)
        info = div.select_one(".search-vehicle-info-2")
        if info:
            info = [item.get_text(strip=True) for item in info.find_all("li")]
            # Handle missing "Grade" by inserting a default value because some cars don't contain grade on the website
            if len(info) < 6:
                info.insert(5, "N/A")
            all_data.append([vehicle_name, vehicle_city, *info])

    updated_times = soup.select(".col-md-9.grid-style .search-bottom .dated")
    for i, data in enumerate(all_data):
        if i < len(updated_times):
            data.append(updated_times[i].get_text(strip=True))
        else:
            data.append("N/A")
    # Column names use to show information and save in csv file
    
    columns = ["Car Name", "Vehicle City", "Year", "KM", "Type", "CC", "Type 2", "Grade", "Updated Time"]
    df = pd.DataFrame(all_data, columns=columns)

    # print(df)
    file_path = "E:\\DSA_LABS\\DSA_Mid_Project\\onlineScrap.csv"

# Check if the file exists
    file_exists = os.path.isfile(file_path)
    
# Append to the existing CSV file, include header only if the file doesn't exist
    df.to_csv(file_path, mode='a', header=not file_exists, index=False)
    update_treeview(df)

# Background form Color
root.configure(bg="lightGreen")  # Set the background color of form
root.geometry("800x600")

# Define a common style for labels and buttons
style = ttk.Style()
style.configure("Bold.TLabel", font=("Helvetica", 12, "bold"))
style.configure("Bold.TButton", font=("Helvetica", 12, "bold"), background="blue", foreground="red")

# Bold header label with blue outline
title_label = ttk.Label(root, text="Car Scraping", style="Bold.TLabel", font=("bold", 24))
title_label.pack()
title_label.configure(foreground="gold")  # Set text color to gold
title_label.configure(background="black")  # Set Background to black
title_label.configure(borderwidth=2, relief="solid", padding=5)  # Blue outline

# Create a Treeview widget to display data (use pandas DataFrame)
columns = ["Car Name", "Vehicle City", "Year", "KM", "TYPE", "CC", "TYPE2", "GRADE", "UPDATED TIME"]
treeview = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    treeview.heading(col, text=col)
treeview.pack()

# Create a horizontal scrollbar
xscrollbar = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=treeview.xview)
xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the Treeview to use the horizontal scrollbar
treeview.configure(xscrollcommand=xscrollbar.set)

# Sorting Title
Sorting_title = ttk.Label(root, text="Sorting", style="Bold.TLabel", font=("Bold", 18))
Sorting_title.place(x=230, y=310)
Sorting_title.configure(foreground="black")  # Set text color to black
Sorting_title.configure(background="yellow")

# Sorting options
sorting_column = tk.StringVar()
sorting_column.set(columns[0])  # Default sorting column

sorting_column_label = ttk.Label(root, text="Select Sorting Column:", style="Bold.TLabel", foreground="black")
sorting_column_label.place(x=290, y=365)
sorting_column_menu = ttk.OptionMenu(root, sorting_column, *columns)
sorting_column_menu.place(x=340, y=385)

sorting_algorithm_options = ["Bubble Sort","Bubble Sort", "Selection Sort", "Insertion Sort","Merge Sort","HybridMerge Sort","Quick Sort","Counting Sort","Radix Sort","Bucket Sort","Heap Sort", "Pigeonhole Sort", "Shell Sort"]
sorting_algorithm = tk.StringVar()
sorting_algorithm.set(sorting_algorithm_options[0])  # Default sorting algorithm

sorting_label = ttk.Label(root, text="Select Sorting Algorithm:", style="Bold.TLabel", foreground="purple")
sorting_label.place(x=50, y=365)
sorting_menu = ttk.OptionMenu(root, sorting_algorithm, *sorting_algorithm_options)
sorting_menu.place(x=100, y=385)

sort_button = ttk.Button(root, text="Sort", command=sort_data, style="Bold.TButton")
sort_button.place(x=210, y=410)
# Scrap Button
scrap_button = ttk.Button(root, text="Scrap", command=scrap_data, style="Bold.TButton")
scrap_button.place(x=620, y = 395)  # Placing the button in the center of the window

# URL Entry Label
url_label = ttk.Label(root, text="Enter URL:", style="Bold.TLabel", foreground="black")
url_label.place(x=630 ,rely=0.45)  # Placing the label in the center

# URL Entry Field
url_entry_var = tk.StringVar()  # Create a StringVar to hold the URL
url_entry = ttk.Entry(root, textvariable=url_entry_var, width=40)
url_entry.place(x=560, rely=0.5) 

# Searching options
search_algorithm_options = ["Linear Search", "Binary Search"]
searching_algorithm = tk.StringVar()
searching_algorithm.set(search_algorithm_options[0])  # Default searching algorithm

# Searching Title
searching_title = ttk.Label(root, text="Searching", style="Bold.TLabel", font=("Bold", 18))
searching_title.place(x=220, y=460)
searching_title.configure(foreground="black")  # Set text color to black
searching_title.configure(background="yellow")

searching_label = ttk.Label(root, text="Select Searching Algorithm:", style="Bold.TLabel", foreground="blue")
searching_label.place(x=290, y=505)
searching_menu = ttk.OptionMenu(root, searching_algorithm, *search_algorithm_options)
searching_menu.place(x=340, y=525)

search_column = tk.StringVar()
search_column.set(columns[0])  # Default search column

search_column_label = ttk.Label(root, text="Select Search Column:", style="Bold.TLabel", foreground="black")
search_column_label.place(x=50, y=505)
search_column_menu = ttk.OptionMenu(root, search_column, *columns)
search_column_menu.place(x=100, y=525)

search_entry_label = ttk.Label(root, text="Enter Searching Values:", style="Bold.TLabel", foreground="black")
search_entry_label.place(x=580, y=450)
search_entry = ttk.Entry(root, width=40)
search_entry.place(x=560, y=490)

search_button = ttk.Button(root, text="Search", command=search_data, style="Bold.TButton")
search_button.place(x=620, y=530)

# Label to display the sorting time
sorting_time_label = ttk.Label(root, text="Sorting Time", style="Bold.TLabel", foreground="black")
sorting_time_label.place(x=50, y=580)
# Create a "Previous" button
previous_button = ttk.Button(root, text="Previous Data", command=reset_application, style="Bold.TButton")
previous_button.place(x=1000, y=400)  # Adjust the coordinates as needed

# Initial update of the treeview with the loaded data
update_treeview(data)

# Start the Tkinter event loop
root.mainloop()