import math
# Create Class Object for Courses

class Course:
    
    """
    Represents a course with grade entries and category weightings.

    Attributes:
        course_code (str): The course code (e.g., MHF4U1 for Advanced Function).
        category_weighting (dict): The weighting for each category.
        grade_entries (list): List of grade entries.
        overall (float): The overall grade for the course.
    """

    def __init__(self, course_code: str, category_weighting: dict): # Constructor
        self.course_code = course_code # MHF4U1 -> Advanced Function
        self.category_weighting = category_weighting # [0.35, 0.15, 0.25, 0.25]
        self.grade_entries = [] # [("unit 1 test", "Oct 10", "application", 10.4, 95), (), (), ...]
        self.overall = 0

    # Displays
    def __str__(self):
        """
        Return a string representation of the Course.

        Returns:
            str: A string containing the course code and overall grade.
        """
        return f"Class: {self.course_code} - Overall: {self.overall:.2f}"
    
    def display_entries(self):
        """Display all grade entries in a formatted table."""
        print(f"{'Entry #':^8} {'Title':^30} {'Date':^10} {'Category':^14} "
              f"{'Weight Factor':^15} {'Mark':^12}")
        
        for entry_id, entry in enumerate(self.grade_entries):
            assessment, date, category, weight_factor, grade = entry
            print(f"{entry_id:^8} {assessment.title():^30} {date:^10} "
                  f"{category.title():^14} {weight_factor:^15} {grade:^12}")
            
    # Setters 
    def new_grade_entry(self, package: set):
        """
        Add a new grade entry to the course.

        Args:
            package (tuple): A tuple containing (Title, Date, Category, Weight Factor, Mark).

        Raises:
            ValueError: If the package is incomplete.
        """
        if len(package) != 5: # Invalid length
            raise Exception("The entry package is incomplete!")
        
        self.grade_entries.append(package) 

    def remove_grade_entry(self, entry_id: int):
        """
        Remove a grade entry from the course.

        Args:
            entry_id (int): The index of the entry to remove.

        Raises:
            IndexError: If the entry_id is out of range.
        """
        if entry_id < len(self.grade_entries) and entry_id >= 0:
            del self.grade_entries[entry_id] 
        else:
            raise Exception("Cannot delete entry outside the range!") 
        
    # Grade Calculations
    def weighted_average_calculation(self):
        """
        Calculate the weighted average grade for the course.

        This method updates the overall grade of the course.
        """
        categories = {
            "Thinking": [0, []],
            "Knowledge": [0, []],
            "Communication": [0, []],
            "Application": [0, []]
        }

        categories = {"Thinking": [0, []], "Knowledge": [0, []], "Communication": [0, []], "Application": [0, []]}
        
        # Filter grade entries into their own category
        for entry_id in range(len(self.grade_entries)):
            entry_package = self.grade_entries[entry_id]
            category, weight_factor, grade = entry_package[2:]

            categories[category.title()][0] += weight_factor 
            categories[category.title()][1].append((weight_factor, grade)) 

        # Weighted Calculation
        for category in categories.keys():
            total_weight = categories[category][0] # Sum of all weight factors
            category_result = 0  

            for entry in categories[category][1]:
                weight_factor, grade = entry 
                category_result += (weight_factor / total_weight) * grade 
            
            categories[category] = math.ceil(category_result) # Update array with percentage grade
        
        # Final result
        print(f"Categories: {categories}")
        self.overall = sum(list(categories.values())[category_id] * self.category_weighting[category_id]\
                   for category_id in range(len(categories.values())))


# [thinking, knowledge, communication, application] 
data_management = Course("MDM4U1", [0.25, 0.25, 0.25, 0.25])

# ("unit 1 test", "Oct 10", "application", 10.4, 95)
data_management.new_grade_entry(("Gapminder Investigation", "Sep 6", "Thinking", 12.5, 100))
data_management.new_grade_entry(("Ch5 Vocavulary Assmt", "Sep 10", "Communication", 10.4, 100))
data_management.new_grade_entry(("Ch5 Test Stat Graphs", "Sep 13", "Knowledge", 10.4, 95))
data_management.new_grade_entry(("Ch5 Test Short Answer", "Sep 13", "Application", 12.5, 93))
data_management.new_grade_entry(("1-Var Stats Quiz", "Sep 26", "Knowledge", 4.2, 89))
data_management.new_grade_entry(("1-Var Stats Quiz", "Sep 26", "Communication", 4.2, 82))
data_management.new_grade_entry(("1-Var Unit Test m.c.", "Oct 3", "Knowledge", 10.4, 87))
data_management.new_grade_entry(("1-Var Unit Test", "Oct 3", "Application", 12.5, 96))
data_management.new_grade_entry(("1-Var Unit Test", "Oct 3", "Thinking", 12.5, 100))
data_management.new_grade_entry(("1-Var Unit Test", "Oct 3", "Communication", 10.4, 92))
data_management.weighted_average_calculation() 
print(data_management.__str__())
print(data_management.display_entries())
