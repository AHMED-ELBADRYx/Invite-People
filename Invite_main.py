StringLetter_file = r"Input\Letters\StringLetter.txt"
InvitedName_file = r"Names\Invited_name.txt"

def Read_StringLetter_file():
    with open(StringLetter_file, "r") as file:
        return file.read()

def Read_InvitedName_file():
    with open(InvitedName_file, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]
    
def Generate_StringLetters():
    for line in Read_InvitedName_file():
        New_letter = Read_StringLetter_file().replace("user", line).replace("Team", "Ahmed Elbadry")
        Output_file = fr"D:\vs code projects\newProject\Invite people\Output\Ready to send\Letter_for_{line}.txt"
        with open(Output_file, "w") as file:
            file.write(New_letter)
        print(f"Letter for {line.strip()} has been generated and saved as {Output_file}")

Generate_StringLetters()