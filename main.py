import os

file = open('tasks.txt', 'a')

class Todo:
    def __init__(self) -> None:
        read_file = open('tasks.txt', 'r')
        self.task_list = read_file.readlines()

    def add(self, task):
        self.task_list.append(task)

    def remove_task(self, index):
        self.task_list.pop(index)

    def complete(self, index):
        self.task_list[index] = '\u0336' + '\u0336'.join(self.task_list[index]) # Add strike through effect

    def showTask(self):
        for index, tasks in enumerate(self.task_list):
            print(f"[{index}] {tasks.strip()}")
        
    def edit(self, index, new_task):
        self.task_list[index] = new_task
    
    def prioritize(self, index, new_index):
        self.task_list.insert(new_index, self.task_list[index])
        self.task_list.pop(index+1)

    def empty(self):
            self.task_list = []

    def save(self):
        write_file = open('tasks.txt', 'w', encoding='utf-8')
        for task in self.task_list:
            write_file.write(f"{task.strip()}\n")

todo = Todo()

def main():
    while True:
        try:
            inp = input(">>> ")
            argument = inp.split(' ')
            command = argument[0].lower()

            if command == "add":
                task = inp[4::]
                if task != '':
                    todo.add(task)

            elif command == "remove" or command == "rmv":
                index = int(argument[1])
                todo.remove_task(index)

            elif command == "complete" or command == "com":
                index = int(argument[1])
                todo.complete(index)

            elif command == "edit" or command == "edt":
                index = int(argument[1])
                todo.edit(index, inp[7::])

            elif command == "prioritize" or command == "pri":
                index = int(argument[1])
                new_index = int(argument[2])
                todo.prioritize(index, new_index)
            
            elif command == "show":
                if len(todo.task_list) == 0:
                    print("None")
                else:
                    todo.showTask()
            
            elif command == "empty":
                if len(argument) > 1:
                    flag = argument[1].lower()
                    if flag == '-y':
                        todo.empty()
                else:
                    print("All the tasks will be deleted")
                    confirm = input("Are you sure? [Y/N]: ")
                    if confirm.lower() == "y" or confirm.lower() == "yes":
                        todo.empty()

            elif command == "cls" or command == "clear":
                os.system("cls")
            
            elif command == "exit" or command == "quit":
                quit()

            todo.save()

        except Exception as why:
            if why == KeyboardInterrupt:
                file.close()
                quit()
            else:
                print(why)

if __name__=='__main__':
    main()
