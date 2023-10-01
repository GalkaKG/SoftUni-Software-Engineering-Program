namespace TaskBoard.WebApp.Models.Task
{
    public class TaskDetailsViewModel : TaskViewModel
    {
        public string CreatedOn { get; init; }

        public string Board { get; init; }
    }
}
