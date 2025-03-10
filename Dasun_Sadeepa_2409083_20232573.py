import random
import json

# Sample projects with the given structure
projects = [
    {
        "Project ID": "001",
        "Project Name": "MathGenius",
        "Category": "Maths",
        "Team Members": ["Alex Johnson", "Emma Smith", "Charlie Davis"],
        "Brief Description": "Developing an advanced math problem solver algorithm.",
        "Country": "United States"
    },
    {
        "Project ID": "002",
        "Project Name": "QuantumExplorers",
        "Category": "Science",
        "Team Members": ["Olivia White", "Daniel Brown", "Sophie Green"],
        "Brief Description": "Exploring the applications of quantum computing in scientific research.",
        "Country": "Canada"
    },
    {
        "Project ID": "003",
        "Project Name": "AI-Assist",
        "Category": "AI",
        "Team Members": ["Michael Taylor", "Sophia Lee", "Ethan Wang"],
        "Brief Description": "Creating an AI-powered personal assistant with advanced learning capabilities.",
        "Country": "Australia"
    },
    {
        "Project ID": "004",
        "Project Name": "SecureNet",
        "Category": "Cybersecurity",
        "Team Members": ["Ava Robinson", "Liam Brown", "Mia Johnson"],
        "Brief Description": "Developing a secure networking solution to prevent cyber attacks.",
        "Country": "Germany"
    },
    {
        "Project ID": "005",
        "Project Name": "MathWhiz",
        "Category": "Maths",
        "Team Members": ["Jack Miller", "Sophie Taylor", "Lucas Chen"],
        "Brief Description": "Creating an interactive platform for mastering mathematical concepts.",
        "Country": "United Kingdom"
    },
    {
        "Project ID": "006",
        "Project Name": "BioTechExploration",
        "Category": "Science",
        "Team Members": ["Emily Davis", "William Green", "Natalie White"],
        "Brief Description": "Exploring advancements in biotechnology for sustainable solutions.",
        "Country": "France"
    },
    {
        "Project ID": "007",
        "Project Name": "AI-MedicalDiagnosis",
        "Category": "AI",
        "Team Members": ["Oliver Taylor", "Zoe Johnson", "Sophie Brown"],
        "Brief Description": "Developing an AI system for medical diagnosis and prognosis.",
        "Country": "Japan"
    },
    {
        "Project ID": "008",
        "Project Name": "CyberShield",
        "Category": "Cybersecurity",
        "Team Members": ["Nathan Miller", "Isabella White", "Jackson Davis"],
        "Brief Description": "Building an advanced cybersecurity solution to safeguard digital assets.",
        "Country": "South Korea"
    },
    {
        "Project ID": "009",
        "Project Name": "MathPuzzleSolver",
        "Category": "Maths",
        "Team Members": ["Lily Brown", "Thomas Johnson", "Emma White"],
        "Brief Description": "Creating a fun and educational math puzzle solver for all ages.",
        "Country": "Brazil"
    },
    {
        "Project ID": "010",
        "Project Name": "SpaceExploration",
        "Category": "Science",
        "Team Members": ["Aiden Taylor", "Grace Robinson", "Leo Miller"],
        "Brief Description": "Exploring outer space and studying celestial bodies for scientific research.",
        "Country": "United States"
    },
    {
        "Project ID": "011",
        "Project Name": "AI-Chatbot",
        "Category": "AI",
        "Team Members": ["Sophie Chen", "Daniel Green", "Ella Davis"],
        "Brief Description": "Developing an intelligent chatbot with natural language processing capabilities.",
        "Country": "Germany"
    },
    {
        "Project ID": "012",
        "Project Name": "SecureTransactions",
        "Category": "Cybersecurity",
        "Team Members": ["Mia Taylor", "Lucas Brown", "Ava Johnson"],
        "Brief Description": "Implementing secure protocols for online financial transactions.",
        "Country": "Australia"
    }
]


def load_projects():
    global projects
    try:
        with open('projects.json', 'r') as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []


save_needed = False


# Function to ask from the user whether the random selection for the spotlight showcase is done
def ask_random_selection_done():
    answer = input("Is the random selection for the spotlight showcase done? (yes/no): ").lower()
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return ask_random_selection_done()


