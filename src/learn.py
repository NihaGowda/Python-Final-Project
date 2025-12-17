import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


LEARN_CONTENT = {
    "Insertion Sort": {
        "overview": """
Insertion Sort builds the final sorted array one element at a time.
It works the way you sort playing cards in your hand.
""",
        "how": """
How it works:
1. Start from the second element.
2. Compare it with elements before it.
3. Shift larger elements to the right.
4. Insert the element at its correct position.
""",
        "example": """
Example:
Array: [5, 3, 4, 1]

Step 1: Insert 3 → [3, 5, 4, 1]
Step 2: Insert 4 → [3, 4, 5, 1]
Step 3: Insert 1 → [1, 3, 4, 5]
""",
        "complexity": """
Time Complexity:
Best Case: O(n)  (already sorted)
Average:   O(n²)
Worst:     O(n²)

Space Complexity: O(1)
Stable: Yes
""",
        "when": """
When to use:
✔ Small datasets
✔ Nearly sorted data
✘ Large random datasets
"""
    },

    "Merge Sort": {
        "overview": """
Merge Sort is a divide-and-conquer algorithm.
It divides the array into halves, sorts them, and merges them.
""",
        "how": """
How it works:
1. Divide array into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.
""",
        "example": """
Example:
Array: [8, 3, 5, 2]

Split → [8, 3] & [5, 2]
Sort  → [3, 8] & [2, 5]
Merge → [2, 3, 5, 8]
""",
        "complexity": """
Time Complexity:
Best / Average / Worst: O(n log n)

Space Complexity: O(n)
Stable: Yes
""",
        "when": """
When to use:
✔ Large datasets
✔ Linked lists
✔ Guaranteed performance needed
✘ Memory-constrained systems
"""
    },

    "Quick Sort": {
        "overview": """
Quick Sort is a divide-and-conquer algorithm that uses a pivot.
It is very fast in practice.
""",
        "how": """
How it works:
1. Choose a pivot element.
2. Partition array into smaller and larger elements.
3. Recursively sort partitions.
""",
        "example": """
Example:
Array: [6, 3, 9, 2]

Pivot: 6
Left: [3, 2]
Right: [9]

Result: [2, 3, 6, 9]
""",
        "complexity": """
Time Complexity:
Best / Average: O(n log n)
Worst:          O(n²)

Space Complexity: O(log n)
Stable: No
""",
        "when": """
When to use:
✔ Fast real-world performance
✔ Large arrays
✘ Worst-case sensitive input
"""
    }
}


def show_topic(topic: str):
    clear()
    data = LEARN_CONTENT[topic]

    print(f"===== {topic} =====\n")
    print("OVERVIEW")
    print(data["overview"])

    print("\nHOW IT WORKS")
    print(data["how"])

    print("\nEXAMPLE")
    print(data["example"])

    print("\nCOMPLEXITY")
    print(data["complexity"])

    print("\nWHEN TO USE")
    print(data["when"])

    input("\nPress Enter to go back...")


def run_learn_mode():
    while True:
        clear()
        print("====== LEARN MODE ======\n")
        print("1. Insertion Sort")
        print("2. Merge Sort")
        print("3. Quick Sort")
        print("0. Back to Main Menu")

        choice = input("\nChoose a topic: ")

        if choice == "0":
            return
        elif choice == "1":
            show_topic("Insertion Sort")
        elif choice == "2":
            show_topic("Merge Sort")
        elif choice == "3":
            show_topic("Quick Sort")
