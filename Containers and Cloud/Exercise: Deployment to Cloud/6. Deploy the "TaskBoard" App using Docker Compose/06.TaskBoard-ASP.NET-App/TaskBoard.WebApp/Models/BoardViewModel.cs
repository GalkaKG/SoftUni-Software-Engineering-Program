using System.Collections.Generic;

using TaskBoard.WebApp.Models.Task;

namespace TaskBoard.WebApp.Models
{
    public class BoardViewModel
    {
        public int Id { get; init; }

        public string Name { get; init; }

        public IEnumerable<TaskViewModel> Tasks { get; set; } = new List<TaskViewModel>();
    }
}
