from task_manager_module import TaskManager

def main() -> None:

    while True:
        to_do_list: TaskManager = TaskManager()
        print("=======Python To-do List=======\n"
              "1. Add a to-do page\n"
              "2. Add to-do task\n"
              "3. Show to-do list\n"
              "4. Check the task (Still in progress)\n"
              "5. Remove the task (Still in progress)\n"
              "6. Exit from the apk")

        user_choice: str = input("Select the option by typing the number!\n>")

        if user_choice == "1":
            to_do_list.add_a_page()

        elif user_choice == "2":
            to_do_list.add_tasks()

        elif user_choice == "3":
            to_do_list.show_task()

        elif user_choice == "4":
            print("Still in progress")    

        elif user_choice == "5":
            print("Still in progress")

        elif user_choice == "6":
            print("Exit from the to-do apk")
            break
        
        else:
            print("Your choice is not recognized!")


if __name__ == "__main__":
    main()
