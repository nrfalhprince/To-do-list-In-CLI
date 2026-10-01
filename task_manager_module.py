class TaskManager:

    def __init__(self):
        self.pages: list[str] = []
        self.total_of_page: int = 0

        try:
            with open(file="to-do pages name.txt", mode="r") as file:
                for row in file:
                    row = row[:len(row) - 1]
                    self.pages.append(row)

                self.total_of_page = len(self.pages)

        except FileNotFoundError:
            ...

    def add_a_page(self) -> None:
        self.total_of_page += 1
        file_name_and_path: str = F"Task list page{self.total_of_page}.txt"

        with open(file="to-do pages name.txt", mode="a") as file:
            file.write(F"{file_name_and_path}\n")

        with open(file=file_name_and_path, mode="w") as file:
            file.write("=======Todo list=======\n")
            print("Todo list was added!")
       
    
    def add_tasks(self) -> None:
        if len(self.pages) == 1:
            task: str = input("Add a task: ")

            with open(file="Task list page1.txt", mode="a") as file:        
                while True:
                    file.write(F"-{task}\n")
                    task: str = input("Add another task (type \"0\" to quit): ")
                    
                    if task == "0":
                        print()
                        return

        elif len(self.pages) > 1:
            print(self.pages)
            while True:
                try:
                    task_list_number: int = int(input("Which task list that you want to update the task? (choose the number of the task list!) \n>"))
                    
                    if task_list_number > len(self.pages):
                        print(F"Todo list page number \"{task_list_number}\" was not found!")
                        continue

                    else:
                        task: str = input("Add a task: ")
                        break

                except ValueError:
                    print("Please input number only!")

            with open(file=self.pages[task_list_number - 1], mode="a") as file:        
                while True:
                    file.write(F"-{task}\n")
                    task: str = input("Add another task (type \"0\" to quit): ")
                    
                    if task == "0":
                        print()
                        return



    def show_task(self) -> None:
        if len(self.pages) == 1:
            with open(file="Task list page.txt", mode="r") as file:
                for row in file:
                    print(row, end="")

        elif len(self.pages) > 1:
            while True:
                try:
                    task_list_number: int = int(input("Which task list that you want to show the task? (choose the number of the task list!) \n>"))
                    
                    if task_list_number > len(self.pages):
                        print(F"Todo list page number \"{task_list_number}\" was not found!")
                        continue

                    else:
                        break

                except ValueError:
                    print("Please input number only!")

            with open(file=self.pages[task_list_number - 1], mode="r") as file:
                for row in file:
                    print(row, end="")


    def remove_task(self) -> None:
        ...


    def check_the_task(self) -> None:
        ...