is_random_selection_done = ask_random_selection_done()


# Function to add project details
def add_project(projects):
    save_needed = True  # Initialize save_needed locally

    while True:
        try:
            project_id = int(input("Enter Project ID(Start with 0): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for Project ID.")
    project_name = input("Enter Project Name: ")

    while True:
        category = input("Enter Category(AI/MATH/SCIENCE/CYBER SECURITY): ").upper()
        if category in ["AI", "MATH", "SCIENCE", "CYBER SECURITY"]:
            break
        else:
            print("Invalid category. Please enter a valid category.")
    team_members = input("Enter Team Members (comma-separated): ").split(',')
    description = input("Enter Brief Description: ")
    country = input("Enter Country: ")

    projects.append({
        "Project ID": project_id,
        "Project Name": project_name,
        "Category": category,
        "Team Members": team_members,
        "Brief Description": description,
        "Country": country,
        "Selected for Showcase": False,
        "Awards": []
    })
    print("Project details added successfully!")
    save_changes(projects, save_needed)


# Function to delete project details
def delete_project(projects):
    if not projects:
        print("No projects to delete.")
        return
    while True:
        try:
            project_id = input("Enter Project ID to delete: ")
            if any(project["Project ID"] == project_id for project in projects):
                projects = [project for project in projects if project["Project ID"] != project_id]
                print("Project deleted successfully!")
                save_changes(projects, True)  # Prompt the user to save changes
                break
            else:
                print("Project ID not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Project ID.")


# Function to update project details
def update_project(projects):
    project_id = input("Enter Project ID to update: ")
    for project in projects:
        if project["Project ID"] == project_id:
            project["Project Name"] = input("Enter updated Project Name: ")
            project["Category"] = input("Enter updated Category: ")
            project["Team Members"] = input("Enter updated Team Members (comma-separated): ").split(',')
            project["Brief Description"] = input("Enter updated Brief Description: ")
            project["Country"] = input("Enter updated Country: ")
            print("Project details updated successfully!")
            save_changes(projects, True)
            return
    print("Project ID not found.")
    update_project(projects)


# Function to ask whether the user wants to save details after adding, deleting, and updating the details
def save_changes(projects, save_needed):
    if save_needed:
        answer = input("Do you want to save the changes to the file? (yes/no) ").lower()
        if answer == "yes":
            save_to_file(projects)
            print("Details Saved Successfully")
        elif answer != "no":
            print("Invalid input. Please answer with 'yes' or 'no'.")


# Function to arrange the order which we need to save the details
def categorize_projects(projects):
    categorized_projects = {}
    for project in projects:
        category = project["Category"]
        if category not in categorized_projects:
            categorized_projects[category] = []
        categorized_projects[category].append(project)
    return categorized_projects


# Function to save project details to a file
def save_to_file(projects):
    categorized_projects = categorize_projects(projects)
    with open("project_details.txt", "w") as file:
        for category, projects_in_category in categorized_projects.items():
            file.write(f"{category}:\n")
            for project in projects_in_category:
                file.write(json.dumps(project) + "\n")
            file.write("\n")


# Function to View project details
def get_project_id(project):
    return project["Project ID"]


# Function to arrange the details in the order
def view_projects(projects):
    sorted_projects = sorted(projects, key=get_project_id)
    for project in sorted_projects:
        for key, value in project.items():
            print(f"{key}: {value}")
        print("-----------------------------")


# Function to calculate total points of a project
def get_total_points(project):
    return project["Total Points"]


# Function to print stars based on total points
def print_stars(total_points):
    stars = "★" * total_points
    return stars


# visualizing the winning projects
def simulate_random_selection(projects):
    winning_projects = {}  # Dictionary to store winning projects with points
    categories_selected = set()

    for project in projects:
        category = project["Category"]
        if category not in categories_selected:
            # Filter projects by category
            category_projects = [proj for proj in projects if proj["Category"] == category]
            # Shuffle the projects within the category
            random.shuffle(category_projects)
            # Select the first project after shuffling
            selected_project = category_projects[0]

            print(f"\nProject: {selected_project['Project Name']} (Category: {category})")
            points = []
            for judge in range(4):
                while True:
                    try:
                        judge_points = int(input(f"Enter points from Judge {judge + 1} (out of 5): "))
                        if judge_points < 1 or judge_points > 5:
                            raise ValueError("Points must be between 1 and 5.")
                        break
                    except ValueError as e:
                        print(e)
                points.append(judge_points)
            selected_project["Points"] = points
            selected_project["Total Points"] = sum(points)
            # Add the selected project to the list of winning projects
            winning_projects[category] = selected_project
            categories_selected.add(category)
    return winning_projects


def visualization(winning_projects):
    print("\nVisualizing The Award-Winning Projects:")

    max_points = max(project['Total Points'] for project in winning_projects.values())

    printable_lines = {}
    max_display_length = 0

    # Sort projects by rank
    sorted_projects = sorted(winning_projects.values(), key=get_total_points, reverse=True)

    # Iterate over the first three projects
    idx = 0
    for project in sorted_projects[:3]:
        remaining_stars = project['Total Points']
        rank_text = f"{idx + 1}{'st' if idx == 0 else 'nd' if idx == 1 else 'rd'} place"
        name_text = f"name: {project['Project Name']}"
        country_text = f"country: {project['Country']}"
        display_texts = [country_text, name_text, rank_text]

        # Update max display length
        for text in display_texts:
            text_length = len(str(text))
            if text_length > max_display_length:
                max_display_length = text_length

        # Populate printable_lines
        for i in range(max_points + 3, max_points, -1):
            line_id = i
            if line_id not in printable_lines:
                printable_lines[line_id] = []
            # Append strings
            if line_id == max_points + 3:
                context = display_texts[0]
            elif line_id == max_points + 2:
                context = display_texts[1]
            elif line_id == max_points + 1:
                context = display_texts[2]

            printable_lines[line_id].append(context)

            # Append stars
            for j in range(max_points, 0, -1):
                star_line_id = j
                if star_line_id not in printable_lines:
                    printable_lines[star_line_id] = []
                if remaining_stars != 0:
                    printable_lines[star_line_id].append("★")
                    remaining_stars -= 1

        idx += 1

    # Print the visualization
    for i in range(1, len(printable_lines.keys()) + 1):
        text = f"{printable_lines[i]}"
        text = text.replace("[", "").replace("]", "").replace("'", "").replace("'", "")
        elements = text.split(',')
        lengths = [len(element.strip()) for element in elements]
        for length in lengths:
            space = max_display_length - length
            text = text.replace(",", " " * space)

        print(text)


# Function to print the menu
def print_menu():
    print("\nTechExpo Management System Menu:")
    print("1. Adding Project Details (APD)")
    print("2. Updating Project Details (UPD)")
    print("3. Deleting Project Details (DPD)")
    print("4. Viewing Project Details (VPD)")
    print("5. Random Spotlight Selection (RSS)")
    print("6. Exiting the Program (EXIT)")
    print("If you prefer to visualize the details please run the option 5 first")


# Main Program
while True:
    if is_random_selection_done:
        print("Sorry The Random Selections Are Already Done.")
        asking = input("Do you need to Enter the Judge's Point and Display the Winners (Yes/No)").lower()
        if asking == "yes":
            simulate_random_selection(projects)
            exit()
        elif asking == "no":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Input Answer with Yes/No: ")
    else:
        print_menu()
        choice = input("Please Select Your choice(1-6): ")
        if choice == "1":
            add_project(projects)
        elif choice == "2":
            update_project(projects)
        elif choice == "3":
            delete_project(projects)
        elif choice == "4":
            view_projects(projects)
        elif choice == "5":
            winning_projects = simulate_random_selection(projects)
            answer = input("Do you need to Visualize the winners(yes/no)? ")
            if answer == "yes":
                visualization(winning_projects)
            elif answer == "no":
                print("Exiting the process")
                exit()
            else:
                print("Invalid Input use yes and no only")
                winning_projects = simulate_random_selection(projects)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    input("Press Enter to Continue")  # Added this line to display "Press any key to Continue"
